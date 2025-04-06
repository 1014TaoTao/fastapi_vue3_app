# -*- coding: utf-8 -*-

import json
import mimetypes
from pathlib import Path
import aiofiles
from fastapi import File, Query, Request, APIRouter, Depends, Path, Body, UploadFile
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, desc, func, select, asc, and_
from typing import Dict, Union
from datetime import datetime, timedelta


from app.api.model import User
from app.api.schema import (
    LogoutSchema,
    RegisterSchema,
    ForgotPasswordSchema,
    JWTPayloadSchema,
    JWTOutSchema,
    Page,
    UserSchema,
    UserOutSchema,
)
from app.core.security import (
    create_access_token,
    decode_access_token,
    set_password_hash,
    verify_password,
)
from app.core.config import settings
from app.core.dependencies import get_current_user
from app.core.log import logger
from app.core.response import ExceptResponse, ErrorResponse, SuccessResponse
from app.core.database import get_db


router: APIRouter = APIRouter(prefix="/api")

@router.post(path="/login", summary="登录", response_model=JWTOutSchema)
async def login(
    request: Request,
    login_form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(dependency=get_db),
) -> Union[JSONResponse, Dict]:
    """用户登录"""
    try:
        # 用户认证
        existing_obj: User | None = db.exec(
            select(User).where(User.username == login_form.username)
        ).first()
        if not existing_obj:
            logger.warning(f"用户{login_form.username}不存在")
            return ErrorResponse(message="用户不存在")
        if existing_obj.disabled:
            logger.warning(f"用户{login_form.username}已禁用")
            return ErrorResponse(message="用户已禁用")
        if not verify_password(
            plain_password=login_form.password, password_hash=existing_obj.password
        ):
            logger.warning(f"用户 {login_form.username} 密码错误")
            return ErrorResponse(message="密码错误")

        access_expires: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        access_token: str = create_access_token(
            payload=JWTPayloadSchema(
                sub=existing_obj.username,
                exp=datetime.now() + access_expires,
            )
        )

        login_token: JWTOutSchema = JWTOutSchema(
            access_token=access_token,
            token_type=settings.TOKEN_TYPE,
            expires_in=access_expires.total_seconds(),
            user_info=UserOutSchema.model_validate(existing_obj).model_dump(),
        )

        logger.info(f"用户{existing_obj.username}登录成功")

        # 如果是文档请求，则不记录日志:http://localhost:8000/api/v1/docs
        if "docs" in request.headers.get("referer", ""):
            return login_token.model_dump()

        return SuccessResponse(data=login_token.model_dump())
    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.patch(path="/forgot_password", summary="忘记密码")
async def forgot_password(
    payload: ForgotPasswordSchema, db: Session = Depends(dependency=get_db)
) -> JSONResponse:
    """忘记密码"""
    try:
        user: User | None = db.exec(
            select(User).where(User.username == payload.username)
        ).first()
        if not user:
            logger.warning(f"账号{payload.username}不存在")
            return ErrorResponse(message="用户不存在")
        if user.disabled:
            logger.warning(f"账号{payload.username}已禁用")
            return ErrorResponse(message="用户已禁用")
        if not verify_password(
            plain_password=payload.old_password, password_hash=user.password
        ):
            logger.warning(f"账号{payload.username}密码错误")
            return ErrorResponse(message="用户名或密码错误")
        if payload.new_password != payload.confirm_password:
            logger.warning(f"账号{payload.username}新密码与确认密码不一致")
            return ErrorResponse(message="新密码与确认密码不一致")

        new_hash_password: str = set_password_hash(password=payload.new_password)
        user.password = new_hash_password
        user.updated_at = datetime.now()
        db.add(instance=user)
        db.commit()
        db.refresh(instance=user)

        logger.info(f"账号{payload.username}修改密码成功")
        return SuccessResponse(data=True)
    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.post(path="/register", summary="注册用户", response_model=UserOutSchema)
async def register(
    payload: RegisterSchema,
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    """注册用户"""
    try:
        if not payload.name and payload.username and payload.password:
            logger.warning("注册用户失败，参数不完整")
            return ErrorResponse(message="注册失败，必填项不可以为空")
        existing_obj: User | None = db.exec(
            select(User).where(User.username == payload.username)
        ).first()
        if existing_obj:
            logger.warning(f"注册用户失败，账号{payload.username}已存在")
            return ErrorResponse(message="账号已存在")

        payload.password = set_password_hash(password=payload.password)
        obj_db: User = User.model_validate(obj=payload)
        db.add(instance=obj_db)
        db.commit()
        db.refresh(instance=obj_db)

        logger.info(f"账号 {payload.username} 注册成功")

        return SuccessResponse(data=UserOutSchema.model_validate(obj_db).model_dump())
    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.post(path="/logout", summary="退出登录", dependencies=[Depends(dependency=get_current_user)])
async def logout(
    request: Request,
    payload: LogoutSchema,
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    try:
        jwt_payload: JWTPayloadSchema = decode_access_token(token=payload.token)
        username: str = jwt_payload.sub
        existing_obj: User | None = db.exec(
            select(User).where(User.username == username)
        ).first()
        if not existing_obj:
            logger.warning(f"用户{username}不存在")
            return ErrorResponse(message="用户不存在")
        if existing_obj.disabled:
            logger.warning(f"用户{username}已禁用")
            return ErrorResponse(message="用户已禁用")

        request.scope["user_id"] = None

        logger.info(f"{username} 用户退出登录成功")
        return SuccessResponse(data=True)

    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.post(path='/upload', summary="上传文件", dependencies=[Depends(dependency=get_current_user)])
async def upload_file(
    request: Request,
    file: UploadFile = File(...)
):
    """上传文件"""
    try:
        if not file.filename or not file.content_type:
            logger.warning(f"文件不支持")
            return ErrorResponse(message=f"{file.filename} 文件不支持")
        file_extension = mimetypes.guess_extension(file.content_type)
        if not file_extension in settings.ALLOWED_EXTENSIONS:
            logger.warning(f"文件 {file.filename} 格式不支持上传")
            return ErrorResponse(message=f"{file.filename} 文件不允许上传")
        if file.size and file.size > settings.MAX_FILE_SIZE:
            logger.warning(f"文件 {file.filename} 大小不可以超过10MB")
            return ErrorResponse(message=f"{file.filename} 文件大小超过限制10MB")
        
        # 构建文件名称
        name, ext = file.filename.rsplit(".", 1)
        filename = f'{name}_{datetime.now().strftime("%Y%m%d%H%M%S")}{settings.UPLOAD_MACHINE}.{ext}'

        # 构建文件路径
        dir_path = settings.UPLOAD_FILE_PATH
        dir_path.mkdir(parents=True, exist_ok=True)
        filepath = dir_path / filename

        # 分块写入文件
        chunk_size = 8 * 1024 * 1024  # 8MB chunks
        async with aiofiles.open(filepath, 'wb') as f:
            while chunk := await file.read(chunk_size):
                await f.write(chunk)

        # 返回相对路径
        logger.info(f"文件 {file.filename} 上传成功，路径为 {filepath}")
        return SuccessResponse(data=f'{request.base_url}{filepath}')
    
    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.get(path="/users", summary="用户分页", response_model=Page, dependencies=[Depends(dependency=get_current_user)])
async def list_user(
    offset: int = Query(default=0, description="偏移量"),
    limit: int = Query(default=10, description="每页数量"),
    order_by: str | None = Query(default=None, description="排序字段", example={"id": "asc"}),
    name: str | None = Query(default=None, description="名称"),
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    try:
        sql = select(User)
        if name:
            sql = sql.where(and_(User.name.contains(name)))

        # 获取总数
        total: int | None = db.exec(select(func.count()).select_from(User)).one()
        
        if total is None:
            total = 0

        # 处理排序
        if order_by:
            try:
                order_by_dict = json.loads(order_by)
                for key, value in order_by_dict.items():
                    if not hasattr(User, key):
                        logger.warning(f"无效的排序字段: {key}")
                        return ErrorResponse(message=f"无效的排序字段: {key}")
                    order_func = desc if value.lower() == "desc" else asc
                    sql = sql.order_by(order_func(getattr(User, key)))
            except json.JSONDecodeError:
                logger.warning("排序参数格式错误")
                raise ExceptResponse(message="排序参数格式错误")

        # 分页
        objs = db.exec(sql.offset(offset).limit(limit)).all()

        logger.info("查询用户成功")
        return SuccessResponse(
            data=Page(
                items=[UserOutSchema.model_validate(obj).model_dump() for obj in objs],
                total=total,
                page_no=offset // limit + 1 if limit else 1,
                page_size=limit,
                total_pages=(total + limit - 1) // limit if limit else 1,
                has_next=offset + limit < total,
            ).model_dump()
        )

    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.post(path="/user", summary="创建用户", response_model=UserOutSchema, dependencies=[Depends(dependency=get_current_user)])
async def create_user(
    obj: UserSchema, db: Session = Depends(dependency=get_db)
) -> JSONResponse:
    """创建用户"""
    try:
        existing_obj: User | None = db.exec(
            select(User).where(User.username == obj.username)
        ).first()
        if existing_obj:
            logger.warning(f"创建用户失败：账号 {obj.username} 已存在")
            return ErrorResponse(message=f"账号 {obj.username} 已存在")

        obj.password = set_password_hash(password=obj.password)
        obj_db: User = User.model_validate(obj)
        db.add(instance=obj_db)
        db.commit()
        db.refresh(instance=obj_db)

        logger.info(f"用户 {obj.name} 创建成功")

        return SuccessResponse(data=UserOutSchema.model_validate(obj_db).model_dump())

    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.get(path="/user/{id}", summary="用户详情", response_model=UserOutSchema, dependencies=[Depends(dependency=get_current_user)])
async def detail_user(
    id: int = Path(default=..., description="用户ID"),
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    """获取用户详情"""
    try:
        existing_obj: User | None = db.get(User, id)
        if not existing_obj:
            logger.warning(f"用户{id}不存在")
            return ErrorResponse(message="用户不存在")

        logger.info(f"获取用户{id}详情成功")
        return SuccessResponse(
            data=UserOutSchema.model_validate(existing_obj).model_dump()
        )
    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.patch(path="/user/{id}", summary="更新用户", response_model=UserOutSchema, dependencies=[Depends(dependency=get_current_user)])
async def update_user(
    obj: UserSchema,
    id: int = Path(default=..., description="用户ID"),
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    """更新用户"""
    try:
        existing_obj: User | None = db.get(User, id)
        if not existing_obj:
            logger.warning(f"用户{id}不存在")
            return ErrorResponse(message=f"用户{id}不存在")
        if existing_obj.is_superuser:
            logger.warning("超级管理员不允许修改")
            return ErrorResponse(message="超级管理员不允许修改")
        
        update_data_dict = obj.model_dump(exclude_unset=True)
        existing_obj.sqlmodel_update(update_data_dict)
        existing_obj.updated_at = datetime.now()

        db.add(instance=existing_obj)
        db.commit()
        db.refresh(instance=existing_obj)

        logger.info(f"更新用户{id}成功")
        return SuccessResponse(
            data=UserOutSchema.model_validate(existing_obj).model_dump()
        )

    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")

@router.delete(path="/user/{id}", summary="删除用户", response_model=UserOutSchema, dependencies=[Depends(dependency=get_current_user)])
async def delete_user(
    id: int = Path(default=..., description="用户ID"),
    db: Session = Depends(dependency=get_db),
) -> JSONResponse:
    """删除用户"""
    try:
        existing_obj: User | None = db.get(User, id)
        if not existing_obj:
            logger.warning(f"用户{id}不存在")
            return ErrorResponse(message=f"用户{id}不存在")
        if existing_obj.is_superuser:
            logger.warning("超级管理员不允许删除")
            return ErrorResponse(message="超级管理员不允许删除")

        db.delete(instance=existing_obj)
        db.commit()
        logger.info(f"删除用户{id}成功")
        return SuccessResponse(
            data=UserOutSchema.model_validate(existing_obj).model_dump()
        )

    except Exception as e:
        logger.error(f"系统异常: {e}")
        raise ExceptResponse(message=f"系统异常: {e}")


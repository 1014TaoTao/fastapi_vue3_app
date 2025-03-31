# -*- coding: utf-8 -*-

from fastapi import Depends, Request
from sqlmodel import Session, select

from app.api.schema import JWTPayloadSchema
from app.api.model import User
from app.core.security import OAuth2Schema, decode_access_token
from app.core.database import get_db
from app.core.response import ExceptResponse


async def get_current_user(
    request: Request,
    token: str = Depends(dependency=OAuth2Schema),
    db: Session = Depends(dependency=get_db),
) -> User:
    try:
        # 处理Bearer token
        if token.startswith("Bearer"):
            token = token.split(sep=" ")[1]

        # 解析token
        payload: JWTPayloadSchema = decode_access_token(token=token)

        # 获取用户信息
        user: User | None = db.exec(
            select(User).where(User.username == payload.sub)
        ).first()
        if not user:
            raise ExceptResponse(message="用户不存在", status_code=401)
        if user.disabled:
            raise ExceptResponse(message="用户已被停用", status_code=401)

        # 设置请求上下文
        request.scope["user_id"] = user.id

        return user
    except Exception as e:
        raise ExceptResponse(message=f"获取用户信息异常: {e}")

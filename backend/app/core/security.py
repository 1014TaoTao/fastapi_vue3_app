# -*- coding: utf-8 -*-

import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.api.schema import JWTPayloadSchema
from app.core.config import settings
from app.core.response import ExceptResponse

# 密码加密配置
pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(secret=plain_password, hash=password_hash)


def set_password_hash(password: str) -> str:
    return pwd_context.hash(secret=password)


# OAuth2认证配置
OAuth2Schema: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="/api/login", description="认证"
)


def create_access_token(payload: JWTPayloadSchema) -> str:
    """生成JWT访问令牌"""
    return jwt.encode(
        payload=payload.model_dump(),
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def decode_access_token(token: str) -> JWTPayloadSchema:
    """解析JWT访问令牌"""
    if not token:
        raise ExceptResponse(message="认证不存在,请重新登录", status_code=403)

    try:
        payload = jwt.decode(
            jwt=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

        username = payload.get("sub")
        if not username:
            raise ExceptResponse(message="无效认证,请重新登录", status_code=403)

        return JWTPayloadSchema(**payload)

    except (jwt.InvalidSignatureError, jwt.DecodeError):
        raise ExceptResponse(message="无效认证,请重新登录", status_code=403)

    except jwt.ExpiredSignatureError:
        raise ExceptResponse(message="认证已过期,请重新登录", status_code=403)

    except jwt.InvalidTokenError:
        raise ExceptResponse(message="token已失效,请重新登录", status_code=403)

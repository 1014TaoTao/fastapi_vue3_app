from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Any, Union, Annotated, Union
from pydantic import AfterValidator, PlainSerializer, WithJsonSchema


def datetime_validator(value: Union[str, datetime]) -> Union[str, datetime, None]:
    """
    日期格式验证器
    """
    pattern = "%Y-%m-%d %H:%M:%S"
    if isinstance(value, str):
        value = datetime.strptime(value, pattern)
    elif isinstance(value, datetime):
        value = value.strftime(pattern)
    return value


DateTimeStr = Annotated[
    datetime,
    AfterValidator(lambda x: datetime_validator(x)),
    PlainSerializer(lambda x: x, return_type=str),
    WithJsonSchema({"type": "string"}, mode="serialization"),
]


class BaseSchema(SQLModel):
    """用户返回模型"""

    id: int = Field(default=..., description="自增ID")
    created_at: DateTimeStr = Field(default=..., description="创建时间")
    updated_at: DateTimeStr = Field(default=..., description="更新时间")


class Response(SQLModel):
    """响应模型"""

    code: int = 200
    message: str = ""
    data: Any = None


class Page(SQLModel):
    """分页模型"""

    items: list = Field(default=[], description="数据列表")
    total: int = Field(default=0, description="总记录数")
    page_no: int = Field(default=1, description="当前页码")
    page_size: int = Field(default=10, description="每页数量")
    total_pages: int = Field(default=0, description="总页数")
    has_next: bool = Field(default=False, description="是否有下一页")


class JWTPayloadSchema(SQLModel):
    """JWT载荷模型"""

    sub: str = Field(default=..., description="用户账号")
    exp: Union[datetime, int] = Field(default=..., description="过期时间")


class JWTOutSchema(SQLModel):
    """JWT响应模型"""

    access_token: str = Field(default=..., description="访问token")
    token_type: str = Field(default="Bearer", description="token类型")
    expires_in: float = Field(default=..., gt=0, description="过期时间(秒)")
    user_id: int | None = Field(description="用户ID")


class LogoutPayloadSchema(SQLModel):
    """退出登录载荷模型"""

    token: str = Field(default=..., min_length=1, description="token")


class ForgotPasswordSchema(SQLModel):
    """忘记密码模型"""

    username: str = Field(default=..., description="账号")
    old_password: str = Field(default=..., description="旧密码")
    new_password: str = Field(default=..., description="新密码")
    confirm_password: str = Field(default=..., description="确认密码")


class RegisterSchema(SQLModel):
    """注册模型"""

    name: str = Field(default=..., description="用户名")
    username: str = Field(default=..., description="账号")
    password: str = Field(default=..., description="密码")


class BaseUserOut(SQLModel):
    """用户基础模型"""

    name: str | None = Field(default=None, description="用户名")
    username: str | None = Field(default=None, description="登录账号")
    disabled: bool | None = Field(default=False, description="是否禁用")
    description: str | None = Field(default=None, description="用户描述信息")
    parent_id: int | None = Field(default=None, description="上级用户ID")


class UserSchema(BaseUserOut):
    """用户模型"""

    password: str = Field(default=None, max_length=255, description="密码")


class User2Schema(BaseSchema, BaseUserOut):
    """用户返回模型"""

    ...
    is_superuser: bool | None = Field(default=False, description="是否超级管理员")

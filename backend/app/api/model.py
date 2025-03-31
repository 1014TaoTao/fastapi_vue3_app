# -*- coding: utf-8 -*-

from datetime import datetime
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """系统用户表，存储平台所有用户信息"""
    id: int | None = Field(default=None, primary_key=True, description="用户ID")
    name: str = Field(index=True, nullable=False, max_length=50, description="用户名")
    username: str = Field(unique=True, max_length=50, description="登录账号")
    password: str = Field(max_length=255, description="加密后的密码")
    disabled: bool = Field(default=False, description="是否禁用(True:禁用 False:启用)")
    is_superuser: bool = Field(default=False, description="是否超级管理员")
    description: str | None = Field(default=None, max_length=500, description="用户描述信息")
    created_at: datetime = Field(default_factory=datetime.now, description='创建时间')
    updated_at: datetime = Field(default_factory=datetime.now, description='更新时间')

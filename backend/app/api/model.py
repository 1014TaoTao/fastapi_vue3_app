# -*- coding: utf-8 -*-

from datetime import datetime
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """系统用户表，存储平台所有用户信息"""
    id: int | None = Field(default=None, primary_key=True, description="ID")
    name: str = Field(index=True, nullable=False, max_length=50, description="名称")
    username: str = Field(unique=True, max_length=50, description="登录账号")
    password: str = Field(max_length=255, description="哈希密码")
    avatar: str | None = Field(default="https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png", max_length=255, description="头像")
    available: bool = Field(default=True, description="是否激活(True:启用 False:禁用)")
    is_superuser: bool = Field(default=False, description="是否超级管理员")
    description: str | None = Field(default=None, max_length=255, description="备注")
    created_at: datetime = Field(default_factory=datetime.now, description='创建时间')
    updated_at: datetime = Field(default_factory=datetime.now, description='更新时间')

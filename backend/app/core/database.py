# -*- coding: utf-8 -*-

from sqlalchemy.engine.base import Engine
from collections.abc import Generator
from sqlmodel import SQLModel, create_engine, Session, select, or_

from app.core.config import settings
from app.core.response import ExceptResponse
from app.core.log import logger

# 创建数据库引擎，增加连接池配置
engine: Engine = create_engine(
    url=settings.DATABASE_URL, echo=False, connect_args={"check_same_thread": False})


def get_db() -> Generator[Session, None, None]:
    """获取数据库会话连接"""
    with Session(bind=engine) as session:
        yield session


def create_db_and_tables() -> None:
    try:
        from app.api.model import User

        with Session(bind=engine) as session:
            # SQLModel.metadata.drop_all(bind=engine)
            # SQLModel.metadata.create_all(bind=engine)

            if session.exec(select(User).where(
                or_(
                    User.username == "admin", 
                    User.username == "test", 
                    User.username == "demo"
                    )
                )).first():
                logger.info("管理员、测试、演示用户已存在，无需创建")
                return
            users = [
                User(
                    name="管理员",
                    username="admin",
                    password="$2b$12$rjGmN9msqoZJy/IG4ScfwuHTFBI4O33gAKQuTmk.p/K.No6AaW.tC",
                    is_superuser=True,
                    description="系统管理员",
                ),
                User(
                    name="测试用户",
                    username="test",
                    password="$2b$12$rjGmN9msqoZJy/IG4ScfwuHTFBI4O33gAKQuTmk.p/K.No6AaW.tC",
                    is_superuser=False,
                    description="测试用户",
                ),
                User(
                    name="演示用户",
                    username="demo",
                    password="$2b$12$rjGmN9msqoZJy/IG4ScfwuHTFBI4O33gAKQuTmk.p/K.No6AaW.tC",
                    is_superuser=False,
                    description="演示用户",
                ),
            ]

            session.add_all(users)
            session.commit()
            logger.info("初始化数据成功")

    except Exception as e:
        raise ExceptResponse(message=f"初始化数据异常: {str(e)}")

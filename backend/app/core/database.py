# -*- coding: utf-8 -*-

from sqlalchemy.engine.base import Engine
from collections.abc import Generator
from sqlmodel import SQLModel, create_engine, Session, select

from app.core.security import set_password_hash
from app.core.logger import logger
from app.core.config import settings
from app.core.response import ExceptResponse

# 创建数据库引擎，增加连接池配置
engine: Engine = create_engine(
    url=settings.DATABASE_URL,
    echo=False,
    pool_size=20,
    max_overflow=0,
    connect_args={"check_same_thread": False},
)


def get_db() -> Generator[Session, None, None]:
    """获取数据库会话连接"""
    with Session(bind=engine) as session:
        yield session


def read_json():
    import json
    with open(settings.data_path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


async def create_db_and_tables() -> None:
    try:
        from app.api.model import (User)

        with Session(bind=engine) as session:
            SQLModel.metadata.drop_all(bind=engine)
            SQLModel.metadata.create_all(bind=engine)

            if session.exec(select(User).where(User.username == "admin")).first():
                logger.info("初始化数据已存在")
                return
            admin = User(
                id=1,
                name="管理员",
                username="admin",
                password=set_password_hash(password="123456"),
                disabled=False,
                is_superuser=True,
                description="管理员",
                parent_id=None,
            )

            session.add(admin)
            session.commit()

            logger.info("初始化数据成功")

    except Exception as e:
        logger.error(f"初始化数据失败: {e}")
        raise ExceptResponse(message=f"初始化数据异常: {str(e)}")

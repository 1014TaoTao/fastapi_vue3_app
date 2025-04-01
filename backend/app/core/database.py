# -*- coding: utf-8 -*-

from sqlalchemy.engine.base import Engine
from collections.abc import Generator
from sqlmodel import SQLModel, create_engine, Session, select

from app.core.config import settings
from app.core.response import ExceptResponse
from app.core.log import logger

# 创建数据库引擎，增加连接池配置
engine: Engine = create_engine(url=settings.DATABASE_URL, echo=False, connect_args = {"check_same_thread": False})

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

            if session.exec(select(User).where(User.username == "admin")).first():
                logger.info("管理员用户已存在，无需创建")
                return
            admin = User(
                name="管理员",
                username="admin",
                password="$2b$12$rjGmN9msqoZJy/IG4ScfwuHTFBI4O33gAKQuTmk.p/K.No6AaW.tC",
                is_superuser=True,
                avatar="https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png"
            )
            
            session.add(admin)
            session.commit()
            session.refresh(admin)
            logger.info("管理员用户创建成功")

    except Exception as e:
        raise ExceptResponse(message=f"初始化数据异常: {str(e)}")

# -*- coding: utf-8 -*-

from collections.abc import AsyncGenerator
import typer
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.concurrency import asynccontextmanager
from alembic import command
from alembic.config import Config

from app.core.middlewares import register_middleware_handler
from app.core.exceptions import register_exception_handlers
from app.api.controller import router
from app.core.log import logger, uvicorn_logger
from app.core.config import settings


app = typer.Typer()
# 初始化 Alembic 配置
alembic_cfg: Config = Config(file_="alembic.ini")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """
    自定义生命周期
    """
    try:
        logger.info(f"服务启动...{settings.BANNER}")
        from app.core.database import create_db_and_tables

        create_db_and_tables()
        yield
    except Exception as e:
        logger.error(f"服务启动失败: {e}")
        raise e
    finally:
        logger.info(f"服务关闭...{app.title}")


def create_app() -> FastAPI:

    # 创建FastAPI应用
    app: FastAPI = FastAPI(lifespan=lifespan, debug=True)

    # 挂载静态文件
    app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

    # 注册中间件
    register_middleware_handler(app)

    # 注册异常处理器
    register_exception_handlers(app)

    # 注册路由
    app.include_router(router=router)

    return app


@app.command()
def revision(message: str | None = "生成新的 Alembic 迁移脚本") -> None:
    """
    生成新的 Alembic 迁移脚本。
    """
    command.revision(config=alembic_cfg, message=message, autogenerate=True)
    typer.echo(message=f"生成新的 Alembic 迁移脚本")


@app.command()
def upgrade() -> None:
    """
    应用最新的 Alembic 迁移。
    """
    command.upgrade(config=alembic_cfg, revision="head")
    typer.echo(message="所有迁移已应用。")


@app.command()
def run() -> None:
    """
    启动应用。
    """
    import uvicorn

    uvicorn.run(
        app="main:create_app",
        host="localhost",
        port=8000,
        reload=True,
        factory=True,
        log_config=uvicorn_logger(),
    )


if __name__ == "__main__":

    app()

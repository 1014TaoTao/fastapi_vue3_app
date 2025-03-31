# -*- coding: utf-8 -*-

from collections.abc import AsyncGenerator
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.concurrency import asynccontextmanager

from app.core.logger import logger
from app.core.middlewares import register_middleware_handler


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    自定义生命周期
    """
    try:
        logger.info(f"服务启动...{app.title}")
        from app.core.database import create_db_and_tables
        await create_db_and_tables()
        yield
    finally:
        logger.info(f"服务关闭...{app.title}")


def create_app() -> FastAPI:

    # 创建FastAPI应用
    app: FastAPI = FastAPI(lifespan=lifespan, debug=True)

    # 挂载静态文件
    app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

    # 注册中间件
    register_middleware_handler(app)


    # 注册路由
    from app.api.controller import router

    Router: APIRouter = APIRouter(prefix="/api")
    Router.include_router(router=router)
    app.include_router(router=Router)

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:create_app", host="localhost", port=8000, reload=True, factory=True
    )

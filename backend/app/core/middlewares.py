# -*- coding: utf-8 -*-

import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.types import ASGIApp

from app.core.logger import logger


class CustomCORSMiddleware(CORSMiddleware):
    """CORS跨域中间件"""

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(
            app,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
            allow_credentials=True,
        )


class RequestLogMiddleware(BaseHTTPMiddleware):
    """
    记录请求日志中间件: 提供详细的请求和响应日志记录，便于问题排查
    """

    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time: float = time.time()

        logger.info(
            f"客户端IP: {request.client.host if request.client else '未知'} | "
            f"方法: {request.method} | 路径: {request.url.path} | "
            f"查询参数: {request.query_params} | "
            f"请求体参数: {(await request.body()).decode(encoding='utf-8')}"
        )

        response = await call_next(request)

        process_time = round(time.time() - start_time, 5)
        response.headers["X-Process-Time"] = str(process_time)

        logger.info(
            f"响应状态: {response.status_code}, "
            f"响应内容长度: {response.headers.get('content-length', '0')}, "
            f"处理时间: {process_time}s"
        )

        return response


def register_middleware_handler(app: FastAPI) -> None:
    app.add_middleware(middleware_class=CustomCORSMiddleware)
    app.add_middleware(middleware_class=RequestLogMiddleware)

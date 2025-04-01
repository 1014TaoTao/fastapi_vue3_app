# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.core.response import ErrorResponse
from app.core.log import logger


def register_exception_handlers(app: FastAPI) -> None:
    """注册异常处理器"""

    app.exception_handler(HTTPException)
    async def HttpExceptionHandler(
        request: Request, exc: HTTPException
    ) -> JSONResponse:
        """HTTP异常处理器"""
        logger.error(f"请求地址: {request.url}, 错误详情: {exc.detail}")
        return ErrorResponse(message=exc.detail, status_code=exc.status_code)


    app.exception_handler(RequestValidationError)
    async def RequestValidationHandler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        """请求参数验证异常处理器"""
        error_mapping = {
            "Field required": "请求失败，缺少必填项！",
            "value is not a valid list": "类型错误，提交参数应该为列表！",
            "value is not a valid int": "类型错误，提交参数应该为整数！",
            "value could not be parsed to a boolean": "类型错误，提交参数应该为布尔值！",
            "Input should be a valid list": "类型错误，输入应该是一个有效的列表！",
        }

        msg = error_mapping.get(exc.errors()[0].get("msg"), exc.errors()[0].get("msg"))
        if not msg:
            msg = exc.errors()[0].get("msg")
        logger.error(f"请求地址: {request.url}, 错误信息: {msg}, 错误详情: {exc}")
        return ErrorResponse(
            message=msg, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, data=exc.body
        )

    app.exception_handler(ResponseValidationError)
    async def ResponseValidationHandle(
        request: Request, exc: ResponseValidationError
    ) -> JSONResponse:
        logger.error(f"请求地址: {request.url}, 错误详情: {exc}")
        return ErrorResponse(
            message=str(exc),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data=exc.body,
        )

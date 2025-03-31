
# -*- coding: utf-8 -*-

from typing import Any, Dict, Optional
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

from app.api.schema import Response


class SuccessResponse(JSONResponse):
    """成功响应类"""

    def __init__(
            self,
            data: Any | None = None,
            message: str = "success",
            status_code: int = status.HTTP_200_OK,
    ) -> None:
        """
        初始化成功响应类
        """
        content: Dict[str, Any] = Response(
            code=status_code,
            message=message,
            data=data,
        ).model_dump()
        super().__init__(content=content, status_code=status_code)


class ErrorResponse(JSONResponse):
    """错误响应类"""

    def __init__(
            self,
            data: Any | None = None,
            message: str = "error",
            status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> None:
        """
        初始化错误响应类
        """
        content: Dict[str, Any] = Response(
            code=status_code,
            message=message,
            data=data,
        ).model_dump()
        super().__init__(content=content, status_code=status_code)


class ExceptResponse(HTTPException):
    """异常响应类"""

    def __init__(
            self,
            data: Optional[Any] = None,
            message: str = "network error...",
            status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        """
        初始化错误响应类
        """
        content: Dict[str, Any] = Response(
            code=status_code,
            message=message,
            data=data,
        ).model_dump()
        super().__init__(detail=content, status_code=status_code)

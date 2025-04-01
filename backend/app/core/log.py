# -*- coding: utf-8 -*-

import logging
from datetime import date
from logging.handlers import TimedRotatingFileHandler

from app.core.config import settings


class LoggerHandler:
    """日志处理器类，用于配置和管理日志"""

    def __init__(self) -> None:
        """初始化日志处理器"""
        self.log_path = settings.BASE_DIR.joinpath("logs")
        self.log_path.mkdir(parents=True, exist_ok=True)

        self.logger_name: str = date.today().strftime(r"%Y-%m-%d.log")
        self.filename = self.log_path.joinpath(self.logger_name)
        self.log_format: str = (
            "%(asctime)s - %(levelname)s - [%(name)s:%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
        )
        self.log_level: str = "INFO"
        
        
        self.when = "MIDNIGHT"
        self.interval = 1
        self.backup_count = 10
        self.encoding = "utf-8"

        self.logger = logging.getLogger(__name__)
        self._configure_logger()

    def _configure_logger(self) -> None:
        """配置日志处理器"""
        try:
            # 清除现有处理器
            self.logger.handlers.clear()

            # 设置日志级别
            self.logger.setLevel(self.log_level)

            # 配置日志格式
            self.formatter = logging.Formatter(fmt=self.log_format)

            # 配置文件处理器
            file_handler = TimedRotatingFileHandler(
                filename=self.filename,
                when=self.when,
                interval=self.interval,
                backupCount=self.backup_count,
                encoding=self.encoding,
            )
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(self.formatter)
            self.logger.addHandler(file_handler)

            # 配置控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(self.formatter)
            self.logger.addHandler(console_handler)
        except Exception as e:
            self.logger.error(f"日志配置失败: {e}")

    def __enter__(self) -> logging.Logger:
        """上下文管理器入口"""
        return self.logger

    def _uvicorn_logger(self) -> dict:
        """配置uvicorn日志处理器
        
        Returns:
            dict: uvicorn日志配置字典
        """
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": self.log_format,
                    "use_colors": None,
                },
                "access": {
                    "()": "uvicorn.logging.AccessFormatter",
                    "fmt": self.log_format,
                },
            },
            "handlers": {
                "console": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stderr",
                },
                "access_console": {
                    "formatter": "access",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                },
                "file": {
                    "formatter": "default",
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "filename": self.filename,
                    "interval": self.interval,
                    "when": self.when,
                    "backupCount": self.backup_count,
                    "encoding": self.encoding,
                },
            },
            "loggers": {
                "uvicorn": {
                    "handlers": ["file", "console"],
                    "level": self.log_level,
                    "propagate": False,
                },
                "uvicorn.error": {
                    "handlers": ["file", "console"],
                    "level": self.log_level,
                    "propagate": False,
                },
                "uvicorn.access": {
                    "handlers": ["file", "access_console"],
                    "level": self.log_level,
                    "propagate": False,
                },
            },
        }


# 全局日志实例
logger = LoggerHandler().logger
uvicorn_logger = LoggerHandler()._uvicorn_logger

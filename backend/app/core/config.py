# -*- coding: utf-8 -*-

from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    # 项目根目录
    BASE_DIR: Path = Path(__file__).parent.parent.parent

    # sqlite 数据库名称
    SQLITE_DB_NAME: str = "sqlite.db"

    # token 类型
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    TOKEN_TYPE: str = "bearer"

    data_path: Path = BASE_DIR.joinpath("data.json")

    @property
    def DATABASE_URL(self) -> str:
        return f"sqlite:///{self.BASE_DIR.joinpath(self.SQLITE_DB_NAME)}?characterEncoding=UTF-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

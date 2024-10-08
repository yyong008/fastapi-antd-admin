from typing import Annotated, Any
from pydantic import AnyUrl, BeforeValidator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int
    DATABASE_URL: str
    DATABASE_URL_SYNC: str
    PRESENTATION_MODE: int
    DEBUG: bool
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    PORT: int
    OLLAMA_URL: str

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    settings = Settings()
    return settings

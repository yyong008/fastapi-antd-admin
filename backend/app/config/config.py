from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int
    DATABASE_URL: str
    PRESENTATION_MODE: int
    DEBUG: bool
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    PORT: int
    OLLAMA_URL: str

    model_config = SettingsConfigDict(env_file=".env")


# settings = Settings()

@lru_cache()
def get_settings():
    settings = Settings()
    return settings

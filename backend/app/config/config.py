from pydantic_settings import BaseSettings


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

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    SECRET_KEY: int
    DATABASE_URL: str
    HOST: str = "localhost"
    PORT: int = 8000
    RELOAD: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
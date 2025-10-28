from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    SECRET_KEY: int
    HOST: str = "localhost"
    PORT: int = 8000
    RELOAD: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True
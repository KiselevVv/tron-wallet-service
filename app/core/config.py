import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    TESTING: bool = False

    class Config:
        env_file = ".env.test" if os.getenv("TESTING") == "True" else ".env"


settings = Settings()

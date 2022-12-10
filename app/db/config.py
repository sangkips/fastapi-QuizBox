import os
from dotenv import load_dotenv

from pathlib import Path

env_file_path = Path(".") / ".env"

load_dotenv(dotenv_path=env_file_path)


class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv(" POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


"""  
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    REFRESH_SECRET_KEY: str = os.getenv('REFRESH_SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: str = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    REFRESH_TOKEN_EXPIRE_MINUTES: str = os.getenv(
        'REFRESH_TOKEN_EXPIRE_MINUTES')

"""
Settings = Settings()

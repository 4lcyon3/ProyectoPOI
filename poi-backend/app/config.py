from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # App
    APP_NAME: str = "POI Platform"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str | None = os.getenv('DATABASE_URL')
    
    # Security
    SECRET_KEY: str | None = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

settings = Settings()
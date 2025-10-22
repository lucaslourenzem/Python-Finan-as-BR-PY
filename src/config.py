"""
Configurações globais da aplicação usando Pydantic Settings
"""
from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Configurações principais da aplicação"""
    
    # App
    APP_NAME: str = "FinancialAPI"
    API_VERSION: str = "v1"
    DEBUG: bool = True
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # Database (opcional por enquanto)
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_DATABASE: str = "financial_db"
    DB_USERNAME: str = "financial_user"
    DB_PASSWORD: str = "changeme"
    
    # JWT (opcional por enquanto)
    JWT_SECRET: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 3600
    
    # NFe
    NFE_AMBIENTE: int = 2  # 1=Produção, 2=Homologação
    NFE_UF: str = "SP"
    
    # Redis (opcional por enquanto)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

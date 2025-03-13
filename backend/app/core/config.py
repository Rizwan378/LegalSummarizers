from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60  # seconds
    MAX_CSV_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]
    CACHE_TTL: int = 3600  # seconds

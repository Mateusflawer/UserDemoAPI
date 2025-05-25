from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key-here"  # Substitua por uma chave segura
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./users.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
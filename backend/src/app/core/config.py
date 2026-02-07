import os
import logging
from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Local dev: SQLite if DATABASE_URL not set. Production/Vercel: set DATABASE_URL to your Neon (or other PostgreSQL) URL.
def _default_db_url() -> str:
    url = os.getenv("DATABASE_URL", "").strip()
    if url and url.startswith("postgresql"):
        return url
    return "sqlite:///./test.db"

class Settings(BaseSettings):
    DATABASE_URL: str = ""
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me-at-runtime")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()

# Resolve DATABASE_URL: prefer env (PostgreSQL), else SQLite for local dev
if not settings.DATABASE_URL:
    settings.DATABASE_URL = _default_db_url()

if settings.DATABASE_URL.startswith("postgresql"):
    logger.info("Database: PostgreSQL")
else:
    logger.info("Database: SQLite (local dev)")

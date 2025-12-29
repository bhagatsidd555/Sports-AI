from pydantic import BaseSettings, Field
from functools import lru_cache


class Settings(BaseSettings):
    # =========================
    # Application
    # =========================
    APP_NAME: str = "Sports AI – Athlete Performance Analytics"
    ENVIRONMENT: str = "development"   # development | staging | production
    DEBUG: bool = True

    # =========================
    # Server
    # =========================
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    API_VERSION: str = "v1"

    # =========================
    # Security
    # =========================
    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    # =========================
    # AI / LLM Layer
    # =========================
    OPENAI_API_KEY: str | None = None
    AI_MODEL_NAME: str = "gpt-4.1-mini"
    AI_TEMPERATURE: float = 0.3
    AI_MAX_TOKENS: int = 800

    # =========================
    # Garmin / Wearable Data
    # =========================
    MAX_UPLOAD_SIZE_MB: int = 50
    ALLOWED_FILE_TYPES: list[str] = ["csv", "fit"]

    # =========================
    # Lean V1 Performance Thresholds
    # =========================
    SAFE_SPEED_DECAY_MAX: float = 10.0        # %
    SAFE_HR_DRIFT_MAX: float = 0.30           # correlation
    SAFE_ACWR_MIN: float = 0.8
    SAFE_ACWR_MAX: float = 1.3

    # =========================
    # Logging
    # =========================
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings instance (singleton)
    """
    return Settings()


settings = get_settings()

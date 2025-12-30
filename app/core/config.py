from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Global configuration for Sports-AI backend
    """

    # App
    APP_NAME: str = "Sports-AI Performance Analytics"
    ENV: str = "development"
    DEBUG: bool = True

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Data & Processing
    DEFAULT_LAP_DISTANCE: float = 400.0  # meters (speed skating rink)
    SMOOTHING_WINDOW: int = 5

    # Physiological thresholds
    MAX_HEART_RATE: int = 230
    MIN_HEART_RATE: int = 30

    MAX_SPEED: float = 15.0  # m/s (elite skating upper bound)
    MIN_SPEED: float = 0.0

    # Training load & fatigue
    ACWR_LOW: float = 0.8
    ACWR_HIGH: float = 1.3

    # AI Layer (future)
    ENABLE_AI_INSIGHTS: bool = True
    LLM_PROVIDER: str = "openai"  # openai / local / none

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

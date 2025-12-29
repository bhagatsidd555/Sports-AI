import logging
import sys
from app.core.config import settings


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter(settings.LOG_FORMAT)

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger

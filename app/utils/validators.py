import pandas as pd
from .constants import (
    MIN_HEART_RATE,
    MAX_HEART_RATE,
    MIN_SPEED,
    MAX_SPEED
)


def validate_dataframe(df: pd.DataFrame) -> None:
    """Ensure required columns exist"""
    required_columns = [
        "timestamp",
        "distance",
        "speed",
        "heart_rate"
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def validate_heart_rate(series):
    """Clamp heart-rate values to physiological limits"""
    return series.clip(MIN_HEART_RATE, MAX_HEART_RATE)


def validate_speed(series):
    """Clamp speed values to realistic bounds"""
    return series.clip(MIN_SPEED, MAX_SPEED)


def validate_monotonic_time(series):
    """Ensure timestamp is strictly increasing"""
    if not series.is_monotonic_increasing:
        raise ValueError("Timestamp sequence is not monotonic")


def validate_gps(lat, lon):
    """Basic GPS sanity check"""
    if lat.isnull().any() or lon.isnull().any():
        raise ValueError("GPS data contains null values")

import pandas as pd
from .constants import (
    MIN_HEART_RATE,
    MAX_HEART_RATE,
    MIN_SPEED,
    MAX_SPEED
)


def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate Garmin activity DataFrame for analytics safety
    Raises ValueError if data is invalid
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input is not a Pandas DataFrame")

    if df.empty:
        raise ValueError("DataFrame is empty")

    # Timestamp check
    if "timestamp" in df.columns:
        if df["timestamp"].isnull().all():
            raise ValueError("Timestamp column is fully empty")

    # Heart rate sanity
    if "heart_rate" in df.columns:
        hr = df["heart_rate"].dropna()
        if not hr.empty:
            if hr.min() < MIN_HEART_RATE or hr.max() > MAX_HEART_RATE:
                raise ValueError("Heart rate values out of physiological range")

    # Speed sanity
    if "speed" in df.columns:
        speed = df["speed"].dropna()
        if not speed.empty:
            if speed.min() < MIN_SPEED or speed.max() > MAX_SPEED:
                raise ValueError("Speed values out of realistic range")

    # Distance monotonicity (optional but recommended)
    if "distance" in df.columns:
        if not df["distance"].is_monotonic_increasing:
            raise ValueError("Distance must be cumulative and increasing")

    return

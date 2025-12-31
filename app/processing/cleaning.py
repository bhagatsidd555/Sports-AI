import pandas as pd
import numpy as np

# Physiological & sport-safe limits
MIN_HR = 30
MAX_HR = 220

MIN_SPEED = 0.0
MAX_SPEED = 20.0  # m/s (upper bound for speed skating)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw Garmin data:
    - sort by timestamp
    - handle missing values
    - remove physiological outliers
    """

    df = df.copy()

    # Sort by time
    if "timestamp" in df.columns:
        df = df.sort_values("timestamp")

    # Heart Rate cleaning
    if "heart_rate" in df.columns:
        df.loc[
            (df["heart_rate"] < MIN_HR) | (df["heart_rate"] > MAX_HR),
            "heart_rate"
        ] = np.nan

        df["heart_rate"] = (
            df["heart_rate"]
            .interpolate(method="linear")
            .bfill()
            .ffill()
        )

    # Speed cleaning
    if "speed" in df.columns:
        df.loc[
            (df["speed"] < MIN_SPEED) | (df["speed"] > MAX_SPEED),
            "speed"
        ] = np.nan

        df["speed"] = (
            df["speed"]
            .interpolate(method="linear")
            .bfill()
            .ffill()
        )

    # Distance cleanup
    if "distance" in df.columns:
        df["distance"] = df["distance"].bfill().ffill()

    df.reset_index(drop=True, inplace=True)
    return df

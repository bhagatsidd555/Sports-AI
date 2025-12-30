import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 🔑 FORCE numeric conversion for safety
    numeric_cols = [
        "distance", "speed", "heart_rate",
        "cadence", "elevation", "temperature",
        "latitude", "longitude"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Timestamp
    if "timestamp" in df.columns:
        df = df.dropna(subset=["timestamp"])
        df = df.drop_duplicates(subset=["timestamp"])

    # Distance
    if "distance" in df.columns:
        df["distance"] = df["distance"].fillna(method="ffill").fillna(0)

    # Speed
    if "speed" in df.columns:
        df.loc[(df["speed"] < 0) | (df["speed"] > 15), "speed"] = np.nan
        df["speed"] = df["speed"].interpolate()

    # Heart rate
    if "heart_rate" in df.columns:
        df.loc[(df["heart_rate"] < 30) | (df["heart_rate"] > 230), "heart_rate"] = np.nan
        df["heart_rate"] = df["heart_rate"].interpolate()

    return df.reset_index(drop=True)

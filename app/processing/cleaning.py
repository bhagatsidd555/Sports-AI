import pandas as pd
import numpy as np

# Physiological & sport-safe limits
MIN_HR = 30
MAX_HR = 220

MIN_SPEED = 0.0
MAX_SPEED = 20.0  # m/s (upper bound for speed skating)

NUMERIC_COLUMNS = [
    "distance",
    "speed",
    "heart_rate",
    "cadence",
    "elevation",
    "temperature",
]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw Garmin data:
    - enforce correct data types
    - sort by timestamp
    - handle missing values
    - remove physiological outliers
    """

    df = df.copy()

    # -----------------------------
    # 1️⃣ Timestamp handling (CRITICAL)
    # -----------------------------
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce"
        )

    # Drop rows without valid timestamp
    df = df.dropna(subset=["timestamp"])

    # -----------------------------
    # 2️⃣ Convert numeric columns safely (🔥 FIX)
    # -----------------------------
    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    # -----------------------------
    # 3️⃣ Sort by time
    # -----------------------------
    df = df.sort_values("timestamp").reset_index(drop=True)

    # -----------------------------
    # 4️⃣ Heart Rate cleaning
    # -----------------------------
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

    # -----------------------------
    # 5️⃣ Speed cleaning
    # -----------------------------
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

    # -----------------------------
    # 6️⃣ Distance cleanup
    # -----------------------------
    if "distance" in df.columns:
        df["distance"] = (
            df["distance"]
            .bfill()
            .ffill()
        )

    # -----------------------------
    # 7️⃣ Final safety
    # -----------------------------
    df = df.dropna().reset_index(drop=True)

    return df

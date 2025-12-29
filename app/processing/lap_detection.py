import pandas as pd
from src.logging import logger

def detect_laps(df: pd.DataFrame, lap_distance: float = 400.0) -> pd.DataFrame:
    """
    Detect laps based on cumulative distance.
    Adds a 'lap' column to indicate lap number.
    Default lap_distance = 400 meters (standard speed skating lap)
    """
    df = df.copy()
    df["lap"] = (df["distance"] // lap_distance + 1).astype(int)
    logger.info(f"Laps detected: {df['lap'].nunique()} total")
    return df

def lap_times(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes lap start and end times.
    Returns a DataFrame with lap number, start_time, end_time, and duration
    """
    lap_df = df.groupby("lap")["timestamp"].agg(["min", "max"]).reset_index()
    lap_df["duration_sec"] = (lap_df["max"] - lap_df["min"]).dt.total_seconds()
    logger.info(f"Computed times for {lap_df.shape[0]} laps")
    return lap_df

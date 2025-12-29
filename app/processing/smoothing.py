import pandas as pd
from scipy.signal import savgol_filter
from src.logging import logger

def smooth_speed(df: pd.DataFrame, window: int = 11, polyorder: int = 2) -> pd.DataFrame:
    """
    Applies Savitzky-Golay filter to smooth speed data
    """
    df = df.copy()
    if len(df) < window:
        logger.warning("Data too short for smoothing, returning original")
        return df
    df["speed_smoothed"] = savgol_filter(df["speed"], window_length=window, polyorder=polyorder)
    logger.info("Speed data smoothed")
    return df

def smooth_heart_rate(df: pd.DataFrame, window: int = 11, polyorder: int = 2) -> pd.DataFrame:
    """
    Applies Savitzky-Golay filter to smooth heart rate data
    """
    df = df.copy()
    if len(df) < window:
        logger.warning("Data too short for smoothing, returning original")
        return df
    df["heart_rate_smoothed"] = savgol_filter(df["heart_rate"], window_length=window, polyorder=polyorder)
    logger.info("Heart rate data smoothed")
    return df

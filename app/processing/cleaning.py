import pandas as pd
from src.logging import logger

def clean_garmin_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw Garmin wearable data.
    - Drops rows with missing timestamps or distance
    - Fills missing heart rate and speed
    - Converts columns to correct numeric types
    """
    # Drop rows with missing critical values
    df = df.dropna(subset=["timestamp", "distance"])
    
    # Fill missing heart rate and speed
    df["heart_rate"] = df["heart_rate"].fillna(method="ffill")
    df["speed"] = df["speed"].fillna(method="ffill")
    
    # Ensure numeric types
    df["distance"] = pd.to_numeric(df["distance"])
    df["speed"] = pd.to_numeric(df["speed"])
    df["heart_rate"] = pd.to_numeric(df["heart_rate"])
    
    logger.info(f"Data cleaned: {df.shape[0]} rows remaining")
    return df

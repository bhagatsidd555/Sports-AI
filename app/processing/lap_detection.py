import pandas as pd


def detect_laps(df: pd.DataFrame, lap_distance: float = 400.0) -> pd.DataFrame:
    df = df.copy()

    if "distance" not in df.columns:
        df["lap"] = 1
        return df

    df["distance"] = pd.to_numeric(df["distance"], errors="coerce")
    df["distance"] = df["distance"].fillna(method="ffill").fillna(0)

    df["lap"] = (df["distance"] // lap_distance).astype(int) + 1
    return df

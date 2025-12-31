import pandas as pd

def smooth_signals(
    df: pd.DataFrame,
    window: int = 5
) -> pd.DataFrame:
    """
    Apply rolling average smoothing
    for heart rate and speed signals.
    """

    df = df.copy()

    if "heart_rate" in df.columns:
        df["heart_rate_smooth"] = (
            df["heart_rate"]
            .rolling(window=window, min_periods=1)
            .mean()
        )

    if "speed" in df.columns:
        df["speed_smooth"] = (
            df["speed"]
            .rolling(window=window, min_periods=1)
            .mean()
        )

    return df

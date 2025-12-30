import pandas as pd


def smooth_signals(df: pd.DataFrame, window: int = 5) -> pd.DataFrame:
    """
    Apply rolling smoothing to noisy signals
    Used for speed, heart rate, cadence
    """

    df = df.copy()

    smooth_cols = ["speed", "heart_rate", "cadence"]

    for col in smooth_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .rolling(window=window, min_periods=1, center=True)
                .mean()
            )

    return df

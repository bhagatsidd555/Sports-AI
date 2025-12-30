import pandas as pd
import numpy as np


def compute_speed_kpis(df: pd.DataFrame) -> dict:
    """
    Speed-based KPIs:
    - Average speed
    - Max speed
    - Speed decay
    - Lap consistency (CV)
    """

    metrics = {}

    if "speed" not in df.columns:
        return metrics

    speed = df["speed"].dropna()

    metrics["avg_speed"] = round(speed.mean(), 3)
    metrics["max_speed"] = round(speed.max(), 3)

    # Speed decay: first 25% vs last 25%
    n = len(speed)
    if n > 10:
        first = speed.iloc[: int(0.25 * n)].mean()
        last = speed.iloc[int(0.75 * n):].mean()
        metrics["speed_decay"] = round((first - last) / first, 3)
    else:
        metrics["speed_decay"] = None

    # Lap consistency (Coefficient of Variation)
    if "lap" in df.columns:
        lap_speed = df.groupby("lap")["speed"].mean()
        metrics["lap_consistency"] = round(
            lap_speed.std() / lap_speed.mean(), 3
        )
    else:
        metrics["lap_consistency"] = None

    return metrics

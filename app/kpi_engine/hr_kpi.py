import pandas as pd
import numpy as np


def compute_hr_kpis(df: pd.DataFrame) -> dict:
    """
    Heart-rate-based KPIs:
    - Average HR
    - HR drift
    - Speed–HR efficiency
    """

    metrics = {}

    if "heart_rate" not in df.columns:
        return metrics

    hr = df["heart_rate"].dropna()
    metrics["avg_hr"] = round(hr.mean(), 1)

    # HR Drift: HR increase over time at similar speed
    n = len(hr)
    if n > 10:
        first = hr.iloc[: int(0.25 * n)].mean()
        last = hr.iloc[int(0.75 * n):].mean()
        metrics["hr_drift"] = round((last - first) / first * 100, 2)
    else:
        metrics["hr_drift"] = None

    # Speed–HR Efficiency
    if "speed" in df.columns:
        metrics["efficiency"] = round(
            df["speed"].mean() / hr.mean(), 4
        )

    return metrics

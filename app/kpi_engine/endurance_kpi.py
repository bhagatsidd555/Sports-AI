import pandas as pd
import numpy as np


def compute_endurance_kpis(df: pd.DataFrame) -> dict:
    """
    Endurance KPIs:
    - Endurance index
    """

    metrics = {}

    if "speed" not in df.columns or "heart_rate" not in df.columns:
        return metrics

    speed = df["speed"].dropna()
    hr = df["heart_rate"].dropna()

    # Endurance Index = speed retention per HR unit
    if len(speed) > 10:
        metrics["endurance_index"] = round(
            speed.mean() / hr.mean(), 4
        )
    else:
        metrics["endurance_index"] = None

    return metrics

import pandas as pd
import numpy as np

def compute_speed_kpis(df: pd.DataFrame) -> dict:
    """
    Speed performance KPIs
    """

    result = {}

    speed_col = "speed_smooth" if "speed_smooth" in df.columns else "speed"

    # Average speed
    result["avg_speed"] = float(df[speed_col].mean())

    # Lap consistency (lower CV = better consistency)
    if "lap_number" in df.columns:
        lap_avg = df.groupby("lap_number")[speed_col].mean()
        result["lap_consistency"] = float(
            1 - (lap_avg.std() / lap_avg.mean())
        )
    else:
        result["lap_consistency"] = None

    # Speed decay (first lap vs last lap)
    if "lap_number" in df.columns:
        first_lap = df[df["lap_number"] == df["lap_number"].min()][speed_col].mean()
        last_lap = df[df["lap_number"] == df["lap_number"].max()][speed_col].mean()
        result["speed_decay"] = float(first_lap - last_lap)
    else:
        result["speed_decay"] = None

    return result

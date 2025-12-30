import pandas as pd
import numpy as np


def compute_load_kpis(df: pd.DataFrame) -> dict:
    """
    Load-based KPIs:
    - Training load
    - ACWR (simplified Lean V1)
    """

    metrics = {}

    if "heart_rate" not in df.columns:
        return metrics

    hr = df["heart_rate"].dropna()

    # Simple TRIMP-style load
    metrics["training_load"] = round(hr.mean() * len(hr) / 1000, 2)

    # ACWR (Lean V1 proxy)
    acute = hr.iloc[-int(0.3 * len(hr)):].mean()
    chronic = hr.mean()

    if chronic > 0:
        metrics["acwr"] = round(acute / chronic, 2)
    else:
        metrics["acwr"] = None

    return metrics

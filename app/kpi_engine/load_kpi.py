import pandas as pd

def compute_load_kpis(df: pd.DataFrame) -> dict:
    """
    Training load & fatigue KPIs
    """

    result = {}

    hr_col = "heart_rate_smooth" if "heart_rate_smooth" in df.columns else "heart_rate"

    # Simple training load proxy
    result["session_load"] = float(df[hr_col].sum())

    # ACWR (simplified Lean V1)
    acute = df[hr_col].tail(len(df)//4).mean()
    chronic = df[hr_col].mean()

    result["acwr"] = float(acute / chronic) if chronic != 0 else None

    return result

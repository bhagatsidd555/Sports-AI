import pandas as pd

def compute_endurance_kpis(df: pd.DataFrame) -> dict:
    """
    Endurance & efficiency KPIs
    """

    result = {}

    speed_col = "speed_smooth" if "speed_smooth" in df.columns else "speed"
    hr_col = "heart_rate_smooth" if "heart_rate_smooth" in df.columns else "heart_rate"

    # Endurance Index (speed stability)
    result["endurance_index"] = float(
        1 - (df[speed_col].std() / df[speed_col].mean())
    )

    # Efficiency ratio
    result["efficiency_ratio"] = float(
        df[speed_col].mean() / df[hr_col].mean()
    )

    return result

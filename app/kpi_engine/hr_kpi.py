import pandas as pd

def compute_hr_kpis(df: pd.DataFrame) -> dict:
    """
    Heart rate & physiological KPIs
    """

    result = {}

    hr_col = "heart_rate_smooth" if "heart_rate_smooth" in df.columns else "heart_rate"
    speed_col = "speed_smooth" if "speed_smooth" in df.columns else "speed"

    result["avg_hr"] = float(df[hr_col].mean())
    result["max_hr"] = float(df[hr_col].max())

    # Heart Rate Drift (second half vs first half)
    mid = len(df) // 2
    hr_first = df.iloc[:mid][hr_col].mean()
    hr_second = df.iloc[mid:][hr_col].mean()
    result["hr_drift"] = float(hr_second - hr_first)

    # Speed–HR efficiency
    result["speed_hr_efficiency"] = float(
        df[speed_col].mean() / df[hr_col].mean()
    )

    return result

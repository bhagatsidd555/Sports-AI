import pandas as pd
from .speed_kpi import compute_speed_kpis
from .hr_kpi import compute_hr_kpis
from .load_kpi import compute_load_kpis
from .endurance_kpi import compute_endurance_kpis

def compute_all_kpis(df: pd.DataFrame) -> dict:
    """
    Aggregate all KPIs into a single structure
    """

    return {
        "speed": compute_speed_kpis(df),
        "heart_rate": compute_hr_kpis(df),
        "load": compute_load_kpis(df),
        "endurance": compute_endurance_kpis(df),
    }

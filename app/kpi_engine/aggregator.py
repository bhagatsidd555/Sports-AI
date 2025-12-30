from typing import Dict
import pandas as pd

from .speed_kpi import compute_speed_kpis
from .hr_kpi import compute_hr_kpis
from .load_kpi import compute_load_kpis
from .endurance_kpi import compute_endurance_kpis


def aggregate_kpis(df: pd.DataFrame) -> Dict:
    """
    Aggregate all KPI groups into one metrics dictionary
    """

    metrics = {}

    metrics.update(compute_speed_kpis(df))
    metrics.update(compute_hr_kpis(df))
    metrics.update(compute_load_kpis(df))
    metrics.update(compute_endurance_kpis(df))

    return metrics

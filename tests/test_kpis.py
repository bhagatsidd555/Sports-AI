import pandas as pd
import numpy as np

from app.kpi_engine.baseline import lap_consistency, speed_decay
from app.kpi_engine.physiological import heart_rate_drift
from app.kpi_engine.efficiency import speed_hr_efficiency
from app.kpi_engine.fatigue import endurance_index


def sample_dataframe():
    return pd.DataFrame({
        "timestamp": np.arange(10),
        "distance": np.linspace(0, 100, 10),
        "speed": np.linspace(6.0, 5.0, 10),
        "heart_rate": np.linspace(100, 120, 10)
    })


def test_lap_consistency():
    df = sample_dataframe()
    df["lap"] = 0
    value = lap_consistency(df)
    assert value >= 0


def test_speed_decay():
    df = sample_dataframe()
    decay = speed_decay(df)
    assert decay > 0


def test_heart_rate_drift():
    df = sample_dataframe()
    drift = heart_rate_drift(df)
    assert drift > 0


def test_speed_hr_efficiency():
    df = sample_dataframe()
    eff = speed_hr_efficiency(df)
    assert eff > 0


def test_endurance_index():
    df = sample_dataframe()
    end = endurance_index(df)
    assert end > 0

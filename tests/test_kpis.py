import pandas as pd
from app.kpi_engine.aggregator import aggregate_kpis


def sample_df():
    return pd.DataFrame({
        "timestamp": pd.date_range("2025-01-01", periods=10, freq="S"),
        "distance": [i * 100 for i in range(10)],
        "speed": [6.0, 6.1, 6.2, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6, 5.5],
        "heart_rate": [140, 142, 145, 147, 150, 152, 155, 158, 160, 162],
        "lap": [1,1,1,1,2,2,2,2,3,3]
    })


def test_kpi_aggregation():
    df = sample_df()
    metrics = aggregate_kpis(df)

    assert "avg_speed" in metrics
    assert "max_speed" in metrics
    assert "speed_decay" in metrics
    assert "avg_hr" in metrics
    assert "hr_drift" in metrics
    assert "efficiency" in metrics
    assert "training_load" in metrics
    assert "acwr" in metrics
    assert "endurance_index" in metrics

    assert metrics["avg_speed"] > 0
    assert metrics["max_speed"] >= metrics["avg_speed"]

from scoring.readiness_score import compute_race_readiness_score


def sample_kpis():
    return {
        "lap_consistency": 0.04,
        "speed_decay": 0.05,
        "heart_rate_drift": 0.08,
        "speed_hr_efficiency": 0.35,
        "endurance_index": 0.40,
        "acwr": 1.0,
        "trajectory_smoothness": 0.04,
        "corner_speed_loss": 0.03
    }


def test_race_readiness_score_range():
    result = compute_race_readiness_score(sample_kpis())
    score = result["race_readiness_score"]

    assert 0 <= score <= 100


def test_readiness_interpretation_exists():
    result = compute_race_readiness_score(sample_kpis())
    assert "interpretation" in result


def test_normalized_scores_exist():
    result = compute_race_readiness_score(sample_kpis())
    assert "normalized_scores" in result

"""
Race Readiness Scoring Engine
Combines all KPIs into a single composite score (0–100)
"""

from scoring.weights import KPI_WEIGHTS
from scoring.thresholds import KPI_THRESHOLDS


def normalize_lower_better(value, excellent, poor):
    """
    Lower value = better performance
    """
    if value <= excellent:
        return 1.0
    if value >= poor:
        return 0.0
    return 1 - (value - excellent) / (poor - excellent)


def normalize_higher_better(value, poor, excellent):
    """
    Higher value = better performance
    """
    if value >= excellent:
        return 1.0
    if value <= poor:
        return 0.0
    return (value - poor) / (excellent - poor)


def normalize_acwr(acwr):
    """
    Optimal workload zone: 0.8 – 1.3
    """
    if 0.8 <= acwr <= 1.3:
        return 1.0
    if acwr < 0.8:
        return acwr / 0.8
    return max(0.0, 1 - (acwr - 1.3))


def compute_race_readiness_score(kpis: dict) -> dict:
    """
    Input:
        kpis: dict of computed KPIs

    Output:
        readiness score + breakdown
    """

    scores = {}

    # Lap consistency
    scores["lap_consistency"] = normalize_lower_better(
        kpis["lap_consistency"],
        KPI_THRESHOLDS["lap_consistency"]["excellent"],
        KPI_THRESHOLDS["lap_consistency"]["poor"]
    )

    # Speed decay
    scores["speed_decay"] = normalize_lower_better(
        kpis["speed_decay"],
        KPI_THRESHOLDS["speed_decay"]["excellent"],
        KPI_THRESHOLDS["speed_decay"]["poor"]
    )

    # HR drift
    scores["heart_rate_drift"] = normalize_lower_better(
        kpis["heart_rate_drift"],
        KPI_THRESHOLDS["heart_rate_drift"]["excellent"],
        KPI_THRESHOLDS["heart_rate_drift"]["poor"]
    )

    # Speed-HR efficiency
    scores["speed_hr_efficiency"] = normalize_higher_better(
        kpis["speed_hr_efficiency"],
        KPI_THRESHOLDS["speed_hr_efficiency"]["poor"],
        KPI_THRESHOLDS["speed_hr_efficiency"]["excellent"]
    )

    # Endurance
    scores["endurance_index"] = normalize_higher_better(
        kpis["endurance_index"],
        KPI_THRESHOLDS["endurance_index"]["poor"],
        KPI_THRESHOLDS["endurance_index"]["excellent"]
    )

    # ACWR
    scores["acwr"] = normalize_acwr(kpis["acwr"])

    # Trajectory smoothness
    scores["trajectory_smoothness"] = normalize_lower_better(
        kpis["trajectory_smoothness"],
        KPI_THRESHOLDS["trajectory_smoothness"]["excellent"],
        KPI_THRESHOLDS["trajectory_smoothness"]["poor"]
    )

    # Corner speed loss
    scores["corner_speed_loss"] = normalize_lower_better(
        kpis["corner_speed_loss"],
        KPI_THRESHOLDS["corner_speed_loss"]["excellent"],
        KPI_THRESHOLDS["corner_speed_loss"]["poor"]
    )

    # ---- FINAL COMPOSITE SCORE ----
    final_score = 0.0
    for kpi, weight in KPI_WEIGHTS.items():
        final_score += scores[kpi] * weight

    final_score = round(final_score * 100, 2)

    return {
        "race_readiness_score": final_score,
        "normalized_scores": scores,
        "interpretation": interpret_score(final_score)
    }


def interpret_score(score: float) -> str:
    """
    Coach-friendly explanation
    """
    if score >= 85:
        return "Peak race-ready condition"
    elif score >= 70:
        return "Good condition – minor tuning needed"
    elif score >= 55:
        return "Moderate readiness – monitor fatigue"
    else:
        return "Low readiness – recovery recommended"

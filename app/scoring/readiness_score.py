from app.scoring.thresholds import THRESHOLDS
from app.scoring.weights import WEIGHTS

def _score_metric(value, good, moderate, reverse=False):
    """
    Convert raw KPI into 0–1 score
    reverse=True for metrics where lower is better
    """
    if value is None:
        return 0.5

    if reverse:
        if value <= good:
            return 1.0
        elif value <= moderate:
            return 0.7
        else:
            return 0.3
    else:
        if value >= good:
            return 1.0
        elif value >= moderate:
            return 0.7
        else:
            return 0.3


def compute_race_readiness(kpis: dict) -> dict:
    """
    Compute final race readiness score (0–100)
    """

    # --- Speed score ---
    speed_score = (
        _score_metric(
            kpis["speed"]["lap_consistency"],
            THRESHOLDS["lap_consistency"]["good"],
            THRESHOLDS["lap_consistency"]["moderate"]
        ) +
        _score_metric(
            kpis["speed"]["speed_decay"],
            THRESHOLDS["speed_decay"]["good"],
            THRESHOLDS["speed_decay"]["moderate"],
            reverse=True
        )
    ) / 2

    # --- Heart score ---
    heart_score = _score_metric(
        kpis["heart_rate"]["hr_drift"],
        THRESHOLDS["hr_drift"]["good"],
        THRESHOLDS["hr_drift"]["moderate"],
        reverse=True
    )

    # --- Load score ---
    load_score = _score_metric(
        kpis["load"]["acwr"],
        THRESHOLDS["acwr"]["good"],
        THRESHOLDS["acwr"]["moderate"],
        reverse=True
    )

    # --- Endurance score ---
    endurance_score = _score_metric(
        kpis["endurance"]["endurance_index"],
        THRESHOLDS["endurance_index"]["good"],
        THRESHOLDS["endurance_index"]["moderate"]
    )

    # --- Final weighted score ---
    readiness = (
        speed_score * WEIGHTS["speed"] +
        heart_score * WEIGHTS["heart"] +
        load_score * WEIGHTS["load"] +
        endurance_score * WEIGHTS["endurance"]
    ) * 100

    # --- Coach-friendly label ---
    if readiness >= 80:
        status = "High – Race Ready"
    elif readiness >= 60:
        status = "Moderate – Minor adjustments advised"
    else:
        status = "Low – Recovery recommended"

    return {
        "race_readiness_score": round(readiness, 1),
        "readiness_status": status,
        "component_scores": {
            "speed": round(speed_score * 100, 1),
            "heart": round(heart_score * 100, 1),
            "load": round(load_score * 100, 1),
            "endurance": round(endurance_score * 100, 1),
        }
    }

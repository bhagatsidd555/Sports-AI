from typing import Dict
from .thresholds import THRESHOLDS
from .weights import WEIGHTS


def _score_linear(value, excellent, poor, inverse=False):
    """
    Linear scoring helper.
    Returns value between 0 and 1.
    """
    if value is None:
        return 0.5  # neutral

    if inverse:
        if value <= excellent:
            return 1.0
        if value >= poor:
            return 0.0
        return 1 - (value - excellent) / (poor - excellent)
    else:
        if value >= excellent:
            return 1.0
        if value <= poor:
            return 0.0
        return (value - poor) / (excellent - poor)


def compute_readiness_score(metrics: Dict) -> Dict:
    """
    Compute overall Race Readiness Score (0–100)
    Returns score + component breakdown
    """

    components = {}

    # ---------------------------
    # Speed Decay (lower is better)
    # ---------------------------
    sd = metrics.get("speed_decay")
    components["speed_decay"] = _score_linear(
        sd,
        THRESHOLDS["speed_decay"]["excellent"],
        THRESHOLDS["speed_decay"]["poor"],
        inverse=True
    )

    # ---------------------------
    # HR Drift (lower is better)
    # ---------------------------
    hr_drift = metrics.get("hr_drift")
    components["hr_drift"] = _score_linear(
        hr_drift,
        THRESHOLDS["hr_drift"]["excellent"],
        THRESHOLDS["hr_drift"]["poor"],
        inverse=True
    )

    # ---------------------------
    # Speed–HR Efficiency (higher is better)
    # ---------------------------
    eff = metrics.get("efficiency")
    components["efficiency"] = _score_linear(
        eff,
        THRESHOLDS["efficiency"]["excellent"],
        THRESHOLDS["efficiency"]["poor"]
    )

    # ---------------------------
    # ACWR (penalty outside safe zone)
    # ---------------------------
    acwr = metrics.get("acwr")
    if acwr is None:
        components["acwr"] = 0.5
    elif THRESHOLDS["acwr"]["low_risk_min"] <= acwr <= THRESHOLDS["acwr"]["low_risk_max"]:
        components["acwr"] = 1.0
    else:
        components["acwr"] = 0.3

    # ---------------------------
    # Endurance Index
    # ---------------------------
    ei = metrics.get("endurance_index")
    components["endurance_index"] = _score_linear(
        ei,
        THRESHOLDS["endurance_index"]["excellent"],
        THRESHOLDS["endurance_index"]["poor"]
    )

    # ---------------------------
    # Lap Consistency (lower CV is better)
    # ---------------------------
    lap_cv = metrics.get("lap_consistency")
    if lap_cv is None:
        components["lap_consistency"] = 0.5
    else:
        components["lap_consistency"] = max(0.0, 1 - lap_cv)

    # ---------------------------
    # Weighted aggregation
    # ---------------------------
    readiness_score = 0.0
    for key, weight in WEIGHTS.items():
        readiness_score += components.get(key, 0) * weight

    readiness_score = round(readiness_score * 100, 1)

    return {
        "readiness_score": readiness_score,
        "components": components
    }

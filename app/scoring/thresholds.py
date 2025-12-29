"""
Thresholds define expected physiological & performance ranges
Used for normalization and flagging risk
"""

KPI_THRESHOLDS = {

    # Lower is better
    "lap_consistency": {
        "excellent": 0.03,
        "good": 0.06,
        "poor": 0.10
    },

    "speed_decay": {
        "excellent": 0.03,
        "good": 0.06,
        "poor": 0.10
    },

    "heart_rate_drift": {
        "excellent": 0.05,
        "good": 0.10,
        "poor": 0.15
    },

    # Higher is better
    "speed_hr_efficiency": {
        "poor": 0.20,
        "good": 0.30,
        "excellent": 0.40
    },

    "endurance_index": {
        "poor": 0.25,
        "good": 0.35,
        "excellent": 0.45
    },

    # Workload balance
    "acwr": {
        "low_risk_min": 0.8,
        "low_risk_max": 1.3
    },

    # Technical
    "trajectory_smoothness": {
        "excellent": 0.02,
        "good": 0.05,
        "poor": 0.08
    },

    "corner_speed_loss": {
        "excellent": 0.02,
        "good": 0.05,
        "poor": 0.08
    }
}

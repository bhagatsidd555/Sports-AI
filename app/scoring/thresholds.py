"""
Threshold values for performance & fatigue metrics
All values are Lean V1 safe defaults (can be tuned per athlete later)
"""

THRESHOLDS = {
    # Speed decay (fraction)
    "speed_decay": {
        "excellent": 0.05,
        "acceptable": 0.10,
        "poor": 0.20
    },

    # Heart rate drift (%)
    "hr_drift": {
        "excellent": 5,
        "acceptable": 10,
        "poor": 20
    },

    # Speed–HR efficiency (higher is better)
    "efficiency": {
        "excellent": 0.035,
        "acceptable": 0.025,
        "poor": 0.015
    },

    # ACWR (load balance)
    "acwr": {
        "low_risk_min": 0.8,
        "low_risk_max": 1.3
    },

    # Endurance index
    "endurance_index": {
        "excellent": 0.035,
        "acceptable": 0.025,
        "poor": 0.015
    }
}

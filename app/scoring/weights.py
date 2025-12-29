"""
Weights for composite race readiness score
Sum of all weights MUST be 1.0
"""

KPI_WEIGHTS = {
    # Consistency & pacing
    "lap_consistency": 0.15,
    "speed_decay": 0.15,

    # Physiological control
    "heart_rate_drift": 0.15,
    "speed_hr_efficiency": 0.15,

    # Fatigue & workload
    "acwr": 0.15,
    "endurance_index": 0.10,

    # Technical efficiency
    "trajectory_smoothness": 0.10,
    "corner_speed_loss": 0.05
}

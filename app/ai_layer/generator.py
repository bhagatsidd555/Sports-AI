from typing import Dict
from .prompts import SYSTEM_PROMPT, INSIGHT_PROMPT


def generate_insight(metrics: Dict) -> str:
    """
    Convert computed KPI metrics into coach-friendly insight text.
    This function is LLM-ready (OpenAI / local LLM / future models).
    """

    # Defensive defaults
    def val(key, default="N/A"):
        return metrics.get(key, default)

    prompt = INSIGHT_PROMPT.format(
        avg_speed=val("avg_speed"),
        max_speed=val("max_speed"),
        lap_consistency=val("lap_consistency"),
        avg_hr=val("avg_hr"),
        hr_drift=val("hr_drift"),
        efficiency=val("efficiency"),
        training_load=val("training_load"),
        acwr=val("acwr"),
        endurance_index=val("endurance_index"),
        trajectory_smoothness=val("trajectory_smoothness"),
        corner_speed_loss=val("corner_speed_loss"),
        readiness_score=val("readiness_score"),
    )

    # 🔹 For now: rule-based explanation (Lean V1)
    # 🔹 Future: plug into GPT / LLM

    readiness = val("readiness_score", 0)

    if readiness >= 80:
        status = "Athlete is in peak competitive condition."
    elif readiness >= 60:
        status = "Athlete shows solid readiness but minor fatigue signs."
    elif readiness >= 40:
        status = "Moderate fatigue detected. Training load should be monitored."
    else:
        status = "Low readiness. Recovery and load reduction are recommended."

    insight = f"""
PERFORMANCE INSIGHT REPORT
--------------------------
{status}

Key Observations:
- Speed and heart rate relationship indicates efficiency level: {val("efficiency")}
- Heart rate drift suggests cardiovascular fatigue trend.
- Lap consistency reflects pacing discipline.

Coaching Actions:
- Adjust intensity based on readiness score.
- Focus on technical efficiency if corner speed loss is elevated.
- Monitor ACWR to avoid overload.

Race Outlook:
- Readiness Score: {readiness}/100
"""

    return insight.strip()

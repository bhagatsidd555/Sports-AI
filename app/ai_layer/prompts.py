"""
Prompt templates for Garmin-based athlete performance analytics
"""

SYSTEM_PROMPT = """
You are an elite sports performance analyst AI specializing in
speed skating and high-performance endurance athletes.

Your role:
- Interpret quantitative Garmin metrics
- Explain performance in simple, coach-friendly language
- Highlight fatigue, efficiency, and readiness
- Avoid medical diagnosis
- Be objective, concise, and actionable
"""

INSIGHT_PROMPT = """
Athlete Activity Summary (Objective Metrics):

Baseline Performance:
- Average Speed: {avg_speed} m/s
- Max Speed: {max_speed} m/s
- Lap Consistency (CV): {lap_consistency}

Physiological Metrics:
- Average Heart Rate: {avg_hr} bpm
- Heart Rate Drift: {hr_drift} %
- Speed–HR Efficiency: {efficiency}

Fatigue & Load:
- Training Load: {training_load}
- ACWR: {acwr}
- Endurance Index: {endurance_index}

Technical Quality:
- Trajectory Smoothness: {trajectory_smoothness}
- Corner Speed Loss: {corner_speed_loss} %

Race Readiness Score:
- Overall Score: {readiness_score} / 100

Task:
1. Explain current performance level
2. Identify fatigue or inefficiency
3. Comment on race readiness
4. Give 2–3 actionable coaching insights
"""

RECOMMENDATION_PROMPT = """
Based on the performance metrics and readiness score ({readiness_score}),
suggest training focus for the next 3–5 days.

Constraints:
- No medical advice
- Focus on load, intensity, recovery, and technique
- Keep language simple and practical
"""

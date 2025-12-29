from pydantic import BaseModel
from typing import Optional, Dict

# Individual KPI model
class KPIs(BaseModel):
    lap_consistency: float
    speed_decay: float
    speed_hr_efficiency: float
    training_load: float
    hr_drift: float
    endurance_index: float
    trajectory_smoothness: Optional[float] = None
    corner_speed_loss: Optional[float] = None

# Race readiness model
class RaceReadinessResponse(BaseModel):
    athlete_id: str
    session_date: str
    kpis: KPIs
    race_readiness_score: float

# Full analytics response including optional visualizations
class AnalyticsResponse(BaseModel):
    athlete_id: str
    session_date: str
    kpis: KPIs
    race_readiness_score: float
    trends: Optional[Dict[str, float]] = None  # e.g., training load trend, speed decay trend
    feedback: Optional[str] = None  # Coach-friendly summary or automated insights

"""
Scoring module
Responsible for converting raw KPIs into normalized scores
and computing final composite readiness score.
"""

from .readiness_score import compute_race_readiness_score
from .thresholds import KPI_THRESHOLDS
from .weights import KPI_WEIGHTS

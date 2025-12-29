from .speed_kpi import lap_consistency, speed_decay, corner_speed_loss
from .hr_kpi import hr_drift, speed_hr_efficiency
from .endurance_kpi import endurance_index
from .load_kpi import compute_acwr, training_load_trend
from utils.logging_util import logger

def compute_race_readiness(df):
    """
    Aggregate all KPIs into a single Race Readiness Score (0-100)
    """
    scores = {}

    scores['lap_consistency'] = max(0, 100 - lap_consistency(df))  # lower std = higher score
    scores['speed_decay'] = max(0, 100 - speed_decay(df))          # lower decay = higher score
    scores['hr_drift'] = max(0, 100 - hr_drift(df))                # lower drift = higher score
    scores['speed_hr_efficiency'] = speed_hr_efficiency(df) * 100  # normalized
    scores['endurance_index'] = endurance_index(df) * 10           # normalized
    scores['acwr'] = max(0, 100 - abs(1 - compute_acwr(df)) * 100) # ideal ACWR ~1
    scores['training_load_trend'] = max(0, 100 - abs(training_load_trend(df))*100)
    scores['corner_speed_loss'] = max(0, 100 - corner_speed_loss(df))

    race_readiness_score = sum(scores.values()) / len(scores)
    logger.info(f"Overall Race Readiness Score: {race_readiness_score:.2f}/100")

    return race_readiness_score, scores

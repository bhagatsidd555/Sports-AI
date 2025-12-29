# Expose KPI modules for easy import
from .aggregator import compute_race_readiness
from .endurance_kpi import endurance_index
from .hr_kpi import hr_drift, speed_hr_efficiency
from .load_kpi import compute_acwr, training_load_trend
from .speed_kpi import lap_consistency, speed_decay, corner_speed_loss

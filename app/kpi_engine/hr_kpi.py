import numpy as np
from utils.logging_util import logger

def hr_drift(df):
    hr = df['heart_rate'].values
    drift = hr[-1] - hr[0]
    logger.info(f"Heart rate drift: {drift:.2f} bpm")
    return drift

def speed_hr_efficiency(df):
    speed = df['speed'].values
    hr = df['heart_rate'].values
    efficiency = np.mean(speed / hr)
    logger.info(f"Speed-HR efficiency: {efficiency:.4f}")
    return efficiency

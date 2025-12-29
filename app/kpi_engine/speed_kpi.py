import numpy as np
from utils.logging_util import logger

def lap_consistency(df):
    laps = df['lap_time'].values
    consistency = np.std(laps)
    logger.info(f"Lap consistency: {consistency:.2f} s")
    return consistency

def speed_decay(df):
    speed = df['speed'].values
    decay = speed[0] - speed[-1]
    logger.info(f"Speed decay: {decay:.2f} km/h")
    return decay

def corner_speed_loss(df):
    if 'corner_speed' in df.columns:
        loss = np.max(df['corner_speed']) - np.min(df['corner_speed'])
        logger.info(f"Corner speed loss: {loss:.2f} km/h")
        return loss
    logger.warning("Corner speed data not available")
    return 0

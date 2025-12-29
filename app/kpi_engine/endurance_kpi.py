from utils.logging_util import logger

def endurance_index(df):
    try:
        endurance = df['speed'].mean() / df['heart_rate'].mean()
        logger.info(f"Endurance index: {endurance:.4f}")
        return endurance
    except Exception as e:
        logger.error(f"Error calculating endurance index: {e}")
        return None

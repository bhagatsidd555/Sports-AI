from utils.logging_util import logger

def compute_acwr(df, short_window=7, long_window=28):
    """
    Acute-Chronic Workload Ratio
    """
    load = df['training_load'].rolling(1).sum()  # simplified
    acwr_series = load.rolling(short_window).mean() / load.rolling(long_window).mean()
    acwr_value = acwr_series.iloc[-1] if not acwr_series.empty else 0
    logger.info(f"ACWR: {acwr_value:.4f}")
    return acwr_value

def training_load_trend(df):
    trend = df['training_load'].pct_change().fillna(0).mean()
    logger.info(f"Training load trend: {trend:.4f}")
    return trend

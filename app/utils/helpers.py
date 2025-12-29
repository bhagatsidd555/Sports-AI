import numpy as np
import pandas as pd
from .constants import EPSILON


def safe_divide(a, b):
    """Safe division to avoid ZeroDivisionError"""
    return a / (b + EPSILON)


def rolling_mean(series, window=5):
    """Rolling mean for smoothing wearable signals"""
    return series.rolling(window=window, min_periods=1).mean()


def percentage_change(start, end):
    """Percentage change used for speed decay & HR drift"""
    return safe_divide(end - start, start)


def normalize(value, min_val, max_val):
    """Normalize value to 0–1 range"""
    return (value - min_val) / (max_val - min_val + EPSILON)


def exponential_moving_average(series, alpha=0.3):
    """EMA smoothing for fatigue & training load"""
    ema = []
    prev = series.iloc[0]

    for val in series:
        current = alpha * val + (1 - alpha) * prev
        ema.append(current)
        prev = current

    return pd.Series(ema, index=series.index)

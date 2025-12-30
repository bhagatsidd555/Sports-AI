import pandas as pd
from typing import Optional


def safe_divide(numerator: float, denominator: float) -> Optional[float]:
    """
    Safe division utility
    """
    if denominator == 0 or denominator is None:
        return None
    return numerator / denominator


def percentage_change(first: float, last: float) -> Optional[float]:
    """
    Percentage change utility
    """
    if first is None or first == 0:
        return None
    return (last - first) / first * 100


def ensure_column(df: pd.DataFrame, column: str) -> bool:
    """
    Check if column exists and is not fully null
    """
    return column in df.columns and not df[column].isnull().all()

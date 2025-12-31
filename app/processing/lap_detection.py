import pandas as pd

DEFAULT_LAP_DISTANCE = 400.0  # meters (speed skating standard)

def detect_laps(
    df: pd.DataFrame,
    lap_distance: float = DEFAULT_LAP_DISTANCE
) -> pd.DataFrame:
    """
    Detect laps using cumulative distance.
    Adds:
    - lap_number
    - lap_distance
    - lap_time (seconds)
    """

    df = df.copy()

    if "distance" not in df.columns or "timestamp" not in df.columns:
        df["lap_number"] = 1
        return df

    # Lap number
    df["lap_number"] = (df["distance"] // lap_distance).astype(int) + 1

    # Distance inside lap
    df["lap_distance"] = df["distance"] % lap_distance

    # Lap time calculation
    lap_times = []
    for lap, lap_df in df.groupby("lap_number"):
        start = lap_df["timestamp"].iloc[0]
        end = lap_df["timestamp"].iloc[-1]
        lap_time = (end - start).total_seconds()
        lap_times.append((lap, lap_time))

    lap_time_df = pd.DataFrame(
        lap_times,
        columns=["lap_number", "lap_time"]
    )

    df = df.merge(lap_time_df, on="lap_number", how="left")
    return df

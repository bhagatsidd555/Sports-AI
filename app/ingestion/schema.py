import pandas as pd


class GarminSchema:
    """
    Schema validation for Garmin activity data
    Ensures required columns and basic data sanity
    """

    # Minimum required columns for Lean V1 analytics
    REQUIRED_COLUMNS = {
        "timestamp",
        "distance"
    }

    # Optional but expected columns
    OPTIONAL_COLUMNS = {
        "speed",
        "heart_rate",
        "cadence",
        "elevation",
        "temperature",
        "latitude",
        "longitude"
    }

    @classmethod
    def validate(cls, df: pd.DataFrame) -> None:
        """
        Validate dataframe structure and critical columns
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input data must be a Pandas DataFrame")

        missing = cls.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        # Timestamp sanity check
        if "timestamp" in df.columns:
            if df["timestamp"].isnull().all():
                raise ValueError("Timestamp column contains only null values")

        # Distance sanity check
        if "distance" in df.columns:
            if (df["distance"] < 0).any():
                raise ValueError("Distance contains negative values")

        # Heart rate sanity check
        if "heart_rate" in df.columns:
            if df["heart_rate"].dropna().empty:
                raise ValueError("Heart rate column is empty")

        # Latitude / Longitude consistency
        if "latitude" in df.columns and "longitude" in df.columns:
            if df["latitude"].isnull().all() or df["longitude"].isnull().all():
                raise ValueError("GPS trajectory data is invalid")

        # Passed validation
        return

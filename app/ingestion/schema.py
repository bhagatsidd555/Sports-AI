class GarminSchema:
    """
    Define required and optional columns based on project objective
    """

    REQUIRED_COLUMNS = [
        "timestamp",
        "distance",
        "speed",
        "heart_rate",
        "lap_time",
        "training_load",
        "cadence",
        "elevation",
        "temperature",
        "gps_lat",
        "gps_lon"
    ]

    OPTIONAL_COLUMNS = {
        "EPOC": 0,
        "laps": 0,
        "splits": None,
        "corner_speed": 0
    }

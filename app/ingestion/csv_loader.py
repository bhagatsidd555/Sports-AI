import pandas as pd
from .schema import GarminSchema


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load Garmin CSV file and return DataFrame
    """
    df = pd.read_csv(file_path)

    # Optional: schema validation hook
    # GarminSchema.validate(df)

    return df

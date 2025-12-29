from fitparse import FitFile
import pandas as pd
from .schema import GarminSchema


def load_fit(file_path: str) -> pd.DataFrame:
    """
    Load Garmin FIT file and return a pandas DataFrame
    """

    fitfile = FitFile(file_path)
    records = []

    for record in fitfile.get_messages("record"):
        row = {}
        for field in record:
            row[field.name] = field.value
        records.append(row)

    df = pd.DataFrame(records)

    # Optional: schema validation hook
    # GarminSchema.validate(df)

    return df

from fitparse import FitFile
import pandas as pd
import io
from fastapi import UploadFile
from .schema import GarminSchema


async def load_fit(file: UploadFile) -> pd.DataFrame:
    """
    Load Garmin FIT file from FastAPI UploadFile
    Returns validated Pandas DataFrame
    """

    try:
        contents: bytes = await file.read()
        fit_buffer = io.BytesIO(contents)

        fitfile = FitFile(fit_buffer)

        records = []

        for record in fitfile.get_messages("record"):
            row = {}
            for field in record:
                row[field.name] = field.value
            records.append(row)

        if not records:
            raise ValueError("No activity records found in FIT file")

        df = pd.DataFrame(records)

        # Standardize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # Optional schema validation
        GarminSchema.validate(df)

        return df

    except Exception as e:
        raise RuntimeError(f"FIT loading failed: {str(e)}")

import pandas as pd
import io
from fastapi import UploadFile
from .schema import GarminSchema


async def load_csv(file: UploadFile) -> pd.DataFrame:
    """
    Load Garmin CSV file from FastAPI UploadFile
    Returns validated Pandas DataFrame
    """

    try:
        contents: bytes = await file.read()

        buffer = io.StringIO(contents.decode("utf-8"))
        df = pd.read_csv(buffer)

        if df.empty:
            raise ValueError("CSV file is empty")

        # Standardize column names
        df.columns = [c.strip().lower() for c in df.columns]

        # Optional schema validation
        GarminSchema.validate(df)

        return df

    except UnicodeDecodeError:
        raise ValueError("CSV encoding must be UTF-8")

    except Exception as e:
        raise RuntimeError(f"CSV loading failed: {str(e)}")

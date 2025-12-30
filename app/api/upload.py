from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.ingestion.csv_loader import load_csv
from app.ingestion.fit_loader import load_fit
from app.processing import clean_data, smooth_signals, detect_laps

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_activity(file: UploadFile = File(...)):
    """
    Upload Garmin CSV or FIT file and preprocess activity data
    """

    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file uploaded")

        # 1️⃣ Load raw data
        if file.filename.lower().endswith(".csv"):
            df = await load_csv(file)

        elif file.filename.lower().endswith(".fit"):
            df = await load_fit(file)

        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        if not isinstance(df, pd.DataFrame) or df.empty:
            raise RuntimeError("Parsed data is empty or invalid")

        # 2️⃣ Preprocessing pipeline
        df = clean_data(df)
        df = smooth_signals(df)
        df = detect_laps(df)

        return {
            "status": "success",
            "filename": file.filename,
            "rows": int(df.shape[0]),
            "columns": list(df.columns),
            "message": "File uploaded and preprocessed successfully"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Upload failed: {str(e)}"
        )

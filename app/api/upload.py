from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

import app.core.data_store as data_store   # 🔥 IMPORTANT

from app.ingestion.csv_loader import load_csv
from app.ingestion.fit_loader import load_fit
from app.processing.cleaning import clean_data
from app.processing.smoothing import smooth_signals
from app.processing.lap_detection import detect_laps

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

        if not isinstance(df, pd.DataFrame):
            raise HTTPException(status_code=500, detail="Invalid data format")

        # 2️⃣ Preprocessing pipeline
        df = clean_data(df)
        df = smooth_signals(df)
        df = detect_laps(df)

        # 🔥🔥🔥 3️⃣ STORE DATA GLOBALLY (THIS FIXES READINESS)
        data_store.latest_activity_df = df

        return {
            "status": "success",
            "records": len(df),
            "message": "File uploaded and preprocessed successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

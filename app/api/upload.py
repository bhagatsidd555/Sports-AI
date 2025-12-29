from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ingestion.csv_loader import load_csv
from app.ingestion.fit_loader import load_fit

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload CSV or FIT file
    """
    try:
        validate_file_type(file.filename)

        if file.filename.endswith(".csv"):
            data = await load_csv(file)
        elif file.filename.endswith(".fit"):
            data = await load_fit(file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        return {
            "status": "success",
            "filename": file.filename,
            "records": len(data),
            "message": "File uploaded and parsed successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

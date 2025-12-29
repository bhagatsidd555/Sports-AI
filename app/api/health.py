from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {
        "status": "OK",
        "service": "Sports AI Backend",
        "message": "Server is running successfully"
    }

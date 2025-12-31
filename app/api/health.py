from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
def health_check():
    """
    Health check endpoint for monitoring and uptime validation
    """
    return {
        "status": "ok",
        "service": "Sports-AI Backend",
        "message": "Application is running ok"
    }

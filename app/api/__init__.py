from .upload import router as upload_router
from .chat import router as chat_router
from .health import router as health_router
from .readiness import router as readiness_router

__all__ = [
    "upload_router",
    "chat_router",
    "health_router",
    "readiness_router",
]

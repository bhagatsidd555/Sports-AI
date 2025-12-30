from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logging import get_logger

from app.api import (
    upload_router,
    chat_router,
    health_router
)

logger = get_logger("main")

# -----------------------------
# FastAPI App Initialization
# -----------------------------
app = FastAPI(
    title=settings.APP_NAME,
    description="Garmin-based Athlete Performance Analytics Platform",
    version="1.0.0"
)

# -----------------------------
# CORS Middleware
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routers
# -----------------------------
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)

# -----------------------------
# Startup / Shutdown Events
# -----------------------------
@app.on_event("startup")
def on_startup():
    logger.info("🚀 Sports-AI Backend started successfully")
    logger.info(f"Environment: {settings.ENV}")


@app.on_event("shutdown")
def on_shutdown():
    logger.info("🛑 Sports-AI Backend shutting down")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logging import get_logger

# 🔥 ROUTER IMPORTS (SAFE & GUARANTEED)
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api import readiness   # module import

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
    allow_origins=["*"],
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
app.include_router(readiness.router)  # ✅ CORRECT FIX

# -----------------------------
# Startup / Shutdown Events
# -----------------------------
@app.on_event("startup")
def on_startup():
    logger.info("Sports-AI Backend started successfully")
    logger.info(f"Environment: {settings.ENV}")


@app.on_event("shutdown")
def on_shutdown():
    logger.info("Sports-AI Backend shutting down")
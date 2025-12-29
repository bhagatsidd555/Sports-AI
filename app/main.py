from fastapi import FastAPI
from app.api import upload, chat, health
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="Sports AI Backend",
    version="1.0.0"
)

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(health.router, prefix="/health", tags=["Health"])

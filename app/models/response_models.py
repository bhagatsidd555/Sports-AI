from pydantic import BaseModel
from typing import List, Dict, Optional


class UploadResponse(BaseModel):
    """
    Response model for file upload endpoint
    """
    status: str
    filename: str
    rows: int
    columns: List[str]
    message: str


class KPIResponse(BaseModel):
    """
    Response model for KPI computation
    """
    status: str
    metrics: Dict[str, Optional[float]]


class ChatResponse(BaseModel):
    """
    Response model for chat / AI insight endpoint
    """
    status: str
    answer: str


class HealthResponse(BaseModel):
    """
    Response model for health check endpoint
    """
    status: str
    service: str
    message: str

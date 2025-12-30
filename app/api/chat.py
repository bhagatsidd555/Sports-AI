from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

from app.ai_layer.generator import generate_insight

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    metrics: Dict
    question: str | None = None


@router.post("/")
def chat_with_performance(data: ChatRequest):
    """
    Chat endpoint to interpret performance metrics
    """

    try:
        if not data.metrics:
            raise HTTPException(status_code=400, detail="Metrics data is required")

        insight = generate_insight(data.metrics)

        return {
            "status": "success",
            "answer": insight
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Chat processing failed: {str(e)}"
        )

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai_layer.generator import generate_ai_response
from app.kpi_engine.aggregator import calculate_all_kpis

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    athlete_id: str | None = None
    kpi_data: dict | None = None

class ChatResponse(BaseModel):
    answer: str
    confidence: float

@router.post("/", response_model=ChatResponse)
def chat_with_ai(request: ChatRequest):
    """
    Ask performance-related questions to AI
    """
    try:
        kpis = {}

        if request.kpi_data:
            kpis = calculate_all_kpis(request.kpi_data)

        ai_answer = generate_ai_response(
            question=request.question,
            kpis=kpis
        )

        return ChatResponse(
            answer=ai_answer,
            confidence=0.92
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

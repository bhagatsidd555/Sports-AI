import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from openai import OpenAI

from app.ai_layer.prompts import (
    SYSTEM_ROLE,
    ATHLETE_SUMMARY_PROMPT,
    COACH_INSIGHT_PROMPT,
    QUESTION_ANSWER_PROMPT
)

load_dotenv()

class AIGenerator:
    """
    Central AI interaction layer.
    Handles all LLM-based insight generation.
    """

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4.1-mini"  # stable, cost-efficient

    def _call_llm(self, user_prompt: str) -> str:
        """
        Internal helper to call OpenAI Chat Completion
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_ROLE},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
            max_tokens=600,
        )

        return response.choices[0].message.content.strip()

    def generate_athlete_summary(
        self,
        session_data: Dict[str, Any],
        kpis: Dict[str, Any]
    ) -> str:
        """
        Generate athlete performance summary
        """
        prompt = ATHLETE_SUMMARY_PROMPT.format(
            data=session_data,
            metrics=kpis
        )
        return self._call_llm(prompt)

    def generate_coach_insights(
        self,
        kpis: Dict[str, Any],
        trends: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Generate coach-focused insights using trends
        """
        prompt = COACH_INSIGHT_PROMPT.format(
            metrics=kpis,
            trends=trends or "No historical trend data available"
        )
        return self._call_llm(prompt)

    def answer_question(
        self,
        question: str,
        kpis: Dict[str, Any]
    ) -> str:
        """
        Answer ad-hoc questions from coach/athlete
        """
        prompt = QUESTION_ANSWER_PROMPT.format(
            question=question,
            metrics=kpis
        )
        return self._call_llm(prompt)

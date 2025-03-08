from fastapi import APIRouter
from app.models.mentor_ai import ask_mentor

router = APIRouter(prefix="/mentor", tags=["AI Mentor"])

@router.get("/ask")
def chat_with_mentor(question: str):
    return {"response": ask_mentor(question)}

from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_service import RAGService
from services.history_service import HistoryService

router = APIRouter()

rag = RAGService()
history = HistoryService()


class ChatRequest(BaseModel):
    message: str
    session_id: int | None = None
    source: str | None = None


@router.post("/chat")
def chat(request: ChatRequest):

    # اگر session نداریم بساز
    if not request.session_id:
        request.session_id = history.create_session(
            title=request.message[:20]
        )

    # ذخیره پیام کاربر
    history.save_message(
        request.session_id,
        "user",
        request.message
    )

    # پاسخ RAG
    result = rag.ask(
        question=request.message,
        source=request.source
    )

    # ذخیره جواب bot
    history.save_message(
        request.session_id,
        "bot",
        result["answer"]
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "session_id": request.session_id
    }
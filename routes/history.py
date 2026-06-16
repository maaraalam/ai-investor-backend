from fastapi import APIRouter
from services.history_service import HistoryService

router = APIRouter()

history = HistoryService()


@router.get("/sessions")
def get_sessions():

    return history.get_sessions()


@router.get("/sessions/{session_id}")
def get_session_messages(session_id: int):

    messages = history.get_messages(session_id)

    return [
        {
            "role": m.role,
            "content": m.content
        }
        for m in messages
    ]
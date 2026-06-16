 from db.database import SessionLocal
from db.models import ChatSession, ChatMessage


class HistoryService:

    def create_session(self, title="New Chat"):

        db = SessionLocal()

        session = ChatSession(title=title)
        db.add(session)
        db.commit()
        db.refresh(session)

        db.close()

        return session.id

    def save_message(self, session_id, role, content):

        db = SessionLocal()

        msg = ChatMessage(
            session_id=session_id,
            role=role,
            content=content
        )

        db.add(msg)
        db.commit()

        db.close()

    def get_messages(self, session_id):

        db = SessionLocal()

        messages = db.query(ChatMessage)\
            .filter(ChatMessage.session_id == session_id)\
            .all()

        db.close()

        return messages

    def get_sessions(self):

        db = SessionLocal()

        sessions = db.query(ChatSession).all()

        db.close()

        return sessions
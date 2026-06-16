from fastapi import APIRouter
from pydantic import BaseModel

from db.database import SessionLocal
from db.models import User
from services.auth_service import AuthService

router = APIRouter()

auth = AuthService()


class UserCreate(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    new_user = User(
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = auth.create_token(new_user.id)

    return {"token": token}
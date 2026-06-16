from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"


class AuthService:

    def create_token(self, user_id: int):

        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(days=7)
        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token: str):

        try:
            return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except:
            return None
from pydantic import BaseModel


class QuizRequest(BaseModel):

    document_name: str

    questions_count: int = 5


class QuizResponse(BaseModel):

    quiz: str
from pydantic import BaseModel


class RAGRequest(BaseModel):

    question: str

    document_name: str


class RAGResponse(BaseModel):

    answer: str
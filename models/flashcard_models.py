from pydantic import BaseModel


class FlashcardRequest(BaseModel):

    document_name: str

    count: int = 10


class FlashcardResponse(BaseModel):

    flashcards: str
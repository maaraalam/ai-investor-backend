from pathlib import Path

from fastapi import APIRouter

from models.flashcard_models import (
    FlashcardRequest,
    FlashcardResponse
)

from services.flashcard_service import (
    FlashcardService
)

router = APIRouter()

flashcard_service = FlashcardService()


@router.post(
    "/generate-flashcards",
    response_model=FlashcardResponse
)
def generate_flashcards(
    request: FlashcardRequest
):

    file_path = Path(
        f"data/extracted/{request.document_name}.txt"
    )

    text = file_path.read_text(
        encoding="utf-8"
    )

    flashcards = (
        flashcard_service.generate_flashcards(
            text,
            request.count
        )
    )

    return FlashcardResponse(
        flashcards=flashcards
    )
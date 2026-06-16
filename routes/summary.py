from pathlib import Path

from fastapi import APIRouter

from models.summary_models import (
    SummaryRequest,
    SummaryResponse
)

from services.summary_service import (
    SummaryService
)

router = APIRouter()

summary_service = SummaryService()


@router.post(
    "/summarize",
    response_model=SummaryResponse
)
def summarize(
    request: SummaryRequest
):

    file_path = Path(
        f"data/extracted/{request.document_name}.txt"
    )

    text = file_path.read_text(
        encoding="utf-8"
    )

    summary = (
        summary_service.summarize(
            text
        )
    )

    return SummaryResponse(
        summary=summary
    )
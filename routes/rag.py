from fastapi import APIRouter

from models.rag_models import (
    RAGRequest,
    RAGResponse
)

from services.rag_service import (
    RAGService
)

router = APIRouter()

rag_service = RAGService()


@router.post(
    "/ask",
    response_model=RAGResponse
)
def ask(
    request: RAGRequest
):

    answer = rag_service.ask(
        question=request.question,
        document_name=request.document_name
    )

    return RAGResponse(
        answer=answer
    )
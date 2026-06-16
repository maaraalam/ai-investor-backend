from fastapi import APIRouter

from models.news_models import (
    NewsRequest,
    NewsResponse
)

from services.news_service import (
    NewsService
)

router = APIRouter()

news_service = NewsService()


@router.post(
    "/analyze-news",
    response_model=NewsResponse
)
def analyze_news(
    request: NewsRequest
):

    analysis = (
        news_service.analyze(
            request.news_text
        )
    )

    return NewsResponse(
        analysis=analysis
    )
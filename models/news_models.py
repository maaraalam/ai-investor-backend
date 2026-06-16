from pydantic import BaseModel


class NewsRequest(BaseModel):

    news_text: str


class NewsResponse(BaseModel):

    analysis: str
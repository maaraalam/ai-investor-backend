from pydantic import BaseModel


class SummaryRequest(BaseModel):

    document_name: str


class SummaryResponse(BaseModel):

    summary: str
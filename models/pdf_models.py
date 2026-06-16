from pydantic import BaseModel
 


class PDFResponse(BaseModel):

    file_name: str

    chars_count: int

    chunks_count: int

    preview: str
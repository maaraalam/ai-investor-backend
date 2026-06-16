from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from models.pdf_models import PDFResponse
from services.pdf_service import PDFService
from services.indexing_service import IndexingService

router = APIRouter()

pdf_service = PDFService()
indexing_service = IndexingService()


# ✅ مهم‌ترین بخش: همین endpoint
@router.post("/upload-pdf", response_model=PDFResponse)
async def upload_pdf(file: UploadFile = File(...)):

    # 1. ساخت پوشه آپلود
    upload_dir = Path("data/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    # 2. ذخیره فایل PDF
    file_path = upload_dir / file.filename

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    # 3. استخراج متن از PDF
    text = pdf_service.extract_text(str(file_path))

    # 4. ذخیره متن استخراج شده
    output_file = Path("data/extracted") / f"{file.filename}.txt"

    pdf_service.save_text(text, str(output_file))

    # 5. ایندکس کردن در Vector DB
    chunks_count = indexing_service.index_document(
        file.filename,
        text
    )

    # 6. پاسخ API
    return {
        "file_name": file.filename,
        "chars_count": len(text),
        "chunks_count": chunks_count,
        "preview": text[:500]
    }
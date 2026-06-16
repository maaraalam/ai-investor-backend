from pathlib import Path
from pypdf import PdfReader


class PDFService:

    def extract_text(self, pdf_path: str) -> str:

        reader = PdfReader(pdf_path)

        full_text = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                full_text.append(page_text)

        return "\n".join(full_text)

    def save_text(
        self,
        text: str,
        output_path: str
    ):

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)
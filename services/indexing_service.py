from services.embedding_service import EmbeddingService
from services.vector_service import VectorService


class IndexingService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_service = VectorService()

    def chunk_text(self, text: str, chunk_size: int = 500):

        # جلوگیری از متن خالی
        if not text:
            return []

        return [
            text[i:i + chunk_size]
            for i in range(0, len(text), chunk_size)
            if text[i:i + chunk_size].strip()
        ]

    def index_document(self, document_name: str, text: str):

        chunks = self.chunk_text(text)

        # 🚨 جلوگیری از crash
        if not chunks:
            print("❌ No chunks generated from PDF")
            return 0

        embeddings = self.embedding_service.embed_documents(chunks)

        # 🚨 جلوگیری از embedding خالی
        if not embeddings:
            print("❌ Embeddings are empty")
            return 0

        ids = [
            f"{document_name}_{i}"
            for i in range(len(chunks))
        ]

        self.vector_service.add_documents(
            ids=ids,
            texts=chunks,
            embeddings=embeddings,
            source=document_name
        )

        return len(chunks)
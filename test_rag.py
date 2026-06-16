from services.rag_service import (
    RAGService
)

rag = RAGService()

answer = rag.ask(
    "ETF چیست؟"
)

print(answer)
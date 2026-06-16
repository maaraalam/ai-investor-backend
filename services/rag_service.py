from services.embedding_service import EmbeddingService
from services.vector_service import VectorService
from services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.embedding = EmbeddingService()
        self.vector = VectorService()
        self.llm = LLMService()

    def ask(self, question: str, source: str = None):

        query_embedding = self.embedding.embed_query(question)

        result = self.vector.search(
            query_embedding=query_embedding,
            top_k=3,
            source_filter=source
        )

        docs = result["documents"][0]
        metas = result["metadatas"][0]

        if not docs:
            return {
                "answer": "در این کتاب چیزی پیدا نشد",
                "sources": []
            }

        context = "\n\n".join(docs)

        sources = list(set([
            m.get("source", "unknown")
            for m in metas
        ]))

        prompt = f"""
تو یک دستیار مالی هستی.

فقط از متن زیر جواب بده.

----------------
متن:
{context}

سوال:
{question}
"""

        answer = self.llm.ask(prompt)

        return {
            "answer": answer,
            "sources": sources
        }
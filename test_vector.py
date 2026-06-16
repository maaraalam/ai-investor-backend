from services.chunk_service import ChunkService
from services.embedding_service import EmbeddingService
from services.vector_service import VectorService

sample_text = """
ETF صندوق قابل معامله در بورس است.
سرمایه گذاران می توانند واحدهای آن را خرید و فروش کنند.
صندوق های ETF دارای نقدشوندگی بالا هستند.
"""

chunk_service = ChunkService()
embedding_service = EmbeddingService()
vector_service = VectorService()

chunks = chunk_service.create_chunks(sample_text)

print(f"Chunks: {len(chunks)}")

embeddings = embedding_service.embed_documents(chunks)

ids = [f"chunk_{i}" for i in range(len(chunks))]

vector_service.add_documents(
    ids=ids,
    texts=chunks,
    embeddings=embeddings
)

query_embedding = embedding_service.embed_query(
    "ETF چیست؟"
)

result = vector_service.search(
    query_embedding,
    top_k=3
)

print(result)
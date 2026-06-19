# import chromadb


# class VectorService:

#     def __init__(self):

#         self.client = chromadb.PersistentClient(
#             path="data/vectordb"
#         )

#         self.collection = self.client.get_or_create_collection(
#             name="financial_docs"
#         )

#     def add_documents(self, ids, texts, embeddings, source):

#         metadatas = [
#             {"source": source}
#             for _ in texts
#         ]

#         self.collection.add(
#             ids=ids,
#             documents=texts,
#             embeddings=embeddings,
#             metadatas=metadatas
#         )

#     def search(self, query_embedding, top_k=5, source_filter=None):

#         where = None

#         # 🔥 فیلتر بر اساس کتاب
#         if source_filter:
#             where = {"source": source_filter}

#         return self.collection.query(
#             query_embeddings=[query_embedding],
#             n_results=top_k,
#             where=where,
#             include=["documents", "metadatas"]
#         )


class VectorService:
    def add_documents(self, *args, **kwargs):
        return True

    def search(self, *args, **kwargs):
        return []
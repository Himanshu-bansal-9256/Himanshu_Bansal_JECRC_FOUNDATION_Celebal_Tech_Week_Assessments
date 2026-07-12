from langchain_community.retrievers import BM25Retriever


class HybridRetriever:

    def __init__(self, vector_store, documents):

        self.vector_store = vector_store

        self.documents = documents

        self.bm25 = BM25Retriever.from_documents(documents)

        self.bm25.k = 3

    def retrieve(self, question):

        # FAISS Search
        vector_docs = self.vector_store.similarity_search(
            question,
            k=3
        )

        # BM25 Search
        keyword_docs = self.bm25.invoke(question)

        combined = []

        seen = set()

        for doc in vector_docs + keyword_docs:

            if doc.page_content not in seen:

                combined.append(doc)

                seen.add(doc.page_content)

        return combined
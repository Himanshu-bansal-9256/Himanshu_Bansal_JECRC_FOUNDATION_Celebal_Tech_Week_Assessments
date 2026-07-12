from utils.loader import load_multiple_pdfs
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model
from utils.vectorstore import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)
from utils.memory import build_chat_history
from utils.hybrid_retriever import HybridRetriever
from utils.query_router import QueryRouter

from llm.groq import get_llm
from prompts.prompt import RAG_PROMPT


class RAGPipeline:

    def __init__(self):

        self.embedding_model = get_embedding_model()

        self.vector_store = None
        self.documents = []
        
        self.router = QueryRouter()
        self.llm = get_llm()

    # Process PDFs
    def process_pdfs(self, pdf_paths):

        documents = load_multiple_pdfs(pdf_paths)

        chunks = split_documents(documents)
        self.documents = chunks

        self.vector_store = create_vector_store(
            chunks,
            self.embedding_model
        )

        save_vector_store(self.vector_store)

        return len(documents), len(chunks)

    # Retrieve Documents
    def retrieve(self, question):

        if self.vector_store is None:
            raise ValueError(
                "Please upload PDFs first."
            )

        retriever = HybridRetriever(
            self.vector_store,
            self.documents
        )

        docs = retriever.retrieve(question)

        return docs

    # Build Prompt
    def build_prompt(self, docs, question, history):

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        return RAG_PROMPT.format(
            history=history,
            context=context,
            question=question
        )

    # Ask Question
    def ask_question(self, question, messages):

        docs = self.retrieve(question)
        history = build_chat_history(messages)

        prompt = self.build_prompt(
            docs,
            question,
            history
        )
        query_type = self.router.classify(question)
        print(query_type)
        response = self.llm.invoke(prompt)

        return response.content, docs
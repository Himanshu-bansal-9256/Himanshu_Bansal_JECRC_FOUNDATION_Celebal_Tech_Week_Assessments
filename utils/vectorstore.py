import os

from langchain_community.vectorstores import FAISS

from config import VECTOR_DB_PATH


def create_vector_store(chunks, embedding_model):

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store):

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    vector_store.save_local(VECTOR_DB_PATH)


def load_vector_store(embedding_model):

    if not os.path.exists(VECTOR_DB_PATH):
        return None

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

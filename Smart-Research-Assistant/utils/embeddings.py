from langchain_community.embeddings import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL


def get_embedding_model():

    return HuggingFaceEmbeddings(

        model_name=EMBEDDING_MODEL

    )

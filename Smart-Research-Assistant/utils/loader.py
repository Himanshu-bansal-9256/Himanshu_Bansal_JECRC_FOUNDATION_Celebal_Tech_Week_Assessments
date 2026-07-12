from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path):

    loader = PyPDFLoader(file_path)

    return loader.load()


def load_multiple_pdfs(file_paths):

    documents = []

    for file_path in file_paths:

        loader = PyPDFLoader(file_path)

        documents.extend(loader.load())

    return documents
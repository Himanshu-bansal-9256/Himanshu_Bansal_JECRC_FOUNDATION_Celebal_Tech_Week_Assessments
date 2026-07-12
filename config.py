import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Directories
DATA_FOLDER = "data"
VECTOR_DB_PATH = "vectorstore/faiss_index"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# LLM
LLM_TEMPERATURE = 0.3
TOP_K_RESULTS = 5
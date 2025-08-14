import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Paths
FAISS_INDEX_PATH = "data/embeddings/faiss_index"

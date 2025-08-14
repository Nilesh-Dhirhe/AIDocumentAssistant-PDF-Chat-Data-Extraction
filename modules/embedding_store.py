import faiss
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from config.settings import OPENAI_API_KEY, FAISS_INDEX_PATH
import os
import pickle

embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

def create_faiss_index(chunks):
    """Creates and saves a FAISS index from text chunks."""
    vectors = embedding_model.embed_documents(chunks)
    vectors = np.array(vectors).astype("float32")

    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
    faiss.write_index(index, FAISS_INDEX_PATH)

    with open(f"{FAISS_INDEX_PATH}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def search_faiss_index(query, top_k=5):
    """Search FAISS index for similar chunks."""
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(f"{FAISS_INDEX_PATH}_chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    query_vector = embedding_model.embed_query(query)
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, top_k)
    results = [chunks[i] for i in indices[0]]
    return results

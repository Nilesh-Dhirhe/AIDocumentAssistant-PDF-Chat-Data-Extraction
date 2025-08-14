import numpy as np
from src.embedding_store import get_embedding, build_faiss_index

def test_embedding_vector():
    vector = get_embedding("Hello World")
    assert isinstance(vector, np.ndarray)
    assert vector.shape[0] > 0

def test_faiss_index():
    chunks = ["Hello", "World"]
    index, chunk_list = build_faiss_index(chunks)
    assert len(chunk_list) == 2

from src.retriever import create_retrieval_pipeline, retrieve_answer

def test_pipeline():
    index, chunks = create_retrieval_pipeline("data/sample.pdf")
    assert len(chunks) > 0

def test_retrieval():
    index, chunks = create_retrieval_pipeline("data/sample.pdf")
    results = retrieve_answer(index, chunks, "test query")
    assert isinstance(results, list)

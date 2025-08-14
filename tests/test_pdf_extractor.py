import os
from src.pdf_extractor import extract_text_from_pdf, chunk_text

def test_pdf_extraction():
    text = extract_text_from_pdf("data/sample.pdf")
    assert isinstance(text, str) and len(text) > 0

def test_chunking():
    text = "This is a test text for chunking." * 10
    chunks = chunk_text(text, chunk_size=20, overlap=5)
    assert all(len(chunk) <= 20 for chunk in chunks)

import PyPDF2
import re
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def clean_text(text):
    """Cleans extracted text by removing extra spaces and non-ASCII chars."""
    text = re.sub(r'\s+', ' ', text)
    text = text.encode("ascii", "ignore").decode()
    return text.strip()

def chunk_text(text):
    """Splits text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks

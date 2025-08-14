# AI Document Assistant – PDF Chat & Data Extraction

## Overview
This project is a **Retrieval-Augmented Generation (RAG)**-based PDF assistant that enables contextual question-answering over PDF documents. It uses **OpenAI GPT** for natural language processing, **FAISS** for vector search, and custom text extraction + chunking for precise document retrieval.

## Features
- PDF text extraction and preprocessing
- Custom chunking for improved retrieval accuracy
- FAISS indexing with embedding normalization and custom distance metrics
- Semantic search over document content
- OpenAI GPT-powered contextual responses
- Configurable retrieval workflows

## Tech Stack
- **Python 3.10+**
- [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF text extraction
- [LangChain](https://www.langchain.com/) – RAG pipelines
- [FAISS](https://faiss.ai/) – Vector search and similarity retrieval
- [OpenAI API](https://platform.openai.com/) – LLM integration
- [NumPy](https://numpy.org/) – Data manipulation
- [pytest](https://docs.pytest.org/) – Unit testing

## Project Structure
AI-Document-Assistant/
│
├── src/
│ ├── extract_text.py # PDF extraction & chunking
│ ├── build_index.py # FAISS index creation & management
│ ├── query_engine.py # Query handling & GPT integration
│ ├── config.py # Configuration settings
│
├── tests/
│ ├── test_extract_text.py # Unit tests for text extraction
│ ├── test_build_index.py # Unit tests for FAISS indexing
│ ├── test_query_engine.py # Unit tests for query flow
│
├── requirements.txt
├── README.md
└── .env # API keys & config variables



## Installation
 ```bash 
# Clone the repository
git clone https://github.com/yourusername/AI-Document-Assistant.git
cd AI-Document-Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt    

```
## Environment Variables

Create a .env file in the root directory with:
OPENAI_API_KEY=your_openai_api_key

## Usage
# Extract text & build index
python src/extract_text.py
python src/build_index.py

# Run query engine
python src/query_engine.py


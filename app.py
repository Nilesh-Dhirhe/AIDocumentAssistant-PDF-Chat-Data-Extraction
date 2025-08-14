import streamlit as st
from modules.pdf_processing import extract_text_from_pdf, clean_text, chunk_text
from modules.embedding_store import create_faiss_index
from modules.query_handler import generate_answer
import os

st.title("AI Document Assistant 📄🤖")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.write("Extracting text...")
    text = extract_text_from_pdf("data/temp.pdf")
    text = clean_text(text)
    chunks = chunk_text(text)

    st.write("Creating FAISS index...")
    create_faiss_index(chunks)
    st.success("Index created! You can now ask questions.")

query = st.text_input("Enter your question about the document:")

if query:
    answer = generate_answer(query)
    st.write("### Answer:")
    st.write(answer)

import openai
from modules.embedding_store import search_faiss_index
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_answer(query):
    """Uses retrieved context and GPT to generate an answer."""
    context_chunks = search_faiss_index(query)
    context_text = "\n".join(context_chunks)

    prompt = f"""
    You are a helpful assistant. Use the following context to answer:
    {context_text}
    Question: {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message["content"]

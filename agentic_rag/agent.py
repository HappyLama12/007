import chromadb
from sentence_transformers import SentenceTransformer
import requests

CHROMA_HOST = "localhost"
CHROMA_PORT = 8000
CHROMA_COLLECTION_NAME = "website_content"
OLLAMA_MODEL = "llama3"  # Or mistral, phi3, etc.
OLLAMA_URL = "http://localhost:11434/api/generate"

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
collection = client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)


def ask_agent(user_query, k=5):
    # Step 1: Embed user query
    embedding = embedder.encode(user_query).tolist()

    # Step 2: Search ChromaDB
    results = collection.query(query_embeddings=[embedding], n_results=k)
    context_chunks = results["documents"][0]
    context = "\n".join(context_chunks)

    # Step 3: Construct prompt
    prompt = f"""Answer the question based on the following context:\n{context}\n\nQuestion: {user_query}\nAnswer:"""

    # Step 4: Call local LLM via Ollama API
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )
    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    while True:
        query = input("\n🔍 Ask a question (or 'exit'): ")
        if query.lower() in {"exit", "quit"}:
            break
        answer = ask_agent(query)
        print(f"\n💬 Answer:\n{answer}")
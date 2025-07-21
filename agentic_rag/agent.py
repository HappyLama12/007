import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection(name="web_content")

def query_llm(question, k=5):
    embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=k,
        include=["documents", "distances"]
    )
    docs = results.get("documents", [[]])[0]
    return "\n".join(docs)

if __name__ == "__main__":
    query = input("Ask something: ")
    print(query_llm(query))

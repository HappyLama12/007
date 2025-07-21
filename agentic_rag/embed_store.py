import chromadb
from sentence_transformers import SentenceTransformer
import hashlib

client = chromadb.Client()
collection = client.get_or_create_collection(name="web_content")
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_id(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def store_chunks(chunks):
    existing_ids = set(collection.get()["ids"])
    to_add = []
    for chunk in chunks:
        chunk_id = generate_id(chunk)
        if chunk_id not in existing_ids:
            embedding = model.encode(chunk).tolist()
            to_add.append((chunk_id, chunk, embedding))

    if to_add:
        ids, docs, embeds = zip(*to_add)
        collection.add(documents=docs, embeddings=embeds, ids=ids)
        print(f"Stored {len(ids)} new items.")
    else:
        print("No new items to store.")

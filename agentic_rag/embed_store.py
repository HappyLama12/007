from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup
from langdetect import detect
import chromadb
from config import *

def extract_text_from_page(page):
    text = page.get("content") or page.get("text")
    if not text or len(text.strip()) < 50:
        html = page.get("html", "")
        if html:
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
    return text.strip() if text else None

def chunk_text(text, max_chunk_size=MAX_CHUNK_SIZE):
    return [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]

def embed_pages(pages):
    model = SentenceTransformer(EMBEDDING_MODEL)
    docs, ids, embeddings = [], [], []

    for i, page in enumerate(pages):
        text = extract_text_from_page(page)
        if not text:
            print(f"[WARN] Page {i} has no text, skipping.")
            continue

        chunks = chunk_text(text)
        for j, chunk in enumerate(chunks):
            try:
                if detect(chunk) != LANGUAGE:
                    continue
            except:
                continue
            chunk = chunk.strip()
            if not chunk:
                continue
            embedding = model.encode(chunk)
            embeddings.append(embedding.tolist())
            docs.append(chunk)
            ids.append(f"page_{i}_chunk_{j}")

    print(f"[INFO] Embedded {len(docs)} chunks.")
    return ids, docs, embeddings

def store_embeddings(ids, docs, embeddings):
    if not embeddings:
        print("[WARN] No embeddings to store.")
        return

    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    collection = client.get_or_create_collection(CHROMA_COLLECTION_NAME)

    collection.add(documents=docs, embeddings=embeddings, ids=ids)
    print(f"[INFO] Stored {len(ids)} items in ChromaDB.")

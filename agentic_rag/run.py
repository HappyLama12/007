from crawl import crawl
from embed_store import store_chunks

def pipeline():
    print("Starting crawl + embed pipeline...")
    content = crawl()
    chunks = [para for text in content for para in text.split("\n") if para.strip()]
    print(f"Embedding {len(chunks)} chunks")
    store_chunks(chunks)
    print("Pipeline complete.")

if __name__ == "__main__":
    pipeline()

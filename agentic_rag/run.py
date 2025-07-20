from crawl import crawl_website
from embed_store import embed_pages, store_embeddings

def main():
    print("[MAIN] Starting crawl + embed pipeline...")
    pages = crawl_website()
    ids, docs, embeddings = embed_pages(pages)
    store_embeddings(ids, docs, embeddings)
    print("[MAIN] Pipeline complete.")

if __name__ == "__main__":
    main()

# Agentic RAG

This is a modular RAG pipeline using:

- Local LLM via [Ollama](https://ollama.com)
- Web crawling with [Crawl4AI](https://docs.crawl4ai.com)
- Vector storage via [ChromaDB](https://www.trychroma.com/)
- Embeddings with `sentence-transformers`

## Setup

1. Install requirements:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the full pipeline:
   ```bash
   python run.py
   ```

## Next Steps

- Add `agent.py` for answering user questions using retrieved chunks + LLM.
- Build OpenWebUI / CLI / FastAPI layer.

# Agentic RAG: Local LLM + Crawl4AI + ChromaDB Pipeline

This project builds an **Agentic Retrieval-Augmented Generation (RAG)** system using:

* **Local LLM** served by [Ollama](https://ollama.com)
* **Web crawling and scraping** with [Crawl4AI](https://docs.crawl4ai.com)
* **Vector storage and similarity search** using [ChromaDB](https://www.trychroma.com)
* **Embeddings** via [sentence-transformers](https://www.sbert.net)

---

## Project Structure

```
agentic_rag/
├── agent.py          # Query interface: search ChromaDB and call local LLM
├── crawl.py          # Crawl websites using Crawl4AI
├── embed_store.py    # Chunk, embed, and store content in ChromaDB
├── config.py         # Centralized config (URLs, tokens, model names)
├── run.py            # Main runner to crawl, embed, and store pipeline
├── utils.py          # Utility helpers (optional)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Setup Instructions

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Run Supporting Services

Make sure the following are running locally:

* **Ollama LLM server**
* **ChromaDB** (via Docker)
* **Crawl4AI** (via Docker or local server)

### 3. Configure Your Pipeline

Edit `config.py` to set:

* `CRAWL4AI_URL`
* `CHROMA_HOST`, `CHROMA_PORT`
* `OLLAMA_MODEL` (e.g., `llama3`, `phi3`, etc.)

### 4. Run the Pipeline

```bash
python run.py --url https://example.com --depth 2
```

This will:

1. Crawl the website
2. Extract + chunk + embed the text
3. Store embeddings in ChromaDB

### 5. Query the Agent

You can later query your local agent via `agent.py`:

```bash
python agent.py --query "What is OpenAI?"
```

---

## Features

* Language filtering (English-only by default)
* Simple chunking strategy
* Reusable pipeline components
* Modular config for fast iteration

---

## TODOs / Ideas

* Add streaming output from Ollama
* Add web UI (e.g. with Gradio or Streamlit)
* Implement CAG (Cache-Augmented Generation) mode for faster recall
* Advanced chunking: by semantic boundaries or HTML tag parsing
* Add file/document ingestion (PDF, DOCX, etc.)

---

## References & Inspiration

* [Crawl4AI Docs](https://docs.crawl4ai.com)
* [ChromaDB](https://www.trychroma.com)
* [Ollama LLM Server](https://ollama.com)
* [SentenceTransformers](https://www.sbert.net)
* [LangChain: RAG from Scratch](https://github.com/langchain-ai/rag-from-scratch)
* [Medium Article: CAG vs. RAG](https://medium.com/@hamzaennaffati98/cache-augmented-generation-cag-vs-retrieval-augmented-generation-rag-7b668e3a973b)

---

License
MIT License © HappyLama12

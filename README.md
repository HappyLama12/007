# 007
speciel agent 
# Agentic RAG: Local LLM + Crawl4AI + ChromaDB Pipeline

This project builds an **Agentic Retrieval-Augmented Generation (RAG)** system using:

- **Local LLM** served by [Ollama](https://ollama.com)
- **Web crawling and scraping** with [Crawl4AI](https://docs.crawl4ai.com)
- **Vector storage and similarity search** using [ChromaDB](https://www.trychroma.com)
- **Embeddings** via [sentence-transformers](https://www.sbert.net)

---

## Project Structure

agentic_rag/
├── agent.py # Query interface: search ChromaDB and call local LLM
├── crawl.py # Crawl websites using Crawl4AI
├── embed_store.py # Chunk, embed, and store content in ChromaDB
├── config.py # Centralized config (URLs, tokens, model names)
├── run.py # Main runner to crawl, embed, and store pipeline
├── utils.py # Utility helpers (optional)
├── requirements.txt # Python dependencies
└── README.md # This file


---

## Setup

### 1. Clone repo

```bash
git clone https://github.com/your-username/agentic-rag.git
cd agentic-rag

**### 2. Create and activate virtual environment**
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\activate   # Windows PowerShell

**### 3. Install dependencies**
pip install -r requirements.txt

**### 4. Start dependent services**
Crawl4AI: run your Crawl4AI container or server locally

ChromaDB: start ChromaDB Docker or server locally

Ollama LLM: start your local Ollama LLM server (e.g., llama3, mistral, or phi3)

Usage
Run full pipeline: crawl → embed → store
bash
Copy
Edit
python run.py
This crawls the configured website, chunks and embeds content, and stores embeddings in ChromaDB.

Ask questions interactively
bash
Copy
Edit
python agent.py
You can then input questions; the agent will:

Embed your query

Search ChromaDB for relevant context

Generate an answer using the local Ollama LLM with retrieved context

Type exit or quit to end.

Configuration
Edit config.py to change:

CRAWL4AI_URL — your Crawl4AI API endpoint

WEBSITE_URL — website to crawl

CHROMA_HOST and CHROMA_PORT — ChromaDB endpoint

OLLAMA_MODEL and OLLAMA_URL — local LLM model and API URL

Embedding model, chunk size, and language filter

Next Steps & Enhancements
Add chat history and memory to support multi-turn conversations

Implement Cache-Augmented Generation (CAG) instead of vanilla RAG

Add pipeline automation, scheduling, and monitoring

Integrate with OpenWebUI or build a web frontend/REST API

Support multiple languages and dynamic crawl depth

Use advanced chunking and summarization for better context size control

References
Crawl4AI Documentation

ChromaDB

Ollama LLM

Sentence Transformers

RAG vs CAG Medium article

License
MIT License © HappyLama12

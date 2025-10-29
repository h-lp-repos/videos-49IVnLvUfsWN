# Lesson 3: Implementing RAG (Retrieval-Augmented Generation)

This repository contains all the starter code, data, and scripts for Lesson 3 videos on Implementing RAG. You will find separate folders with instructions for each of the practical demonstration videos.

## Structure

- `video-1/` – Environment & Starter Repo Quickstart: Setup, deps and sample index
- `video-2/` – Connect to Vector Index & Retrieve Top-K Chunks with Provenance
- `video-3/` – Prompt Construction & Token-Budget Enforcement (tiktoken demo)
- `video-4/` – Implement Relevance Reranker & Thresholding (rerank + filter)
- `video-5/` – Caching, Deduplication & Simple Retrieval Optimization
- `video-6/` – End-to-End Demo: Run 5 Sample Queries, Micro-benchmark & Failure Modes

## Setup

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd videos-49IVnLvUfsWN
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Ensure you have Python >=3.8 and required API keys or set sandbox mode:
   ```bash
   export RAG_LLM_MODE=sandbox
   ```

## Data & Index

- Sample corpus, queries, and index files are under `data/`.
- To (re)generate the FAISS index and metadata, run:
  ```bash
  python scripts/load_sample_index.py
  ```

## Scripts & Modules

- Scripts to run each demo are in `scripts/`.
- Core modules are at the repo root (`embeddings.py`, `retrieval.py`, etc.).
- Templates are in `templates/`.

Each `video-*` folder contains a `README.md` with step-by-step instructions for that demo.

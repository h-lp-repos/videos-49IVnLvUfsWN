# Lesson 3: Implementing RAG (Retrieval-Augmented Generation) - Starter Repo

This repository provides a starter implementation and reproducible scripts for the six practical videos in Lesson 3: Implementing RAG. It is intentionally lightweight and uses pure-Python fallbacks so students can run demonstrations without heavy native dependencies.

Structure
- sample-data/: small chunk corpus and embeddings used by the demos
- scripts/: runnable CLI scripts for each video demo (load index, query, retrieve, rerank, caching, benchmark)
- utils/: small helper modules (index loader/fallback, token utils, simple sandbox LLM, cache)
- video-1-environment-setup .. video-6-end-to-end-benchmark/: per-video README with instructions
- requirements.txt: optional Python requirements

Quickstart
1. (Optional) Create a Python virtualenv and install dependencies:
   - python3 -m venv .venv
   - source .venv/bin/activate
   - pip install -r requirements.txt

2. Verify the sample index and run a quick smoke test:
   - python scripts/load_sample_index.py
   - python scripts/query_index.py --query "test" --k 3

3. Explore other scripts per video README files.

Notes
- This repo uses a small JSON-based embedding store (sample-data/embeddings.json) and a deterministic pseudo-embedding for queries so the demos work without FAISS or external embedding services.
- A sandbox LLM stub is provided (utils/sandbox_llm.py) for safe deterministic runs during demos and benchmarking.


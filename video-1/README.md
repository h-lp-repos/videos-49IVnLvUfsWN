# Video 1: Environment & Starter Repo Quickstart

**Duration:** ~12 min

## Objective
Get a working local environment and starter repo running: install dependencies, configure API keys (or sandbox), and load the sample FAISS index so a basic retrieval command returns results.

## Prerequisites
- Python 3.8+
- pip, git, terminal access
- No prior setup required beyond cloning this repo

## Steps

1. **Clone the repo** and verify structure:
   ```bash
   git clone <repo-url>
   cd videos-49IVnLvUfsWN
   ls
   # You should see README.md, scripts/, data/, etc.
   ```
2. **Create a virtual environment** and install requirements:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set environment variables** (use sandbox mode if no API key):
   ```bash
   export RAG_LLM_MODE=sandbox
   ```
4. **Load the sample FAISS index**:
   ```bash
   python scripts/load_sample_index.py
   # Checkpoint: Loaded index with N vectors
   ```
5. **Run a quick retrieval smoke test**:
   ```bash
   python scripts/query_index.py --query "test" --k 3
   # Checkpoint: prints top-3 chunks with similarity scores and provenance
   ```

## Common Issues & Troubleshooting
- **Missing dependency**: pip install errors → ensure virtualenv is activated and try `pip install faiss-cpu`.
- **Env vars not set**: blank API key → sets `RAG_LLM_MODE=sandbox` and re-source terminal.
- **Index load fails**: dimension mismatch → re-run load script or verify sample_corpus.json format.

---
**Checkpoint:** If you see "Loaded index with" and retrieval results, you're ready for Video 2.

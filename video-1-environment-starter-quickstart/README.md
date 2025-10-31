# Video 1: Environment & Starter Repo Quickstart: Setup, Dependencies and Sample Index

**Estimated Duration:** 12 min

**Objective:**
Get a working local environment and starter repo running: install dependencies, configure API keys (or select sandbox), and load the sample FAISS index so a basic retrieval command returns results.

## Prerequisites

- Python 3.8+ and pip
- git
- Terminal access
- Instructor‑provided starter repo and sample FAISS index (or sandbox LLM stub)

## Steps (Reproducible Checklist)

1. Clone the starter repo and verify you see the project README:
   ```bash
   git clone <starter-repo-url>
   cd <repo-root>
   ls
   ```
2. Create a virtual environment and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
3. Set environment variables: API_KEY or sandbox mode:
   ```bash
   export API_KEY=<your_api_key>
   # or
   export RAG_LLM_MODE=sandbox
   ```
4. Load the sample FAISS index:
   ```bash
   python scripts/load_sample_index.py
   ```
5. Run a quick retrieval smoke test:
   ```bash
   python scripts/query_index.py --query "test" --k 3
   ```

## Common Errors & Troubleshooting

- **Missing dependency** → pip install failure: try installing `faiss-cpu` or verify your Python environment.
- **Environment variables not detected** → blank API key: export variables and re-source your shell.
- **Index dimension mismatch** → verify index metadata or regenerate index with matching dimensions.

## Materials

- `scripts/`: `load_sample_index.py` and `query_index.py`
- `requirements.txt`
- `notebooks/`: Example notebook for setup
- `assets/`: Slides and terminal screenshots
- `verification_artifacts/`: Expected CLI output

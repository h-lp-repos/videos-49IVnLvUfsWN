# Video 2: Connect to Vector Index & Retrieve Top-K Chunks with Provenance

**Estimated Duration:** 12 min

**Objective:**
Demonstrate using the retrieval module to query an index, inspect the top-K chunks with provenance metadata (source_id, chunk_id, score), and verify embedding-dimension compatibility.

## Prerequisites

- Video 1 completed with a loaded index
- Virtual environment activated with dependencies installed

## Steps (Reproducible Checklist)

1. Open the retrieval module code and review the `retrieve(query, k)` function signature; confirm it returns `source_id`, `chunk_id`, `score`, and `text`.
2. Run:
   ```bash
   python scripts/retrieve.py --query "How to rotate a key?" --k 5
   ```
3. Verify embedding dimensions match the index:
   ```bash
   python -c "from embeddings import get_dim; print(get_dim())"
   ```
4. Inspect the provenance of a returned chunk (source_id and chunk_id).
5. Demonstrate error handling by querying with a malformed query or missing index file.

## Common Errors & Troubleshooting

- Empty results returned → ensure correct index path or reload the index.
- Embedding-dimension mismatch → regenerate embeddings or use a matching index.
- Missing provenance fields → verify ingestion process preserved provenance metadata.

## Materials

- `scripts/`: `retrieve.py`, `retrieve_module.py`, and `embeddings.py`
- `requirements.txt`
- `notebooks/`: Demo notebook
- `assets/`: Architecture diagram and terminal snapshot
- `verification_artifacts/`: Expected CLI output
- `sample_data/`: Chunked corpus data and metadata

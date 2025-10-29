# Video 2: Connect to Vector Index & Retrieve Top-K Chunks with Provenance

**Duration:** ~12 min

## Objective
Demonstrate using the retrieval module to query an index, inspect top-K chunks with provenance (source_id, chunk_id, score), and verify embedding-dimension compatibility.

## Prerequisites
- Video 1 completed
- Sample index loaded (data/sample_index.faiss)

## Steps

1. **Inspect retrieval function signature**:
   ```bash
   sed -n '1,20p' retrieval.py
   # Check for retrieve(query, k) and provenance keys in return dict
   ```
2. **Run retrieval CLI**:
   ```bash
   python scripts/retrieve.py --query "How to rotate a key?" --k 5
   # Checkpoint: prints 5 results with score values and provenance
   ```
3. **Verify embedding dimension**:
   ```bash
   python -c "from embeddings import get_dim; print(get_dim())"
   ```
4. **Inspect one chunk's provenance source**:
   ```bash
   # Use source_id and chunk_id from output to locate text in data/sample_corpus.json
   grep -R "doc" -n data/sample_corpus.json
   ```
5. **Demonstrate error handling** (e.g., missing index):
   ```bash
   mv data/sample_index.faiss data/tmp.faiss
   python scripts/retrieve.py --query "X" --k 1
   # Checkpoint: shows error message about missing index
   mv data/tmp.faiss data/sample_index.faiss
   ```

## Common Issues & Troubleshooting
- **Zero results**: verify sample_index.faiss exists and k <= number of vectors.
- **Dimension mismatch**: ensure embeddings dim matches index dim; re-run load script if needed.

---
**Checkpoint:** If you see top-K chunks with provenance fields, proceed to Video 3.

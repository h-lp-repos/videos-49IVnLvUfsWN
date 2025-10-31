# Video 4: Implement Relevance Reranker & Thresholding

**Estimated Duration:** 12 min

**Objective:**
Implement and demo a simple relevance reranker that reorders top-K chunks by a combined similarity + feature score, applies a configurable threshold to filter low-relevance chunks, and observe changes in the constructed prompt.

## Prerequisites

- Video 2 completed
- Environment with dependencies installed (`numpy`, `pandas`)

## Steps (Reproducible Checklist)

1. Open `scripts/rerank_module.py` and review the `combine(score, feature, w_sim, w_feat)` and `rerank` functions.
2. Run reranker on simulated retrieval results:
   ```bash
   python scripts/rerank.py --query "X" --k 10 --weights 0.8,0.2
   ```
3. Apply a threshold filter:
   ```bash
   python scripts/rerank.py --query "X" --k 10 --weights 0.8,0.2 --threshold 0.35
   ```
4. Show integration with the prompt constructor and the effect on the final prompt.
5. Experiment by toggling the threshold and observe differences in chunk order and prompt content.

## Common Errors & Troubleshooting

- **NaN in combined_score**: sanitize inputs or use default values.
- **Threshold filters out all chunks**: set a minimum floor or fallback to top-1 chunk.
- **Schema mismatch with prompt constructor**: ensure correct keys in chunk dictionaries.

## Materials

- `scripts/`: `rerank.py`, `rerank_module.py`, and `retrieve_module.py`
- `requirements.txt`
- `notebooks/`: Demo notebook
- `assets/`: Screenshots and graphs
- `verification_artifacts/`: Expected CLI output

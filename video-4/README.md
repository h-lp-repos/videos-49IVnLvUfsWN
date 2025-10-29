# Video 4: Implement Relevance Reranker & Thresholding

**Duration:** ~12 min

## Objective
Implement and demo a simple relevance reranker that reorders top-K by combined similarity and feature score, apply a configurable threshold to filter low-relevance chunks, and observe prompt changes.

## Prerequisites
- Video 2 completed

## Steps

1. **Inspect reranker function**:
   ```bash
   sed -n '1,20p' reranker.py
   # Look for combine(score, feature, weights)
   ```
2. **Run reranker on top-10**:
   ```bash
   python scripts/rerank.py --query "Sample query" --k 10 --weights "0.8,0.2"
   # Checkpoint: prints reordered list with combined scores
   ```
3. **Apply threshold filtering**:
   ```bash
   python scripts/rerank.py --query "Sample query" --k 10 --weights "0.8,0.2" --threshold 0.35
   # Checkpoint: prints fewer chunks above threshold
   ```
4. **Plug reranked output into prompt constructor**:
   ```bash
   python prompt_constructor.py --query "Sample query" --k 10 --budget 2048
   # Checkpoint: prompt reflects reranked chunk order
   ```
5. **Experiment threshold effect**:
   ```bash
   # Toggle threshold and observe changes in prompt output
   ```

## Common Issues & Troubleshooting
- **NaN scores**: ensure feature calculations avoid division by zero.
- **Threshold filters out everything**: lower threshold or enforce minimum one chunk.

---
**Checkpoint:** If reranker output and filtered list display correctly, proceed to Video 5.

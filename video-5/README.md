# Video 5: Caching, Deduplication & Simple Retrieval Optimization

**Duration:** ~12 min

## Objective
Implement a simple caching layer for retrieval results (file-based), demonstrate cache hits/misses, and implement duplicate chunk suppression using hashing.

## Prerequisites
- Videos 1–4 completed

## Steps

1. **Inspect caching utility**:
   ```bash
   sed -n '1,20p' utils/cache.py
   # Check key format, TTL, and storage path
   ```
2. **Demonstrate cache miss**:
   ```bash
   python scripts/cached_query.py --query "Sample query"
   # Checkpoint: prints "Cache miss" and caches results
   ```
3. **Demonstrate cache hit**:
   ```bash
   python scripts/cached_query.py --query "Sample query"
   # Checkpoint: prints "Cache hit"
   ```
4. **Show deduplication**:
   ```bash
   python scripts/cached_query.py --query "Sample query with duplicates"
   # Checkpoint: prints "Removed N duplicate chunks"
   ```
5. **Cache invalidation on config change**:
   ```bash
   # Modify weights in command to demonstrate new cache key and miss
   python scripts/cached_query.py --query "Sample query" --k 5
   ```

## Common Issues & Troubleshooting
- **Cache growth**: configure TTL or clean .cache folder.
- **Duplicates persist**: ensure hashing normalizes text (strip and lower-case).

---
**Checkpoint:** If cache hit/miss and deduplication messages appear, proceed to Video 6.

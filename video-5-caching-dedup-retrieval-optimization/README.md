# Video 5: Caching, Deduplication & Simple Retrieval Optimization

**Estimated Duration:** 12 min

**Objective:**
Implement a simple caching layer for retrieval results, demonstrate cache hits and misses, and implement duplicate chunk suppression using hash-based deduplication.

## Prerequisites

- Videos 1–4 completed
- Dependencies installed (`numpy`, `pandas`)

## Steps (Reproducible Checklist)

1. Review `utils/cache.py` and understand the cache key format (query fingerprint + k).
2. Run the first query and observe a cache miss:
   ```bash
   python scripts/cached_query.py --query "X" --k 5
   ```
3. Run the same query again and observe a cache hit:
   ```bash
   python scripts/cached_query.py --query "X" --k 5
   ```
4. Force deduplication using duplicate texts:
   ```bash
   python scripts/cached_query.py --query "dup" --k 5
   ```
5. Demonstrate cache invalidation when weights change:
   ```bash
   python scripts/cached_query.py --query "X" --k 5 --weights 0.7,0.3
   ```

## Common Errors & Troubleshooting

- Cache grows unbounded: configure TTL and eviction policy.
- Deduplication misses near-duplicates: normalize text (strip, lower-case).
- Stale cache entries after index update: include index version in cache key.

## Materials

- `utils/cache.py`: file-based TTL cache logic
- `scripts/`: cached_query script and dummy retrieve module
- `notebooks/`: demo notebook
- `assets/`: latency charts and dedupe flow diagrams
- `verification_artifacts/`: expected CLI output

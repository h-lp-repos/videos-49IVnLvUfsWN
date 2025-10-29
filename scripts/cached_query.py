#!/usr/bin/env python3
"""
Query with simple caching and deduplication demo.
"""
import argparse
import time
import hashlib
from utils.cache import SimpleCache
from retrieval import retrieve


def dedupe(items):
    seen = set()
    unique = []
    for it in items:
        h = hashlib.sha256(it['text'].encode()).hexdigest()
        if h not in seen:
            seen.add(h)
            unique.append(it)
    removed = len(items) - len(unique)
    if removed > 0:
        print(f"Removed {removed} duplicate chunks")
    return unique


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--ttl', type=int, default=3600)
    args = parser.parse_args()
    cache = SimpleCache(ttl=args.ttl)
    key = f"{args.query}-{args.k}"
    results = cache.get(key)
    if results is None:
        print("Cache miss")
        start = time.time()
        items = retrieve(args.query, args.k)
        duration = time.time() - start
        print(f"Retrieved in {duration:.3f}s")
        cache.set(key, items)
        results = items
    else:
        print("Cache hit")
    unique = dedupe(results)
    for r in unique:
        print(f"[{r['score']:.4f}] {r['source_id']}:{r['chunk_id']} - {r['text']}")

if __name__ == '__main__':
    main()

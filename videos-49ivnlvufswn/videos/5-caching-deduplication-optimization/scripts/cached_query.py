import argparse
import hashlib
import time
from utils.cache import get_cache_key, load_cache, save_cache


def retrieve(query, k=5):
    # Dummy retrieval returning some duplicates
    results = []
    for i in range(k):
        text = f"Chunk content {i // 2}"  # duplicate every 2 chunks
        results.append({
            'source_id': f'source_{i}',
            'chunk_id': i,
            'score': 1.0 - i*0.1,
            'text': text
        })
    return results


def deduplicate(results):
    seen_hashes = set()
    unique = []
    for r in results:
        h = hashlib.sha256(r['text'].encode()).hexdigest()
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique.append(r)
    removed = len(results) - len(unique)
    print(f"Removed {removed} duplicate chunks")
    return unique


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    args = parser.parse_args()

    key = get_cache_key(args.query, args.k)

    cached = load_cache(key)
    if cached:
        print(f"Cache hit for query '{args.query}'")
        results = cached
    else:
        print(f"Cache miss for query '{args.query}'")
        results = retrieve(args.query, args.k)
        results = deduplicate(results)
        save_cache(key, results)

    for r in results:
        print(f"Score: {r['score']:.3f} | Source: {r['source_id']} | Chunk: {r['chunk_id']}\nText: {r['text']}\n")


if __name__ == '__main__':
    main()

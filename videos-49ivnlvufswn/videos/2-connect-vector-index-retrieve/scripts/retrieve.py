import os
import sys
import argparse

# Dummy retrieve function simulating retrieval with provenance

def retrieve(query, k=5):
    # Return dummy results with provenance fields
    results = []
    for i in range(k):
        results.append({
            'source_id': f'source_{i}',
            'chunk_id': i,
            'score': 1.0 - i*0.1,
            'text': f'Retrieved chunk {i} for query "{query}"'
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    args = parser.parse_args()

    results = retrieve(args.query, args.k)
    for r in results:
        print(f"Score: {r['score']:.3f} | Source: {r['source_id']} | Chunk: {r['chunk_id']}\nText: {r['text']}\n")


if __name__ == '__main__':
    main()

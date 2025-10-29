#!/usr/bin/env python3
"""
Smoke test for querying the sample index.
"""
import argparse
from retrieval import retrieve

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=3)
    args = parser.parse_args()
    results = retrieve(args.query, args.k)
    for r in results:
        print(f"[{r['score']:.4f}] {r['source_id']}:{r['chunk_id']} - {r['text']}")

if __name__ == '__main__':
    main()

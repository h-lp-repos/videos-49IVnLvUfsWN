#!/usr/bin/env python3
"""
CLI for retrieval module.
"""
import argparse
from retrieval import retrieve

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    args = parser.parse_args()
    items = retrieve(args.query, args.k)
    for it in items:
        print(f"[{it['score']:.4f}] {it['source_id']}:{it['chunk_id']} - {it['text']}")

if __name__ == '__main__':
    main()

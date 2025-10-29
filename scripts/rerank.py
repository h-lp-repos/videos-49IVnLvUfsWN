#!/usr/bin/env python3
"""
CLI for reranking retrieved chunks.
"""
import argparse
from reranker import rerank_items
from retrieval import retrieve


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=10)
    parser.add_argument('--weights', type=str, default='0.8,0.2')
    parser.add_argument('--threshold', type=float, default=None)
    args = parser.parse_args()
    w = tuple(map(float, args.weights.split(',')))
    items = retrieve(args.query, args.k)
    out = rerank_items(items, w, args.threshold)
    for it in out:
        print(f"[{it['combined_score']:.4f}] {it['source_id']}:{it['chunk_id']} - {it['text']}")

if __name__ == '__main__':
    main()

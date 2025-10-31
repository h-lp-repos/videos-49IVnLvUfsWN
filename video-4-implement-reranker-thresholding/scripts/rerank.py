#!/usr/bin/env python3
"""
CLI script for reranking and thresholding.
"""
import argparse
from rerank_module import rerank
from retrieve_module import retrieve

def main():
    parser = argparse.ArgumentParser(description='Relevance reranker CLI')
    parser.add_argument('--query', required=True, help='Query text')
    parser.add_argument('--k', type=int, default=10, help='Number of chunks to retrieve')
    parser.add_argument('--weights', default='0.8,0.2', help='Weights w_sim,w_feat')
    parser.add_argument('--threshold', type=float, default=None, help='Relevance threshold')
    args = parser.parse_args()
    w_sim, w_feat = map(float, args.weights.split(','))
    res = retrieve(args.query, args.k)
    ranked = rerank(res, weights=(w_sim, w_feat), threshold=args.threshold)
    print('Reranked results:')
    for r in ranked:
        print(r)

if __name__ == '__main__':
    main()

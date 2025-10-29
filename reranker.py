"""
Relevance reranker and threshold filter.
"""
import argparse
from retrieval import retrieve


def combine(score, feature, weights=(0.8, 0.2)):
    return score * weights[0] + feature * weights[1]


def rerank_items(items, weights, threshold=None):
    reranked = []
    for it in items:
        feat = len(it['text']) / 100.0
        combined = combine(it['score'], feat, weights)
        reranked.append({**it, 'combined_score': combined})
    reranked.sort(key=lambda x: x['combined_score'], reverse=True)
    if threshold is not None:
        filtered = [it for it in reranked if it['combined_score'] >= threshold]
        return filtered
    return reranked

if __name__ == '__main__':
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

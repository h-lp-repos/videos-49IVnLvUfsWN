import argparse


def combine_scores(score, recency, length, weight_score=0.8, weight_recency=0.2):
    return weight_score * score + weight_recency * recency


def rerank(results, weights=(0.8, 0.2), threshold=0.0):
    weight_score, weight_recency = weights
    reranked = []
    for r in results:
        combined = combine_scores(r['score'], r.get('recency', 0.5), len(r.get('text', '')), weight_score, weight_recency)
        if combined >= threshold:
            r['combined_score'] = combined
            reranked.append(r)
    reranked.sort(key=lambda x: x['combined_score'], reverse=True)
    return reranked


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=10)
    parser.add_argument('--weights', type=str, default='0.8,0.2')
    parser.add_argument('--threshold', type=float, default=0.0)
    args = parser.parse_args()

    # Dummy results
    results = []
    for i in range(args.k):
        results.append({
            'source_id': f'source_{i}',
            'chunk_id': i,
            'score': 1.0 - i*0.05,
            'recency': 1.0 - i*0.1,
            'text': f'Retrieved chunk {i} for query "{args.query}"'
        })

    weights = tuple(map(float, args.weights.split(',')))
    reranked = rerank(results, weights, args.threshold)

    for r in reranked:
        print(f"Combined Score: {r['combined_score']:.3f} | Source: {r['source_id']} | Chunk: {r['chunk_id']}\nText: {r['text']}\n")


if __name__ == '__main__':
    main()

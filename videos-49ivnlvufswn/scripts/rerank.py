#!/usr/bin/env python3
import argparse
from scripts.retrieve import retrieve


def combined_score(item, weights=(0.8,0.2)):
    sim = item['score']
    length = len(item['text'].split())
    # normalize length into 0..1 by simple heuristic
    length_score = min(1.0, length/100.0)
    return weights[0]*sim + weights[1]*length_score

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--k', type=int, default=10)
    p.add_argument('--weights', default='0.8,0.2')
    p.add_argument('--threshold', type=float, default=0.0)
    args = p.parse_args()
    w = tuple(float(x) for x in args.weights.split(','))
    items = retrieve(args.query, args.k)
    for it in items:
        it['combined'] = combined_score(it, weights=w)
    items.sort(key=lambda x: x['combined'], reverse=True)
    filtered = [i for i in items if i['combined'] >= args.threshold]
    if len(filtered) == 0 and len(items)>0:
        filtered = [items[0]]
    print('Reranked results:')
    for i,it in enumerate(filtered):
        print(f"{i+1}. combined={it['combined']:.4f} sim={it['score']:.4f} len={len(it['text'].split())} source={it['source_id']}:{it['chunk_id']}")


#!/usr/bin/env python3
import argparse
from utils.index import get_dim, query_index
import hashlib


def query_to_vector(q, dim):
    import hashlib
    h = hashlib.md5(q.encode('utf-8')).digest()
    vec = [((b % 100)/100.0) for b in h[:dim]]
    if len(vec) < dim:
        vec = (vec * ((dim//len(vec))+1))[:dim]
    return vec


def retrieve(query, k=3):
    dim = get_dim()
    qv = query_to_vector(query, dim)
    res = query_index(qv, k=k)
    # ensure provenance keys
    out = []
    for r in res:
        out.append({
            'source_id': r['source_id'],
            'chunk_id': r['chunk_id'],
            'score': r['score'],
            'text': r['text']
        })
    return out

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--k', type=int, default=3)
    args = p.parse_args()
    for i,r in enumerate(retrieve(args.query, args.k)):
        print(f"{i+1}. score={r['score']:.4f} source={r['source_id']}:{r['chunk_id']}\n   {r['text']}")


#!/usr/bin/env python3
import argparse
import hashlib
from utils.index import query_index, get_dim


def query_to_vector(q, dim):
    # deterministic pseudo-embedding based on md5
    h = hashlib.md5(q.encode('utf-8')).digest()
    vec = [((b % 100)/100.0) for b in h[:dim]]
    # if dim > len(h) repeat
    if len(vec) < dim:
        vec = (vec * ((dim//len(vec))+1))[:dim]
    return vec

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--k', type=int, default=3)
    args = p.parse_args()
    dim = get_dim()
    qv = query_to_vector(args.query, dim)
    res = query_index(qv, k=args.k)
    for i,r in enumerate(res):
        print(f"Result {i+1}: score={r['score']:.4f} source_id={r['source_id']} chunk_id={r['chunk_id']}\n  text={r['text']}")


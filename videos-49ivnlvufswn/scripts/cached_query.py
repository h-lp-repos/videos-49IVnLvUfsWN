#!/usr/bin/env python3
import argparse
import hashlib
from utils.cache import get, set
from scripts.retrieve import retrieve


def key_for(query,k,version=1):
    h = hashlib.md5(f"{version}|{k}|{query}".encode('utf-8')).hexdigest()
    return h

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--k', type=int, default=5)
    p.add_argument('--ttl', type=int, default=3600)
    args = p.parse_args()
    key = key_for(args.query, args.k)
    cached = get(key)
    if cached:
        print('cache hit')
        for i,r in enumerate(cached):
            print(f"{i+1}. {r['source_id']}:{r['chunk_id']} score={r['score']:.4f}")
    else:
        print('cache miss')
        res = retrieve(args.query, args.k)
        set(key, res, ttl=args.ttl)
        for i,r in enumerate(res):
            print(f"{i+1}. {r['source_id']}:{r['chunk_id']} score={r['score']:.4f}")


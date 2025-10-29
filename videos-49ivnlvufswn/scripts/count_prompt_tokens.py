#!/usr/bin/env python3
import argparse
from utils.token_utils import count_tokens
from scripts.retrieve import retrieve

TEMPLATE = """
User question: {user_query}

Context:
{retrieved}

Answer:
"""

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--query', required=True)
    p.add_argument('--k', type=int, default=5)
    p.add_argument('--budget', type=int, default=2048)
    args = p.parse_args()
    chunks = retrieve(args.query, args.k)
    per = []
    for c in chunks:
        t = c['text']
        tokens = count_tokens(t)
        per.append((c, tokens))
    total = 0
    assembled = ''
    included = []
    # include highest scored first
    for c,tokens in per:
        if total + tokens <= args.budget:
            assembled += '\n' + c['text']
            total += tokens
            included.append(c)
    print(f'Total tokens: {total} (budget {args.budget})')
    for i,(c,tokens) in enumerate(per):
        print(f"Chunk {i+1}: tokens={tokens} score={c['score']:.4f} source={c['source_id']}:{c['chunk_id']}")
    if len(included) < len(per):
        print(f'Truncated to {len(included)} chunks to meet budget')
    print('\nConstructed prompt:')
    print(TEMPLATE.format(user_query=args.query, retrieved='\n'.join([c['text'] for c in included])))


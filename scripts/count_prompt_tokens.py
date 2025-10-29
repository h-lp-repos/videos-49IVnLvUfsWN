#!/usr/bin/env python3
"""
Count tokens for constructed prompt and demo truncation.
"""
import argparse
from prompt_constructor import count_tokens, construct_prompt
from retrieval import retrieve


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--budget', type=int, default=2048)
    args = parser.parse_args()
    chunks = retrieve(args.query, args.k)
    prompt = construct_prompt(args.query, chunks, args.budget)
    tokens = count_tokens(prompt)
    print(f"Total tokens: {tokens}")

if __name__ == '__main__':
    main()

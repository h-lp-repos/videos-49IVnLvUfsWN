#!/usr/bin/env python3
"""
Cuenta tokens del prompt y muestra totales y truncado.
"""
import argparse
from prompt_constructor import construct_prompt

def main():
    parser = argparse.ArgumentParser(description='Contar tokens del prompt')
    parser.add_argument('--query', required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--budget', type=int, default=2048)
    parser.add_argument('--template', required=True, help='Ruta a la plantilla de prompt')
    args = parser.parse_args()
    # chunks de ejemplo
    chunks = [{'source_id': f'doc{i}', 'chunk_id': i, 'text': f'Sample chunk text {i}'} for i in range(args.k)]
    prompt, total, truncated, k_used = construct_prompt(args.query, chunks, args.budget, args.template)
    print(f"Total tokens: {total}")
    if truncated:
        print(f"Truncated to {k_used} chunks to meet budget {args.budget}")
    print(prompt)

if __name__ == '__main__':
    main()

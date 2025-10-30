#!/usr/bin/env python3
"""
Construye prompt y simula llamada al LLM stub.
"""
import argparse
from prompt_constructor import construct_prompt

def call_stub(prompt):
    return "[LLM-STUB RESPONSE] El resultado simulado del stub basado en el prompt."

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Construye prompt y llama stub')
    parser.add_argument('--query', required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--budget', type=int, default=2048)
    parser.add_argument('--template', required=True)
    args = parser.parse_args()
    chunks = [{'source_id': f'doc{i}', 'chunk_id': i, 'text': f'Sample chunk text {i}'} for i in range(args.k)]
    prompt, total, truncated, k_used = construct_prompt(args.query, chunks, args.budget, args.template)
    print("Constructed Prompt:\n", prompt)
    response = call_stub(prompt)
    print("LLM Stub Response:\n", response)

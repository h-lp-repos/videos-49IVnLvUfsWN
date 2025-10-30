#!/usr/bin/env python3
"""
Módulo para construir prompt con control de presupuesto de tokens.
"""
import tiktoken

def load_template(path):
    with open(path, 'r') as f:
        return f.read()

def count_tokens(text, model='gpt2'):
    enc = tiktoken.get_encoding(model)
    return len(enc.encode(text))

def construct_prompt(query, chunks, budget, template_path):
    template = load_template(template_path)
    # ensamblar textos
    bodies = ''.join([ch['text'] + '\n' for ch in chunks])
    prov = ''.join([f"{ch['source_id']}|{ch['chunk_id']}\n" for ch in chunks])
    prompt = template.format(user_query=query, retrieved_chunks=bodies, provenance=prov)
    total = count_tokens(prompt)
    truncated = False
    if total > budget:
        # truncar a primeras 3 chunks
        chunks = chunks[:3]
        bodies = ''.join([ch['text'] + '\n' for ch in chunks])
        prov = ''.join([f"{ch['source_id']}|{ch['chunk_id']}\n" for ch in chunks])
        prompt = template.format(user_query=query, retrieved_chunks=bodies, provenance=prov)
        total = count_tokens(prompt)
        truncated = True
    return prompt, total, truncated, len(chunks)

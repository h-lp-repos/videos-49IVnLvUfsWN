#!/usr/bin/env python3
from utils.index import load_embeddings

if __name__ == '__main__':
    emb = load_embeddings()
    print(f'Loaded index with {len(emb)} vectors')


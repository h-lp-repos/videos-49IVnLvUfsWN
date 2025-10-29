#!/usr/bin/env python3
"""
Load sample FAISS index from sample_corpus.json and save index and metadata.
"""
import json
import numpy as np
import faiss
from embeddings import get_embeddings, get_dim

def main():
    with open('data/sample_corpus.json', 'r') as f:
        corpus = json.load(f)
    texts = [item['text'] for item in corpus]
    embeddings = get_embeddings(texts)
    dim = embeddings.shape[1] if embeddings.ndim == 2 else get_dim()
    index = faiss.IndexFlatIP(dim)
    faiss.normalize_L2(np.array(embeddings, dtype='float32'))
    index.add(np.array(embeddings, dtype='float32'))
    faiss.write_index(index, 'data/sample_index.faiss')
    with open('data/sample_metadata.json', 'w') as f:
        json.dump(corpus, f, indent=2)
    print(f"Loaded index with {index.ntotal} vectors and saved to data/sample_index.faiss")

if __name__ == '__main__':
    main()

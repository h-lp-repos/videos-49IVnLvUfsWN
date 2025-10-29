"""
Retrieval module: query FAISS index and return top-K chunks with provenance.
"""
import faiss
import numpy as np
import json
from embeddings import get_embeddings

_INDEX = None
_METADATA = None


def load_index(index_path='data/sample_index.faiss', metadata_path='data/sample_metadata.json'):
    global _INDEX, _METADATA
    if _INDEX is None:
        _INDEX = faiss.read_index(index_path)
    if _METADATA is None:
        with open(metadata_path, 'r') as f:
            _METADATA = json.load(f)
    return _INDEX, _METADATA


def retrieve(query, k=5):
    index, metadata = load_index()
    emb = get_embeddings([query])
    D, I = index.search(np.array(emb).astype('float32'), k)
    results = []
    for score, idx in zip(D[0], I[0]):
        if idx < 0 or idx >= len(metadata):
            continue
        meta = metadata[idx]
        results.append({
            'source_id': meta['source_id'],
            'chunk_id': meta['chunk_id'],
            'score': float(score),
            'text': meta['text']
        })
    return results

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=3)
    args = parser.parse_args()
    results = retrieve(args.query, args.k)
    for r in results:
        print(f"[{r['score']:.4f}] {r['source_id']}:{r['chunk_id']} - {r['text']}")

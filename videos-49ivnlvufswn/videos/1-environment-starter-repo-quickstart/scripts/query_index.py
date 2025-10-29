import os
import sys
import argparse
import faiss

INDEX_PATH = os.getenv('FAISS_INDEX_PATH', 'data/sample_faiss.index')


def load_index(path=INDEX_PATH):
    if not os.path.exists(path):
        print(f"Index file not found at {path}")
        return None
    with open(path, 'rb') as f:
        index = faiss.read_index(f.read())
    return index


def query_index(index, query, k=3):
    # Dummy implementation: return k dummy results
    # Replace with actual retrieval logic
    results = []
    for i in range(k):
        results.append({
            'source_id': f'source_{i}',
            'chunk_id': i,
            'score': 0.9 - i*0.1,
            'text': f'Result chunk {i} for query "{query}"'
        })
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=3)
    args = parser.parse_args()

    index = load_index()
    if index is None:
        print("Cannot query without index.")
        sys.exit(1)

    results = query_index(index, args.query, args.k)
    for r in results:
        print(f"Score: {r['score']:.3f} | Source: {r['source_id']} | Chunk: {r['chunk_id']}\nText: {r['text']}\n")


if __name__ == '__main__':
    main()

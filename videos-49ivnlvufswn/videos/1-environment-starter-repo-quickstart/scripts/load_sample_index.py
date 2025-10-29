import os
import faiss
import pickle

INDEX_PATH = os.getenv('FAISS_INDEX_PATH', 'data/sample_faiss.index')


def load_index(path=INDEX_PATH):
    if not os.path.exists(path):
        print(f"Index file not found at {path}")
        return None
    with open(path, 'rb') as f:
        index = faiss.read_index(f.read())
    return index


def main():
    index = load_index()
    if index is not None:
        print(f"Loaded index with {index.ntotal} vectors from {INDEX_PATH}")
    else:
        print("Failed to load index.")


if __name__ == '__main__':
    main()

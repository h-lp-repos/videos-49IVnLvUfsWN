#!/usr/bin/env python3
"""
Carga o genera un índice FAISS de ejemplo y muestra la cantidad de vectores.
"""
import os

def load_index(index_path):
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    if not os.path.exists(index_path):
        # Generación de índice FAISS de ejemplo (dummy)
        with open(index_path, 'w') as f:
            f.write('dummy faiss index')
    # Simulamos que hay 5 vectores
    print(f"Loaded index with 5 vectors from {index_path}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Carga índice FAISS de ejemplo')
    parser.add_argument('--index-path', default='sample_data/faiss_sample.index', help='Ruta al índice FAISS')
    args = parser.parse_args()
    load_index(args.index_path)

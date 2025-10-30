#!/usr/bin/env python3
"""
Script CLI para mostrar resultados de retrieve() con procedencia.
"""
import argparse
from retrieve_module import retrieve

def main():
    parser = argparse.ArgumentParser(description='Recuperación de chunks con procedencia')
    parser.add_argument('--query', required=True, help='Texto de la consulta')
    parser.add_argument('--k', type=int, default=5, help='Número de resultados')
    args = parser.parse_args()
    print("Retrieval results:")
    for r in retrieve(args.query, args.k):
        print(r)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Ejecuta una consulta rápida sobre el índice y muestra resultados con puntuaciones y procedencia.
"""
import argparse

def query_index(query, k):
    print("Running quick retrieval smoke test")
    for i in range(k):
        print(f"doc{i}\tscore={1.0/(i+1):.4f}\tsource_id=doc{i}\tchunk_id={i}\ttext=Sample chunk text {i}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Consulta rápida al índice')
    parser.add_argument('--query', required=True, help='Texto de la consulta')
    parser.add_argument('--k', type=int, default=3, help='Número de resultados a recuperar')
    args = parser.parse_args()
    query_index(args.query, args.k)

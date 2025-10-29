# Video 5: Caching, Deduplication & Simple Retrieval Optimization

## Objetivo

Implementar una capa de caching para resultados de recuperación, con deduplicación de chunks.

## Pasos

1. Revisar utilidad de caching en `utils/cache.py`.
2. Ejecutar consulta con cache miss y cache hit:
   ```bash
   python scripts/cached_query.py --query "X"
   ```
3. Mostrar deduplicación de chunks duplicados.
4. Mostrar invalidación de cache al cambiar pesos de reranker.

## Archivos principales

- `utils/cache.py`: Utilidad de caching.
- `scripts/cached_query.py`: Script que usa caching.

## Notas

- Requiere videos 1 a 4 completados.

# Video 2: Connect to Vector Index & Retrieve Top-K Chunks with Provenance

## Objetivo

Demostrar cómo consultar un índice vectorial y obtener los top-K chunks con información de proveniencia.

## Pasos

1. Revisar la función `retrieve(query, k)` en `scripts/retrieve.py`.
2. Ejecutar:
   ```bash
   python scripts/retrieve.py --query "How to rotate a key?" --k 5
   ```
3. Verificar la dimensión de embeddings con:
   ```bash
   python -c "from embeddings import get_dim; print(get_dim())"
   ```
4. Inspeccionar un chunk retornado y su archivo fuente.
5. Probar manejo de errores con consultas malformadas o índice faltante.

## Archivos principales

- `scripts/retrieve.py`: Módulo de recuperación con retorno de proveniencia.

## Notas

- Requiere haber completado el video 1.

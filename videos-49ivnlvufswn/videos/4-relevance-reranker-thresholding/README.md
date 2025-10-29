# Video 4: Implement Relevance Reranker & Thresholding

## Objetivo

Implementar un reranker de relevancia que reordene y filtre chunks según un umbral configurable.

## Pasos

1. Revisar la función de scoring en `scripts/rerank.py`.
2. Ejecutar rerank con pesos configurables:
   ```bash
   python scripts/rerank.py --query "X" --k 10 --weights "0.8,0.2"
   ```
3. Aplicar umbral con `--threshold` y observar resultados filtrados.
4. Integrar salida rerankeada en construcción de prompt.
5. Experimentar con umbral y observar cambios.

## Archivos principales

- `scripts/rerank.py`: Script para reranking y filtrado.

## Notas

- Requiere video 2 completado.

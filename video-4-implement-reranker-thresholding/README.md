# Video 4: Implementación de Relevance Reranker y Thresholding

**Duración estimada:** 12 min

**Objetivo:**
Implementar y demostrar un reranker de relevancia que reordena top-K por score combinado y aplica umbral configurable.

## Requisitos previos

- Video 2 completado
- Entorno con dependencias instaladas (`numpy`, `pandas`)

## Pasos (checklist reproducible)

1. Abrir `scripts/rerank_module.py` y revisar función `combine` y `rerank`.
2. Ejecutar rerank en resultados simulados:
   ```bash
   python scripts/rerank.py --query "X" --k 10 --weights 0.8,0.2
   ```
3. Aplicar umbral:
   ```bash
   python scripts/rerank.py --query "X" --k 10 --weights 0.8,0.2 --threshold 0.35
   ```
4. Mostrar cómo el rerank se integra con prompt constructor.
5. Experimentar con distinto threshold y observar cambios.

## Errores comunes y soluciones

Consulte `tech_notes.md`.

## Materiales incluidos

- `scripts/`: Módulo de reranking y script CLI.
- `notebooks/`: Notebook de ejemplo.
- `verification_artifacts/`: Salida esperada.
- `assets/`: Capturas y gráficos.


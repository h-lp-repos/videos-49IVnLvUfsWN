# Video 6: Demo End-to-End, Micro-benchmark y Modos de Falla

**Duración estimada:** 15 min

**Objetivo:**
Ejecutar el pipeline completo de RAG para 5 consultas de ejemplo, mostrar micro-benchmarks (p50/p95) y reproducir modos de falla con sus mitigaciones.

## Requisitos previos

- Videos 1–5 completados
- Dependencias instaladas (`numpy`, `pandas`)

## Pasos (checklist reproducible)

1. Ejecutar benchmark:
   ```bash
   python scripts/benchmark.py --queries sample_queries.json --runs 5
   ```
2. Observar logs step-level y resumen p50/p95.
3. Reproducir modo de falla de contexto (prompt muy grande) y aplicar truncado.
4. Reproducir duplicación/hallucination y aplicar dedupe + grounding.
5. Verificar que `benchmark_results.json` se haya generado.

## Errores comunes y soluciones

Consulte `tech_notes.md`.

## Materiales incluidos

- `scripts/benchmark.py`: Runner de benchmark end-to-end.
- `sample_queries.json`: Consultas de ejemplo.
- `templates/`: Plantilla de prompt usada.
- `notebooks/`: Notebook de análisis de benchmarks.
- `verification_artifacts/`: Resultados ejemplo.
- `assets/`: Gráficos de latencias y fallas.


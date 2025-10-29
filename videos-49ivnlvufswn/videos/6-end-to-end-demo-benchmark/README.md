# Video 6: End-to-End Demo & Benchmark

## Objetivo

Ejecutar la pipeline completa RAG para 5 consultas de ejemplo, capturar micro-benchmarks y reproducir modos de fallo.

## Pasos

1. Ejecutar benchmark con:
   ```bash
   python scripts/benchmark.py --queries sample_queries.json --runs 5
   ```
2. Observar logs de tiempos por etapa.
3. Ver resultados agregados p50/p95.
4. Reproducir modos de fallo y mitigaciones.
5. Guardar logs en `scripts/benchmark_results.json`.

## Archivos principales

- `scripts/benchmark.py`: Script para benchmarking.
- `scripts/sample_queries.json`: Archivo con 5 consultas de ejemplo.

## Notas

- Requiere todos los videos anteriores completados.

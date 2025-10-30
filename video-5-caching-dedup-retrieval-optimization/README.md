# Video 5: Caching, Deduplicación y Optimización de Recuperación

**Duración estimada:** 12 min

**Objetivo:**
Implementar una capa de caching para resultados de recuperación, demostrar hits/misses, y aplicar deduplicación de chunks.

## Requisitos previos

- Videos 1–4 completados
- Dependencias instaladas (`numpy`, `pandas`)

## Pasos (checklist reproducible)

1. Revisar `utils/cache.py` y entender formato de key (query fingerprint + k).
2. Ejecutar primer query y observar cache miss:
   ```bash
   python scripts/cached_query.py --query "X" --k 5
   ```
3. Ejecutar de nuevo y observar cache hit:
   ```bash
   python scripts/cached_query.py --query "X" --k 5
   ```
4. Forzar deduplicación con textos duplicados:
   ```bash
   python scripts/cached_query.py --query "dup" --k 5
   ```
5. Mostrar invalidación de cache al cambiar weights:
   ```bash
   python scripts/cached_query.py --query "X" --k 5 --weights 0.7,0.3
   ```

## Errores comunes y soluciones

Consulte `tech_notes.md`.

## Materiales incluidos

- `utils/cache.py`: Lógica de cache TTL file-based.
- `scripts/`: Script de consulta cacheada y módulo dummy de retrieve.
- `notebooks/`: Notebook de demostración.
- `verification_artifacts/`: Salida esperada.
- `assets/`: Capturas y gráficos de latencia.


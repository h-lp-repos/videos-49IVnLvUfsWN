# Video 2: Conexión al Índice de Vectores y Recuperación Top-K con Procedencia

**Duración estimada:** 12 min

**Objetivo:**
Demostrar cómo usar el módulo de recuperación para consultar un índice FAISS y mostrar los top-K chunks con datos de procedencia (source_id, chunk_id, score).

## Requisitos previos

- Video 1 completado (índice cargado)
- Entorno virtual activado con dependencias instaladas

## Pasos (checklist reproducible)

1. Abrir el módulo de recuperación y revisar la función `retrieve(query, k)` y sus campos de retorno.
2. Ejecutar:
   ```bash
   python scripts/retrieve.py --query "How to rotate a key?" --k 5
   ```
3. Verificar la dimensión de embeddings vs índice:
   ```bash
   python -c "from embeddings import get_dim; print(get_dim())"
   ```
4. Inspeccionar la procedencia de un chunk devuelto.
5. Probar manejo de errores con query malformada o índice faltante.

## Errores comunes y soluciones

Consulte `tech_notes.md`.

## Materiales incluidos

- `scripts/`: Módulo y script de recuperación.
- `sample_data/`: Chunked corpus de ejemplo y metadatos.
- `notebooks/`: Notebook de demostración.
- `verification_artifacts/`: Salida esperada.
- `assets/`: Diagrama de flujo y capturas.


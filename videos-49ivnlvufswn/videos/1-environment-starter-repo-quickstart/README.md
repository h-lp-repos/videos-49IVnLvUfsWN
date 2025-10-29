# Video 1: Environment & Starter Repo Quickstart

## Objetivo

Configurar un entorno local funcional y un repositorio inicial con dependencias instaladas y un índice FAISS de ejemplo cargado.

## Pasos

1. Clonar el repositorio starter y abrir la raíz del proyecto.
2. Crear un entorno virtual y ejecutar:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar variables de entorno:
   - `API_KEY` o
   - `RAG_LLM_MODE=sandbox`
4. Ejecutar el script para cargar el índice FAISS:
   ```bash
   python scripts/load_sample_index.py
   ```
5. Ejecutar una prueba rápida de recuperación:
   ```bash
   python scripts/query_index.py --query "test" --k 3
   ```

## Archivos principales

- `requirements.txt`: Dependencias Python necesarias.
- `scripts/load_sample_index.py`: Script para cargar el índice FAISS.
- `scripts/query_index.py`: Script para realizar consultas rápidas al índice.

## Notas

- Se recomienda usar macOS/Linux/WSL para compatibilidad.
- En caso de error en dependencias, probar con `faiss-cpu`.

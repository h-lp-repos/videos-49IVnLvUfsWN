# Video 1: Configuración de Entorno y Repositorio Starter

**Duración estimada:** 12 min

**Objetivo:**
Obtener un entorno local funcional y un repositorio de inicio que cargue un índice FAISS de ejemplo.

## Requisitos previos

- Python >= 3.8
- Git
- Terminal de línea de comandos
- Acceso al repositorio (clone URL)

## Pasos (checklist reproducible)

1. Clonar el repositorio y moverse al directorio principal:
   ```bash
   git clone <repo_url>
   cd videos-49IVnLvUfsWN
   ```
2. Crear y activar un entorno virtual, luego instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Configurar variables de entorno (API_KEY o modo sandbox):
   ```bash
   export API_KEY=tu_api_key
   # o bien:
   export RAG_LLM_MODE=sandbox
   ```
4. Cargar el índice FAISS de ejemplo:
   ```bash
   python scripts/load_sample_index.py --index-path sample_data/faiss_sample.index
   ```
5. Ejecutar prueba rápida de recuperación:
   ```bash
   python scripts/query_index.py --query "test" --k 3
   ```

## Errores comunes y soluciones

Consulte `tech_notes.md` para detalles de troubleshooting.

## Materiales incluidos

- `scripts/`: Scripts de carga y consulta de índice.
- `sample_data/`: Chunked corpus y archivo de índice FAISS.
- `notebooks/`: Notebook de ejemplo (opcional).
- `verification_artifacts/`: Salida esperada de los scripts.
- `assets/`: Imágenes y diagramas para la grabación.


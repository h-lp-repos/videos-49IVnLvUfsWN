# Video 3: Construcción de Prompt y Control de Presupuesto de Tokens

**Duración estimada:** 15 min

**Objetivo:**
Ensamblar top-K chunks en un prompt con plantilla, medir tokens con tiktoken y aplicar estrategias de truncado para mantenerse dentro de un presupuesto.

## Requisitos previos

- Videos 1 y 2 completados
- Dependencias instaladas (tiktoken)

## Pasos (checklist reproducible)

1. Abrir `templates/prompt_template.txt` y revisar placeholders (`{user_query}`, `{retrieved_chunks}`, `{provenance}`).
2. Ejecutar contador de tokens:
   ```bash
   python scripts/count_prompt_tokens.py --query "X" --k 5 --budget 2048 --template templates/prompt_template.txt
   ```
3. Observar salida de tokens totales y contribución por chunk.
4. Demostrar truncado hasta cumplir presupuesto y mensaje "Truncated to K' chunks to meet budget".
5. Enviar prompt al stub de LLM:
   ```bash
   python scripts/construct_and_call_stub.py --query "X" --k 5
   ```

## Errores comunes y soluciones

Consulte `tech_notes.md`.

## Materiales incluidos

- `scripts/`: Módulo de construcción de prompt y scripts de conteo/envío.
- `templates/`: Plantilla de prompt.
- `notebooks/`: Notebook opcional de demostración.
- `verification_artifacts/`: Salida esperada de conteo y truncado.
- `assets/`: Diagramas y capturas.


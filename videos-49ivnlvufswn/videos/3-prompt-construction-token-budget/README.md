# Video 3: Prompt Construction & Token-Budget Enforcement

## Objetivo

Enseñar a construir prompts con un presupuesto de tokens usando la librería tiktoken.

## Pasos

1. Revisar el módulo `scripts/count_prompt_tokens.py`.
2. Ejecutar conteo de tokens con:
   ```bash
   python scripts/count_prompt_tokens.py --query "X" --k 5
   ```
3. Mostrar truncamiento para ajustarse al presupuesto.
4. Mostrar fallback con solo punteros de proveniencia.
5. Ejecutar prompt construido en sandbox LLM stub.

## Archivos principales

- `scripts/count_prompt_tokens.py`: Script para contar tokens y construir prompt.
- `templates/prompt_template.txt`: Plantilla de prompt con placeholders.

## Notas

- Requiere videos 1 y 2 completados.

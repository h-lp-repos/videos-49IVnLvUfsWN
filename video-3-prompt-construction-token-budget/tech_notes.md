# Notas Técnicas y Troubleshooting Video 3

## Errores comunes

- **Conteo de tokens inconsistentes**: Asegurarse de usar el mismo modelo/tokenizer que el LLM de destino.
- **Truncado excesivo**: Agregar fallback de procedencia para chunks recortados.
- **Placeholders literales**: Verificar llamada a `.format()` con las claves correctas.


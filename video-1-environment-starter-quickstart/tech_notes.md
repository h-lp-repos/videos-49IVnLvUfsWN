# Notas Técnicas y Troubleshooting

## Errores comunes

- **Dependencia faltante**: Error de pip install de faiss-cpu. Solución: usar faiss-cpu compatible con la plataforma.
- **Variables de entorno no detectadas**: $API_KEY vacío. Solución: exportar y re-source el terminal.
- **Mismatch de dimensiones**: Dimensión del índice no coincide. Solución: verificar chunk metadata o regenerar índice.


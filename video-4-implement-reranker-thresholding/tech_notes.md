# Technical Notes & Troubleshooting - Video 4

## Common Errors

- **NaN in combined_score**: sanitize inputs or fallback to similarity score.
- **Threshold removes all**: adjust threshold or fallback to at least one chunk.
- **Schema mismatch**: verify chunk dict keys match prompt constructor expectations.

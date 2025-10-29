# Video 3: Prompt Construction & Token-Budget Enforcement (tiktoken demo)

**Duration:** ~15 min

## Objective
Show how to assemble top-K retrieved chunks into a grounded prompt template, measure tokens with tiktoken, and apply truncation or provenance-only fallback strategies to stay within a token budget.

## Prerequisites
- Videos 1 & 2 completed
- tiktoken installed (requirements.txt)
- templates/prompt_template.txt present

## Steps

1. **Inspect prompt template**:
   ```bash
   sed -n '1,20p' templates/prompt_template.txt
   ```
2. **Count tokens for full chunks**:
   ```bash
   python scripts/count_prompt_tokens.py --query "Sample query" --k 5 --budget 2048
   # Checkpoint: prints total tokens and no truncation
   ```
3. **Demonstrate truncation to meet budget**:
   ```bash
   python scripts/count_prompt_tokens.py --query "Sample query" --k 5 --budget 20
   # Checkpoint: prints "Truncated to K'=... chunks to meet budget"
   ```
4. **Show provenance-only fallback**:
   ```bash
   # Modify budget very small to force fallback
   python scripts/count_prompt_tokens.py --query "Sample query" --k 5 --budget 10
   # Checkpoint: prompt uses provenance pointers instead of chunk bodies
   ```
5. **Send prompt to sandbox LLM stub**:
   ```bash
   python prompt_constructor.py --query "Sample query" --k 3 --budget 50
   # Checkpoint: prints LLM response from sandbox stub
   ```

## Common Issues & Troubleshooting
- **Budget too low**: implement provenance-only fallback to reduce token count.
- **Template placeholders unresolved**: ensure correct replace markers (`{{...}}`).

---
**Checkpoint:** If prompt is printed with token count and sandbox stub response, you're ready for Video 4.

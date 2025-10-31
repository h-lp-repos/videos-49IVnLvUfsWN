# Video 3: Prompt Construction & Token-Budget Enforcement

**Estimated Duration:** 15 min

**Objective:**
Assemble top-K retrieved chunks into a grounded prompt template, measure tokens with tiktoken (or the provided helper), and apply truncation/selection strategies to stay within a target token budget.

## Prerequisites

- Videos 1 and 2 completed
- Dependencies installed (`tiktoken`)

## Steps (Reproducible Checklist)

1. Open `templates/prompt_template.txt` and review placeholders (`{user_query}`, `{retrieved_chunks}`, `{provenance}`).
2. Run the token counter:
   ```bash
   python scripts/count_prompt_tokens.py --query "X" --k 5 --budget 2048 --template templates/prompt_template.txt
   ```
3. Observe total tokens and per-chunk contribution.
4. Demonstrate truncation strategy and print "Truncated to 3 chunks to meet budget 2048".
5. Send the constructed prompt to the LLM stub:
   ```bash
   python scripts/construct_and_call_stub.py --query "X" --k 5 --template templates/prompt_template.txt
   ```

## Common Errors & Troubleshooting

- Inconsistent token counts: ensure using the same tokenizer as the target LLM.
- Over-truncation: implement a provenance-only fallback when chunks are dropped.
- Literal placeholders in output: confirm `.format()` keys match the template.

## Materials

- `scripts/`: prompt constructor module and counting/calling scripts
- `templates/`: prompt template
- `notebooks/`: optional demo notebook
- `assets/`: diagrams and screenshots
- `verification_artifacts/`: expected token count, truncation, and stub output

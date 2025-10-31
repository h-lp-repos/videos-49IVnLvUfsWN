# Video 6: End-to-End Demo, Micro-benchmark & Failure Modes

**Estimated Duration:** 15 min

**Objective:**
Run the full RAG pipeline for 5 sample queries, capture micro-benchmark results (p50/p95 latencies), and reproduce failure modes with mitigation strategies.

## Prerequisites

- Videos 1–5 completed
- Dependencies installed (`numpy`, `pandas`)

## Steps (Reproducible Checklist)

1. Run the benchmark:
   ```bash
   python scripts/benchmark.py --queries sample_queries.json --runs 5
   ```
2. Observe step-level logs and the p50/p95 summary.
3. Reproduce a context-window failure (oversized prompt) and apply truncation mitigation.
4. Reproduce duplication/hallucination failure and apply dedupe + grounding mitigation.
5. Verify that `benchmark_results.json` was generated.

## Common Errors & Troubleshooting

- LLM call timeouts: adjust timeout settings or use the stub.
- p95 skewed by cold start: run a warm-up query before measuring.
- `benchmark_results.json` not created: check write permissions.

## Materials

- `scripts/benchmark.py`
- `sample_queries.json`
- `templates/`: prompt template
- `notebooks/`: benchmark analysis notebook
- `verification_artifacts/benchmark_results.json`
- `assets/`: latency and failure-mode graphics

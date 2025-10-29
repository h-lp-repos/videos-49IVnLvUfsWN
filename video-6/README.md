# Video 6: End-to-End Demo & Benchmark

**Duration:** ~15 min

## Objective
Execute the full RAG pipeline (retrieve → rerank → construct prompt → LLM call) for 5 sample queries, capture micro-benchmarks (p50/p95 latencies), and reproduce failure modes with remediation.

## Prerequisites
- Videos 1–5 completed

## Steps

1. **Run benchmark runner**:
   ```bash
   python scripts/benchmark.py --queries data/sample_queries.json --runs 1 --k 5
   # Checkpoint: prints "Saved benchmark results to scripts/benchmark_results.json"
   ```
2. **View benchmark results**:
   ```bash
   cat scripts/benchmark_results.json
   ```
3. **Reproduce failure mode: context blowup**:
   ```bash
   # Append a large chunk to sample_corpus.json and re-run benchmark
   ```
4. **Reproduce failure mode: duplicate chunks**:
   ```bash
   # Use a query that returns overlapping chunks and observe deduplication in cached_query.py
   ```
5. **Save and review logs**:
   ```bash
   ls scripts/benchmark_results.json
   ```

## Common Issues & Troubleshooting
- **Timeouts**: reduce runs or use sandbox mode.
- **High p95**: recommend warming up 1 dummy query before measuring.

---
**Checkpoint:** Ensure `scripts/benchmark_results.json` exists with p50/p95 fields and failure-mode observations.

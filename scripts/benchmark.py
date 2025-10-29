#!/usr/bin/env python3
"""
Benchmark end-to-end RAG pipeline and record p50/p95 timings.
"""
import argparse
import json
import time
import numpy as np
from retrieval import retrieve
from reranker import rerank_items
from prompt_constructor import construct_prompt
from stub_sandbox_llm import generate_response


def benchmark(queries, runs, k, weights, threshold, budget):
    step_times = {'retrieve': [], 'rerank': [], 'construct': [], 'llm': [], 'total': []}
    for q in queries:
        for _ in range(runs):
            t0 = time.time()
            t1 = time.time()
            items = retrieve(q, k)
            t2 = time.time()
            reranked = rerank_items(items, weights, threshold)
            t3 = time.time()
            prompt = construct_prompt(q, reranked, budget)
            t4 = time.time()
            _ = generate_response(prompt)
            t5 = time.time()
            step_times['retrieve'].append(t2 - t1)
            step_times['rerank'].append(t3 - t2)
            step_times['construct'].append(t4 - t3)
            step_times['llm'].append(t5 - t4)
            step_times['total'].append(t5 - t1)
    results = {}
    for step, times in step_times.items():
        results[step] = {
            'p50': float(np.percentile(times, 50)),
            'p95': float(np.percentile(times, 95))
        }
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--queries', type=str, default='data/sample_queries.json')
    parser.add_argument('--runs', type=int, default=1)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--weights', type=str, default='0.8,0.2')
    parser.add_argument('--threshold', type=float, default=None)
    parser.add_argument('--budget', type=int, default=2048)
    args = parser.parse_args()
    weights = tuple(map(float, args.weights.split(',')))
    with open(args.queries, 'r') as f:
        queries = json.load(f)
    results = benchmark(queries, args.runs, args.k, weights, args.threshold, args.budget)
    out_path = 'scripts/benchmark_results.json'
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved benchmark results to {out_path}")

if __name__ == '__main__':
    main()

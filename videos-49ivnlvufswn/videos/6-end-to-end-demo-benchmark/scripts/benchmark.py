import argparse
import json
import time
import random


# Dummy implementations of pipeline steps

def retrieve(query, k=5):
    time.sleep(0.1)  # simulate latency
    results = []
    for i in range(k):
        results.append({
            'source_id': f'source_{i}',
            'chunk_id': i,
            'score': 1.0 - i*0.1,
            'text': f'Retrieved chunk {i} for query "{query}"'
        })
    return results


def rerank(results):
    time.sleep(0.05)
    for r in results:
        r['combined_score'] = r['score'] * 0.8 + 0.2
    return sorted(results, key=lambda x: x['combined_score'], reverse=True)


def construct_prompt(results):
    time.sleep(0.02)
    prompt = "User query: Example\nRetrieved Chunks:\n"
    for r in results:
        prompt += f"- {r['text']}\n"
    return prompt


def call_llm(prompt):
    time.sleep(0.1)
    return "LLM response stub"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--queries', type=str, required=True)
    parser.add_argument('--runs', type=int, default=1)
    args = parser.parse_args()

    with open(args.queries, 'r') as f:
        queries = json.load(f)

    all_timings = []
    for run in range(args.runs):
        for query in queries:
            timings = {}
            start = time.time()
            results = retrieve(query, k=5)
            timings['retrieve'] = time.time() - start

            start = time.time()
            reranked = rerank(results)
            timings['rerank'] = time.time() - start

            start = time.time()
            prompt = construct_prompt(reranked)
            timings['construct_prompt'] = time.time() - start

            start = time.time()
            response = call_llm(prompt)
            timings['llm_call'] = time.time() - start

            timings['total'] = sum(timings.values())
            all_timings.append(timings)

            print(f"Run {run+1}, Query: {query}")
            print(f"Timings: {timings}")
            print(f"Response: {response}\n")

    # Aggregate p50 and p95
    def percentile(data, perc):
        size = len(data)
        sorted_data = sorted(data)
        k = int(size * perc / 100)
        return sorted_data[min(k, size-1)]

    p50_total = percentile([t['total'] for t in all_timings], 50)
    p95_total = percentile([t['total'] for t in all_timings], 95)

    benchmark_results = {
        'p50_total_latency': p50_total,
        'p95_total_latency': p95_total
    }

    with open('scripts/benchmark_results.json', 'w') as f:
        json.dump(benchmark_results, f, indent=2)

    print("Benchmark results saved to scripts/benchmark_results.json")


if __name__ == '__main__':
    main()

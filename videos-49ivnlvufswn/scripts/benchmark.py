#!/usr/bin/env python3
import argparse
import json
import time
from utils.sandbox_llm import call_sandbox
from scripts.retrieve import retrieve
from scripts.rerank import combined_score


def run_query(q):
    out = {'query': q}
    t0 = time.time()
    ret = retrieve(q, k=10)
    t1 = time.time()
    # rerank
    for it in ret:
        it['combined'] = combined_score(it)
    t2 = time.time()
    # construct prompt simple
    prompt = q + '\n' + '\n'.join([r['text'] for r in ret[:3]])
    t3 = time.time()
    resp = call_sandbox(prompt)
    t4 = time.time()
    out['timings'] = {
        'retrieve': t1-t0,
        'rerank': t2-t1,
        'construct': t3-t2,
        'llm': t4-t3,
        'total': t4-t0
    }
    out['response'] = resp
    return out

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--queries', default='sample-queries.json')
    p.add_argument('--runs', type=int, default=1)
    args = p.parse_args()
    with open(args.queries,'r') as f:
        qs = json.load(f)
    results = []
    for r in range(args.runs):
        for q in qs:
            print(f'Run {r+1} query: {q}')
            results.append(run_query(q))
    # compute p50/p95 for total
    totals = sorted([x['timings']['total'] for x in results])
    import math
    def pct(arr,p):
        if not arr: return None
        idx = int(math.ceil((p/100.0)*len(arr)))-1
        idx = max(0,min(idx,len(arr)-1))
        return arr[idx]
    out = {
        'p50_total': pct(totals,50),
        'p95_total': pct(totals,95),
        'runs': len(results),
        'results': results
    }
    with open('scripts/benchmark_results.json','w') as f:
        json.dump(out,f,indent=2)
    print('Benchmark complete. Results written to scripts/benchmark_results.json')


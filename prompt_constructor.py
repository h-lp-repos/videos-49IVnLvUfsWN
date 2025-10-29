"""
Prompt constructor with token-budget enforcement.
"""
import tiktoken
import re
from stub_sandbox_llm import generate_response


def load_template(path='templates/prompt_template.txt'):
    with open(path, 'r') as f:
        return f.read()


def count_tokens(text, model_name='gpt2'):
    enc = tiktoken.get_encoding(model_name)
    return len(enc.encode(text))


def construct_prompt(query, chunks, budget=2048, fallback=True):
    template = load_template()
    # Assemble chunks text and provenance
    chunk_texts = [c['text'] for c in chunks]
    prov_texts = [f"{c['source_id']}:{c['chunk_id']}" for c in chunks]
    # Prepare content
    retrieved = "\n---\n".join(chunk_texts)
    provenance = ", ".join(prov_texts)
    prompt = template.replace('{{retrieved_chunks}}', retrieved)
    prompt = prompt.replace('{{provenance}}', provenance)
    prompt = prompt.replace('{{user_query}}', query)
    total_tokens = count_tokens(prompt)
    if total_tokens > budget and fallback:
        # Truncate chunks until under budget
        for new_k in range(len(chunks)-1, 0, -1):
            retrieved = "\n---\n".join(chunk_texts[:new_k])
            provenance = ", ".join(prov_texts[:new_k])
            prompt = template.replace('{{retrieved_chunks}}', retrieved)
            prompt = prompt.replace('{{provenance}}', provenance)
            prompt = prompt.replace('{{user_query}}', query)
            total_tokens = count_tokens(prompt)
            if total_tokens <= budget:
                print(f"Truncated to {new_k} chunks to meet budget ({total_tokens} tokens)")
                break
    return prompt

if __name__ == '__main__':
    import argparse
    from retrieval import retrieve

    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--budget', type=int, default=2048)
    args = parser.parse_args()
    chunks = retrieve(args.query, args.k)
    prompt = construct_prompt(args.query, chunks, args.budget)
    print(prompt)
    print(f"Total tokens: {count_tokens(prompt)}")
    # Demo LLM stub
    response = generate_response(prompt)
    print(f"LLM response: {response}")

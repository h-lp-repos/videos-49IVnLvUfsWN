import argparse
import tiktoken


def load_template(path):
    with open(path, 'r') as f:
        return f.read()


def count_tokens(text, encoder):
    return len(encoder.encode(text))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=True)
    parser.add_argument('--k', type=int, default=5)
    parser.add_argument('--budget', type=int, default=2048)
    args = parser.parse_args()

    encoder = tiktoken.get_encoding('gpt2')
    template = load_template('templates/prompt_template.txt')

    # Simulate retrieved chunks
    chunks = [f"Chunk {i} content for query '{args.query}'" for i in range(args.k)]

    # Build prompt with all chunks
    prompt = template.format(user_query=args.query, retrieved_chunks='\n'.join(chunks), provenance='Provenance info')

    total_tokens = count_tokens(prompt, encoder)
    print(f"Total tokens with {args.k} chunks: {total_tokens}")

    # Truncate chunks to fit budget
    truncated_chunks = chunks.copy()
    while truncated_chunks and count_tokens(template.format(user_query=args.query, retrieved_chunks='\n'.join(truncated_chunks), provenance='Provenance info'), encoder) > args.budget:
        truncated_chunks.pop()
    print(f"Truncated to {len(truncated_chunks)} chunks to meet budget {args.budget}")

    # Provenance-only fallback
    provenance_only = [f"[Source chunk {i}]" for i in range(len(truncated_chunks))]
    prompt_prov = template.format(user_query=args.query, retrieved_chunks='\n'.join(provenance_only), provenance='Provenance info')
    tokens_prov = count_tokens(prompt_prov, encoder)
    print(f"Tokens with provenance-only fallback: {tokens_prov}")

    # Simulate sandbox LLM stub response
    print("\n--- Sandbox LLM Stub Response ---")
    print(f"Prompt sent to LLM:\n{prompt_prov}")
    print("LLM Response: This is a stub response.")


if __name__ == '__main__':
    main()

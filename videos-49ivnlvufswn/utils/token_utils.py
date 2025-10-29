try:
    import tiktoken
    def count_tokens(text, model='gpt-3.5-turbo'):
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
except Exception:
    def count_tokens(text, model='gpt-3.5-turbo'):
        # Fallback simple whitespace tokenizer
        return len(text.split())


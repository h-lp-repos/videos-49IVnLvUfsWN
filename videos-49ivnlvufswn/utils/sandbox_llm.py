import time

def call_sandbox(prompt: str):
    # Simulate an LLM response quickly
    time.sleep(0.1)
    # Return a canned response including a short summary and an echo of prompt length
    return {
        'answer': 'SANDBOX_RESPONSE: This is a deterministic stub response for testing.',
        'prompt_length': len(prompt)
    }


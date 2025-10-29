import os
import json
import hashlib
import time

CACHE_DIR = os.getenv('CACHE_DIR', 'cache')
TTL_SECONDS = 3600  # 1 hour


def get_cache_key(query, k):
    key_raw = f"{query}:{k}"
    return hashlib.sha256(key_raw.encode()).hexdigest()


def load_cache(key):
    path = os.path.join(CACHE_DIR, f"{key}.json")
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        data = json.load(f)
    # Check TTL
    if time.time() - data.get('timestamp', 0) > TTL_SECONDS:
        os.remove(path)
        return None
    return data.get('results')


def save_cache(key, results):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"{key}.json")
    data = {
        'timestamp': time.time(),
        'results': results
    }
    with open(path, 'w') as f:
        json.dump(data, f)


def clear_cache():
    if not os.path.exists(CACHE_DIR):
        return
    for f in os.listdir(CACHE_DIR):
        os.remove(os.path.join(CACHE_DIR, f))

import os
import time
import pickle
import hashlib

class SimpleCache:
    """File-based cache with TTL"""
    def __init__(self, cache_dir='.cache', ttl=3600):
        self.cache_dir = cache_dir
        self.ttl = ttl
        os.makedirs(self.cache_dir, exist_ok=True)

    def _key_to_path(self, key):
        filename = hashlib.sha256(key.encode()).hexdigest()
        return os.path.join(self.cache_dir, filename)

    def get(self, key):
        path = self._key_to_path(key)
        if not os.path.exists(path):
            return None
        mtime = os.path.getmtime(path)
        if time.time() - mtime > self.ttl:
            os.remove(path)
            return None
        with open(path, 'rb') as f:
            return pickle.load(f)

    def set(self, key, value):
        path = self._key_to_path(key)
        with open(path, 'wb') as f:
            pickle.dump(value, f)

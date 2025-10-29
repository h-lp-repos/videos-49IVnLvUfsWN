import json
import os
import time

CACHE_PATH = 'sample-data/cache.json'

def _ensure():
    d = os.path.dirname(CACHE_PATH)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    if not os.path.exists(CACHE_PATH):
        with open(CACHE_PATH,'w') as f:
            json.dump({}, f)

def get(key):
    _ensure()
    with open(CACHE_PATH,'r') as f:
        data = json.load(f)
    item = data.get(key)
    if not item:
        return None
    # check ttl
    if item.get('ttl') and time.time() > item['ts'] + item['ttl']:
        # expired
        del data[key]
        with open(CACHE_PATH,'w') as f:
            json.dump(data,f)
        return None
    return item['value']

def set(key, value, ttl=None):
    _ensure()
    with open(CACHE_PATH,'r') as f:
        data = json.load(f)
    data[key] = {'value': value, 'ts': time.time(), 'ttl': ttl}
    with open(CACHE_PATH,'w') as f:
        json.dump(data,f)


import json
import math
from typing import List, Dict

BASE = 'sample-data'

def load_chunks():
    with open(f'{BASE}/chunks.json','r') as f:
        chunks = json.load(f)
    return chunks

def load_embeddings():
    with open(f'{BASE}/embeddings.json','r') as f:
        emb = json.load(f)
    return emb

def get_dim():
    emb = load_embeddings()
    return len(emb[0]) if emb else 0


def _dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def _norm(a):
    return math.sqrt(sum(x*x for x in a))

def cosine_similarity(a,b):
    na = _norm(a)
    nb = _norm(b)
    if na==0 or nb==0:
        return 0.0
    return _dot(a,b)/(na*nb)

def query_index(query_vector: List[float], k:int=3):
    emb = load_embeddings()
    chunks = load_chunks()
    sims = []
    for i,vec in enumerate(emb):
        score = cosine_similarity(query_vector, vec)
        item = dict(chunks[i])
        item.update({'score': float(score)})
        sims.append(item)
    sims.sort(key=lambda x: x['score'], reverse=True)
    return sims[:k]


"""
Embeddings helper using sentence-transformers.
"""
from sentence_transformers import SentenceTransformer

_model = None

def get_model(name: str = 'all-MiniLM-L6-v2'):
    global _model
    if _model is None:
        _model = SentenceTransformer(name)
    return _model


def get_embeddings(texts):
    model = get_model()
    return model.encode(texts, show_progress_bar=False)


def get_dim():
    model = get_model()
    return model.get_sentence_embedding_dimension()

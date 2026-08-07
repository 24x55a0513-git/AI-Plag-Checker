from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = None

def load_model():
    global model

    if model is None:
        print("Loading MiniLM...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
        print("MiniLM loaded.")

def get_embedding(code):
    load_model()
    return model.encode(
        code,
        convert_to_numpy=True
    ).reshape(1, -1)

def embedding_similarity(code1, code2):
    emb1 = get_embedding(code1)
    emb2 = get_embedding(code2)

    score = cosine_similarity(emb1, emb2)[0][0]
    return round(score * 100, 2)
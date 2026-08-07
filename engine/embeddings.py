from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = None


def load_model():
    global model

    if model is None:
        print("Loading MiniLM model...")
        model = SentenceTransformer(
    "flax-sentence-embeddings/st-codesearch-distilroberta-base"
)
        print("MiniLM loaded.")


def get_embedding(code):
    load_model()
    return model.encode([code])


def embedding_similarity(code1, code2):

    emb1 = get_embedding(code1)
    emb2 = get_embedding(code2)

    score = cosine_similarity(
        emb1,
        emb2
    )[0][0]

    score = max(0, min(score, 1))

    return round(score * 100, 2)
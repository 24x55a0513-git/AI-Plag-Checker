from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def ai_similarity(code1, code2):

    embedding1 = model.encode([code1])

    embedding2 = model.encode([code2])

    similarity = cosine_similarity(embedding1, embedding2)[0][0]

    return round(similarity * 100, 2)
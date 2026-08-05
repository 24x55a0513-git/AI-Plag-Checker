from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
model.to(DEVICE)
model.eval()


def get_embedding(code):

    inputs = tokenizer(
        code,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding="max_length"
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    embedding = outputs.last_hidden_state[:, 0, :]

    return embedding.cpu().numpy()


def codebert_similarity(code1, code2):

    emb1 = get_embedding(code1)
    emb2 = get_embedding(code2)

    similarity = cosine_similarity(emb1, emb2)[0][0]

    similarity = max(0, min(similarity, 1))

    return round(similarity * 100, 2)
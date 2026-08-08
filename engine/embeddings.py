from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from engine.function_extractor import extract_functions
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/codebert-base"
)
model = AutoModel.from_pretrained(
    "microsoft/codebert-base"
)
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
    inputs = {
        k: v.to(DEVICE)
        for k, v in inputs.items()
    }
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state[:, 0, :]
    return embedding.cpu().numpy()
def compare_functions(funcs1, funcs2):
    scores = []
    for f1 in funcs1:
        best = 0
        emb1 = get_embedding(f1["code"])
        for f2 in funcs2:
            emb2 = get_embedding(f2["code"])
            sim = cosine_similarity(
                emb1,
                emb2
            )[0][0]
            sim = max(0, min(sim, 1))
            best = max(best, sim)
        scores.append(best)
    if len(scores) == 0:
        return 0
    return (sum(scores) / len(scores)) * 100
def embedding_similarity(code1, code2):
    funcs1 = extract_functions(code1)
    funcs2 = extract_functions(code2)
    if not funcs1 or not funcs2:
        emb1 = get_embedding(code1)
        emb2 = get_embedding(code2)
        score = cosine_similarity(
            emb1,
            emb2
        )[0][0]
        score = max(0, min(score, 1))
        score *= 100
    else:
        score = compare_functions(
            funcs1,
            funcs2
        )
    if len(code1.split()) < 20 or len(code2.split()) < 20:
        score *= 0.85
    return round(score, 2)
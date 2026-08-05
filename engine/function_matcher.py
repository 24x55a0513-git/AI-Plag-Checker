from engine.token_similarity import token_similarity
from engine.ast_compare import ast_similarity
from engine.control_flow import control_flow_similarity
def match_functions(funcs1, funcs2):
    matches = []
    used = set()
    for f1 in funcs1:
        best = None
        best_score = -1
        for i, f2 in enumerate(funcs2):
            if i in used:
                continue
            token = token_similarity(f1["code"], f2["code"])
            ast = ast_similarity(f1["code"], f2["code"])
            cfg = control_flow_similarity(f1["code"], f2["code"])
            score = (
                token * 0.4 +
                ast * 0.35 +
                cfg * 0.25
            )
            if score > best_score:
                best_score = score
                best = i
        if best is not None:
            used.add(best)
            matches.append({
                "function1": f1["name"],
                "function2": funcs2[best]["name"],
                "score": round(best_score, 2)
            })
    return matches
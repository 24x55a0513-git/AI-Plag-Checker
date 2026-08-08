from engine.token_similarity import token_similarity
from engine.ast_compare import ast_similarity
from engine.control_flow import control_flow_similarity
from engine.embeddings import embedding_similarity
from engine.scorer import final_score
from engine.complexity import complexity_similarity
from engine.clone_detector import detect_clone_type
from engine.risk import risk_analysis
from engine.preprocessor import preprocess_code

def detect_plagiarism(code1, code2, compare_mode="complete"):
    print("COMPARE MODE:", compare_mode)
    print("CODE1 BEFORE:", code1[:200])
    print("CODE2 BEFORE:", code2[:200])
    if compare_mode == "clean":
        code1 = preprocess_code(code1)
        code2 = preprocess_code(code2)
    print("CODE1 AFTER:", code1[:200])
    print("CODE2 AFTER:", code2[:200])
    if code1.strip() == code2.strip():
        return {
            "overall": 100.0,
            "token": 100.0,
            "ast": 100.0,
            "cfg": 100.0,
            "complexity": 100.0,
            "ai": 100.0,
            "risk": "Very High 🔴",
            "recommendation": "Both files are identical. This is a confirmed Type-1 clone.",
            "clone_type": "Type-1 Clone (Exact Copy)"
        }
    token = token_similarity(code1, code2)
    ast = ast_similarity(code1, code2)
    cfg = control_flow_similarity(code1, code2)
    ai = embedding_similarity(code1, code2)
    complexity = complexity_similarity(code1, code2)
    overall = final_score(
        token,
        ast,
        cfg,
        complexity,
        ai
    )
    clone_type = detect_clone_type(
        token,
        ast,
        cfg,
        complexity,
        ai,
        overall
    )
    risk, recommendation = risk_analysis(overall)
    return {
        "overall": overall,
        "token": token,
        "ast": ast,
        "cfg": cfg,
        "complexity": complexity,
        "ai": ai,
        "risk": risk,
        "recommendation": recommendation,
        "clone_type": clone_type
    }
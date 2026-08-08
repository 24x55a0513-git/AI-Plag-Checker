import ast
def get_complexity(code):
    try:
        tree = ast.parse(code)
    except:
        return 0
    complexity = 1
    decision_nodes = (
        ast.If,
        ast.For,
        ast.While,
        ast.Try,
        ast.ExceptHandler,
        ast.With,
        ast.BoolOp,
        ast.IfExp,
        ast.ListComp,
        ast.SetComp,
        ast.DictComp,
        ast.GeneratorExp,
        ast.Assert,
        ast.Match
    )
    for node in ast.walk(tree):
        if isinstance(node, decision_nodes):
            complexity += 1
    return complexity
def complexity_similarity(code1, code2):
    c1 = get_complexity(code1)
    c2 = get_complexity(code2)
    if c1 == 0 and c2 == 0:
        return 100.0
    similarity = (
        min(c1, c2) /
        max(c1, c2)
    ) * 100
    return round(similarity, 2)
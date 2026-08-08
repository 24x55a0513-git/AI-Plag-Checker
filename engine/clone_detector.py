def detect_clone_type(token, ast, cfg, complexity, ai, overall):
    if (
        token >= 98 and
        ast >= 98 and
        cfg >= 98
    ):
        return "Type-1 Clone (Exact Copy)"
    elif (
        token >= 75 and
        ast >= 85 and
        cfg >= 80
    ):
        return "Type-2 Clone (Renamed Identifiers)"
    elif (
        overall >= 60 and
        ast >= 60
    ):
        return "Type-3 Clone (Modified Statements)"
    elif (
        overall >= 40 and
        ai >= 60
    ):
        return "Type-4 Clone (Semantic Clone)"
    else:
        return "No Clone Detected"
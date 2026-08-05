def detect_clone_type(token, ast, cfg, complexity, ai, overall):

    # Type-1: Exact copy
    if (
        token >= 98 and
        ast >= 98 and
        cfg >= 98
    ):
        return "Type-1 Clone (Exact Copy)"

    # Type-2: Renamed variables / formatting changes
    elif (
        token >= 75 and
        ast >= 85 and
        cfg >= 80
    ):
        return "Type-2 Clone (Renamed Identifiers)"

    # Type-3: Modified statements
    elif (
        overall >= 60 and
        ast >= 60
    ):
        return "Type-3 Clone (Modified Statements)"

    # Type-4: Semantic clone
    elif (
        overall >= 40 and
        ai >= 60
    ):
        return "Type-4 Clone (Semantic Clone)"

    # No meaningful clone
    else:
        return "No Clone Detected"
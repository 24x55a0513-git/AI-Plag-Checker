def final_score(token, ast, cfg, complexity, ai):

    # Base weighted score
    overall = (
        token * 0.35 +
        ast * 0.25 +
        cfg * 0.20 +
        complexity * 0.10 +
        ai * 0.10
    )

    # Very different programs
    if token < 20 and ast < 20:
        overall *= 0.70

    # Same structure but renamed variables
    elif token < 70 and ast > 90 and cfg > 90:
        overall += 5

    # Extremely similar programs
    elif token > 95 and ast > 95 and cfg > 95:
        overall += 3

    # Strong semantic similarity
    elif ai > 90 and ast > 70:
        overall += 2

    overall = max(0, min(100, overall))

    return round(overall, 2)
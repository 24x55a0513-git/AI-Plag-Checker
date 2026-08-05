from difflib import SequenceMatcher


def highlight_matches(original1, original2):

    lines1 = original1.splitlines()
    lines2 = original2.splitlines()

    max_len = max(len(lines1), len(lines2))

    result1 = []
    result2 = []

    for i in range(max_len):

        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""

        score = SequenceMatcher(
            None,
            line1.strip(),
            line2.strip()
        ).ratio()

        match = score >= 0.75

        result1.append({
            "line": line1,
            "match": match
        })

        result2.append({
            "line": line2,
            "match": match
        })

    return result1, result2
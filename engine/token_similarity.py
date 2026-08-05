import io
import keyword
import tokenize
from difflib import SequenceMatcher

def normalize_tokens(code):
    tokens = []

    reader = io.StringIO(code).readline

    try:
        for tok in tokenize.generate_tokens(reader):

            token_type = tok.type
            token_value = tok.string

            if token_type == tokenize.NAME:
                if keyword.iskeyword(token_value):
                    tokens.append(token_value)
                else:
                    tokens.append("ID")

            elif token_type == tokenize.NUMBER:
                tokens.append("NUM")

            elif token_type == tokenize.STRING:
                tokens.append("STR")

            elif token_type == tokenize.OP:
                tokens.append(token_value)

    except:
        pass

    return tokens


def token_similarity(code1, code2):

    tokens1 = normalize_tokens(code1)
    tokens2 = normalize_tokens(code2)

    similarity = SequenceMatcher(
        None,
        tokens1,
        tokens2
    ).ratio()

    return round(similarity * 100, 2)
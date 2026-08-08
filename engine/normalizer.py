import re
import keyword
import tokenize
from io import StringIO
PYTHON_KEYWORDS = set(keyword.kwlist)
def remove_comments(code):
    """
    Remove single-line comments.
    """
    return re.sub(r"#.*", "", code)
def normalize_python_variables(code):
    """
    Rename variables to VAR1, VAR2, ...
    """
    variable_map = {}
    variable_count = 1
    result = []
    tokens = tokenize.generate_tokens(StringIO(code).readline)
    for token in tokens:
        token_type = token.type
        token_value = token.string
        if token_type == tokenize.NAME:
            if token_value not in PYTHON_KEYWORDS:
                if token_value not in variable_map:
                    variable_map[token_value] = f"VAR{variable_count}"
                    variable_count += 1
                token_value = variable_map[token_value]
        result.append(token_value)
    return " ".join(result)
def normalize_code(code):
    """
    Complete normalization pipeline.
    """
    code = remove_comments(code)
    code = normalize_python_variables(code)
    return code
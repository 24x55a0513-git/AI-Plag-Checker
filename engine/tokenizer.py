import tokenize
import keyword
from io import StringIO


PYTHON_KEYWORDS = set(keyword.kwlist)


def tokenize_code(code):

    tokens = []

    variable_map = {}
    variable_count = 1

    try:

        generator = tokenize.generate_tokens(
            StringIO(code).readline
        )

        for token in generator:

            token_type = tokenize.tok_name[token.type]
            token_value = token.string

            if token_type in [
                "ENCODING",
                "NL",
                "NEWLINE",
                "INDENT",
                "DEDENT",
                "ENDMARKER"
            ]:
                continue

            if token_type == "NUMBER":
                tokens.append("NUM")
                continue

            if token_type == "STRING":
                tokens.append("STR")
                continue

            if token_type == "NAME":

                if token_value in PYTHON_KEYWORDS:
                    tokens.append(token_value)

                else:

                    if token_value not in variable_map:
                        variable_map[token_value] = f"VAR{variable_count}"
                        variable_count += 1

                    tokens.append(variable_map[token_value])

                continue

            tokens.append(token_value)

    except Exception:
        pass

    return tokens
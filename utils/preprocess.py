import re
import keyword

def preprocess_code(code):

    # Python comments
    code = re.sub(r"#.*", "", code)

    # C/C++/Java/JavaScript comments
    code = re.sub(r"//.*", "", code)

    # Multi-line comments
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)

    # Remove blank lines
    lines = code.splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    code = "\n".join(lines)

    # Normalize variable names
    words = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", code)

    keywords = set(keyword.kwlist)

    common_keywords = {
        "int","float","double","char","void",
        "public","private","class","static",
        "return","String","System","out",
        "println","include","stdio","main",
        "using","namespace","std","cout","cin",
        "console","log","function","var","let","const"
    }

    keywords.update(common_keywords)

    variables = {}

    count = 1

    for word in words:

        if word not in keywords:

            if word not in variables:

                variables[word] = f"VAR{count}"
                count += 1

    for old, new in variables.items():

        code = re.sub(rf"\b{old}\b", new, code)

    return code
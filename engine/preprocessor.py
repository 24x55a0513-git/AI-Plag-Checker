import re
def preprocess_code(code):
    code = re.sub(r"'''[\s\S]*?'''", "", code)
    code = re.sub(r'"""[\s\S]*?"""', "", code)
    code = re.sub(r"/\*[\s\S]*?\*/", "", code)
    cleaned_lines = []
    for line in code.splitlines():
        line = re.sub(r"#.*", "", line)
        line = re.sub(r"//.*", "", line)
        line = line.rstrip()
        if line.rstrip():
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)
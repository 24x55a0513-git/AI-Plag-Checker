import re
def preprocess_code(code):
    
    # Remove Python multi-line comments
    code = re.sub(r"'''[\s\S]*?'''", "", code)
    code = re.sub(r'"""[\s\S]*?"""', "", code)

    # Remove C/C++ multi-line comments
    code = re.sub(r"/\*[\s\S]*?\*/", "", code)

    cleaned_lines = []

    for line in code.splitlines():
        # Remove Python comments
        line = re.sub(r"#.*", "", line)

        # Remove C/C++ comments
        line = re.sub(r"//.*", "", line)

        # Remove leading/trailing spaces
        line = line.rstrip()

        # Skip empty lines
        if line.rstrip():
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
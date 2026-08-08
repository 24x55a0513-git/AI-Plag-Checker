import os
LANGUAGE_MAP = {
    ".py": "python",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".js": "javascript"
}
def detect_language(filename):
    extension = os.path.splitext(filename)[1].lower()
    return LANGUAGE_MAP.get(extension, "unknown")
def read_code(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()
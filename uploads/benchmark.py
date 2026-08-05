import os
from engine.detector import detect_plagiarism

TEST_FOLDER = "test_cases"

for folder in os.listdir(TEST_FOLDER):

    folder_path = os.path.join(TEST_FOLDER, folder)

    code1_path = os.path.join(folder_path, "code1.py")
    code2_path = os.path.join(folder_path, "code2.py")

    with open(code1_path, "r") as f:
        code1 = f.read()

    with open(code2_path, "r") as f:
        code2 = f.read()

    result = detect_plagiarism(code1, code2)

    print("=" * 50)
    print(folder.upper())
    print(f"Overall : {result['overall']}%")
    print(f"Token   : {result['token']}%")
    print(f"AST     : {result['ast']}%")
    print(f"AI      : {result['ai']}%")
    print(f"Risk    : {result['risk']}")
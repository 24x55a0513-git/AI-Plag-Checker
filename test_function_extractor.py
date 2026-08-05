from engine.function_extractor import extract_functions


code = """

class Student:

    def login(self,name):

        print(name)

    def register(self):

        print("register")


def add(a,b):

    return a+b


def sub(a,b):

    return a-b

"""

functions = extract_functions(code)

for f in functions:

    print("="*40)

    print(f["name"])

    print(f["class"])

    print(f["start"], f["end"])

    print(f["arguments"])

    print(f["code"])
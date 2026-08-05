from engine.function_extractor import extract_functions
from engine.function_matcher import match_functions

code1 = """
def add(a,b):
    return a+b

def sub(a,b):
    return a-b
"""

code2 = """
def sum_numbers(x,y):
    return x+y

def difference(x,y):
    return x-y
"""

f1 = extract_functions(code1)
f2 = extract_functions(code2)

matches = match_functions(f1, f2)

for m in matches:
    print(m)
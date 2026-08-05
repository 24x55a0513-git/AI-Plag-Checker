from engine.tokenizer import tokenize_code

code = """
a = 10
b = 20

print(a+b)
"""

tokens = tokenize_code(code)

print(tokens)
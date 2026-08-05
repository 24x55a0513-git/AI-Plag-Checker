from engine.tokenizer import tokenize_code

code1 = """
a = 10
b = 20
print(a+b)
"""

code2 = """
x = 10
y = 20
print(x+y)
"""

print("Code1 Tokens:")
print(tokenize_code(code1))

print("\nCode2 Tokens:")
print(tokenize_code(code2))
from engine.token_similarity import token_similarity

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

print(token_similarity(code1, code2))
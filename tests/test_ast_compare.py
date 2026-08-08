from engine.ast_compare import ast_similarity

code1 = """
for i in range(10):
    if i % 2 == 0:
        print(i)
"""

code2 = """
x = 0

while x < 10:
    print(x)
    x += 1
"""

print(ast_similarity(code1, code2))
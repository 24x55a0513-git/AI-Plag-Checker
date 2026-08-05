from engine.ast_compare import ast_similarity

code1 = """
for i in range(5):
    print(i)
"""

code2 = """
if a > b:
    print(a)
"""

print(ast_similarity(code1, code2))
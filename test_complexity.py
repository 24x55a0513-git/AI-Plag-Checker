from engine.complexity import complexity_similarity

code1 = """
for i in range(5):
    if i % 2 == 0:
        print(i)
"""

code2 = """
for j in range(10):
    if j > 5:
        print(j)
"""

print(complexity_similarity(code1, code2))
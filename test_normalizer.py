from engine.normalizer import normalize_code

code = """
# This is a comment

a = 10
b = 20

print(a+b)
"""

print(normalize_code(code))
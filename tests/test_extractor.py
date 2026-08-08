from engine.extractor import extract_features

code = """
import math

class Student:
    pass

def add(a,b):
    if a>b:
        return a
    return b

for i in range(5):
    print(i)
"""

print(extract_features(code))
from engine.detector import detect_plagiarism

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

result = detect_plagiarism(code1, code2)

print("Overall :", result["overall"])
print("Text :", result["text"])
print("Feature :", result["feature"])
print("AI :", result["ai"])
print("Risk :", result["risk"])
print("Recommendation :", result["recommendation"])
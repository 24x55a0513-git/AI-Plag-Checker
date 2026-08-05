from engine.control_flow import control_flow_similarity

code1 = """
for i in range(5):
    print(i)
"""

code2 = """
if a>b:
    print(a)
"""

print(control_flow_similarity(code1, code2))
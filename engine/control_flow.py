import ast
from difflib import SequenceMatcher
class CFGVisitor(ast.NodeVisitor):
    def __init__(self):
        self.flow = []
    def visit_If(self, node):
        self.flow.append("IF")
        self.generic_visit(node)
    def visit_For(self, node):
        self.flow.append("FOR")
        self.generic_visit(node)
    def visit_While(self, node):
        self.flow.append("WHILE")
        self.generic_visit(node)
    def visit_Try(self, node):
        self.flow.append("TRY")
        self.generic_visit(node)
    def visit_FunctionDef(self, node):
        self.flow.append("FUNCTION")
        self.generic_visit(node)
    def visit_Return(self, node):
        self.flow.append("RETURN")
        self.generic_visit(node)
    def visit_Break(self, node):
        self.flow.append("BREAK")
    def visit_Continue(self, node):
        self.flow.append("CONTINUE")
def extract_flow(code):
    try:
        tree = ast.parse(code)
    except:
        return []
    visitor = CFGVisitor()
    visitor.visit(tree)
    return visitor.flow
def control_flow_similarity(code1, code2):
    flow1 = extract_flow(code1)
    flow2 = extract_flow(code2)
    similarity = SequenceMatcher(
        None,
        flow1,
        flow2
    ).ratio()
    return round(similarity * 100, 2)
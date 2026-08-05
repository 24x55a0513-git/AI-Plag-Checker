import ast
from difflib import SequenceMatcher

class ASTVisitor(ast.NodeVisitor):

    def __init__(self):
        self.nodes = []

    def generic_visit(self, node):
        self.nodes.append(type(node).__name__)
        super().generic_visit(node)


def get_ast_nodes(code):

    try:
        tree = ast.parse(code)
        visitor = ASTVisitor()
        visitor.visit(tree)
        return visitor.nodes

    except Exception:
        return []


def ast_similarity(code1, code2):

    nodes1 = get_ast_nodes(code1)
    nodes2 = get_ast_nodes(code2)

    score = SequenceMatcher(None, nodes1, nodes2).ratio()

    return round(score * 100, 2)
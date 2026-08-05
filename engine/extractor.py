import ast
class FunctionExtractor(ast.NodeVisitor):
    def __init__(self, code):
        self.code = code
        self.lines = code.splitlines()
        self.functions = []
        self.current_class = None
    def visit_ClassDef(self, node):
        previous = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = previous
    def visit_FunctionDef(self, node):
        start = node.lineno - 1
        end = node.end_lineno
        source = "\n".join(
            self.lines[start:end]
        )
        self.functions.append({
            "name": node.name,
            "class": self.current_class,
            "start": node.lineno,
            "end": node.end_lineno,
            "arguments": len(node.args.args),
            "code": source
        })
        self.generic_visit(node)
def extract_functions(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
    extractor = FunctionExtractor(code)
    extractor.visit(tree)
    return extractor.functions
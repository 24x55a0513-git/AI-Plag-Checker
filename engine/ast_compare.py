import ast
from difflib import SequenceMatcher


class ASTNormalizer(ast.NodeTransformer):

    def visit_Name(self, node):
        return ast.copy_location(
            ast.Name(id="VAR", ctx=node.ctx),
            node
        )

    def visit_arg(self, node):
        node.arg = "ARG"
        return node

    def visit_FunctionDef(self, node):
        node.name = "FUNCTION"
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        node.name = "CLASS"
        self.generic_visit(node)
        return node


def ast_similarity(code1, code2):

    try:

        tree1 = ast.parse(code1)
        tree2 = ast.parse(code2)

        tree1 = ASTNormalizer().visit(tree1)
        tree2 = ASTNormalizer().visit(tree2)

        ast.fix_missing_locations(tree1)
        ast.fix_missing_locations(tree2)

        dump1 = ast.dump(tree1)
        dump2 = ast.dump(tree2)

        similarity = SequenceMatcher(
            None,
            dump1,
            dump2
        ).ratio()

        return round(similarity * 100, 2)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return 0.0
# Compile the code - called by both the GUI and the command line interface
from antlr4 import CommonTokenStream

from antlr.generated import GreekBaseParser
from src.ast_builder import GreekASTBuilder
from src.codegen import CGenerator
from src.semantic_checker import SemanticChecker


def compile_code(lexer) -> tuple[str, str]:

    token_stream = CommonTokenStream(lexer)
    parser = GreekBaseParser(token_stream)

    tree = parser.program()

    ast_builder = GreekASTBuilder()
    ast = ast_builder.visit(tree)

    print(ast)

    checker = SemanticChecker()
    tab, errors_and_warnings = checker.analyze(ast)

    checker.finalise()

    codegen = CGenerator(tab)
    # Generate C code from the AST
    code = codegen.generate(ast)
    return code, errors_and_warnings
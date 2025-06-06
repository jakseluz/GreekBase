from antlr4 import CommonTokenStream
from antlr.generated import GreekBaseLexer, GreekBaseParser
from src import GreekASTBuilder, CGenerator, SemanticChecker


# Called by both - the GUI and the CLI
def compile_code(input_stream) -> tuple[str, str]:

    lexer = GreekBaseLexer(input_stream)
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
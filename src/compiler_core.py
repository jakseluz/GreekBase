from antlr4 import CommonTokenStream
from antlr.generated import GreekBaseLexer, GreekBaseParser
from src import GreekASTBuilder, CGenerator, SemanticChecker, ast
from .error_listener import GreekErrorListener


# Called by both - the GUI and the CLI
def compile_code(input_stream) -> tuple[str, str, bool, ast.Program]:

    lexer = GreekBaseLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GreekBaseParser(token_stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    error_listener = GreekErrorListener()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    ast_builder = GreekASTBuilder()
    ast = ast_builder.visit(tree)

    checker = SemanticChecker()
    tab, errors_and_warnings = checker.analyze(ast)
    all_errors = "\n".join(error_listener.syntax_errors) + "\n" + errors_and_warnings
    success = checker.finalise()

    if success:
        codegen = CGenerator(tab)
        # Generate C code from the AST
        code = codegen.generate(ast)
    else:
        code = ""
    
    return code, all_errors, success, ast
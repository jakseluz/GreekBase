import sys, os
from antlr4 import FileStream, CommonTokenStream

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'antlr', 'generated')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src')))

from GreekBaseLexer import GreekBaseLexer
from GreekBaseParser import GreekBaseParser
from ast_builder import GreekASTBuilder
from semantic_checker import SemanticChecker
from codegen import CGenerator


def main():
    input_stream = FileStream(os.path.join(os.path.dirname(__file__), "examples", "example1.adan"))

    lexer = GreekBaseLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GreekBaseParser(token_stream)

    tree = parser.program()

    ast_builder = GreekASTBuilder()
    ast = ast_builder.visit(tree)

    print(ast)

    checker = SemanticChecker()
    tab = checker.analyze(ast)
    checker.finalise()

    codegen = CGenerator(tab)
    code = codegen.generate(ast)
    
    with open("output/example1.c", "w") as filehandler:
        filehandler.write(code)


if __name__ == '__main__':
    main()
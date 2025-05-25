import sys, os
from antlr4 import FileStream, CommonTokenStream, InputStream

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'antlr', 'generated')))

from GreekBaseLexer import GreekBaseLexer
from GreekBaseParser import GreekBaseParser
from ast_builder import GreekASTBuilder


def main():
    # input = FileStream("example.my")
    input_stream = InputStream("x := 5; y := 10; if x < y then x := x + 1; else y := y - 1; end if; print x; print y;")

    lexer = GreekBaseLexer(input)
    token_stream = CommonTokenStream(lexer)
    parser = GreekBaseParser(token_stream)

    tree = parser.program()

    ast_builder = GreekASTBuilder()
    ast = ast_builder.visit(tree)

    print(ast)


if __name__ == '__main__':
    main()
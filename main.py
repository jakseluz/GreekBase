import sys
from antlr4 import *
from antlr.GreekBaseLexer import GreekBaseLexer
from antlr.GreekBaseParser import GreekBaseParser
from antlr.interpreter import GreekInterpreter
def main():
    #print("Enter code (end input with Ctrl+D on Unix or Ctrl+Z on Windows):")
    #input_stream = InputStream(sys.stdin.read())
    #lexer = GreekBaseLexer(input_stream)


    input = "x := 5; y := 10; if x < y then x := x + 1; else y := y - 1; end if; print x; print y;"
    lexer = GreekBaseLexer(InputStream(input))




    tokens = CommonTokenStream(lexer)
    parser = GreekBaseParser(tokens)
    tree = parser.program()

    visitor = GreekInterpreter()
    visitor.visit(tree)

    if __name__ == '__main__':
        main()
main()
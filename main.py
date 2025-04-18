import sys
#IMPORTY MAJA ZLA LOKALIZACJE
from antlr4 import *
from .p_GreekLexer import p_GreekLexer
from .p_GreekParser import p_GreekParser
from . import GreekInterpreter 

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = p_GreekLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = p_GreekParser(tokens)
    tree = parser.program() # 'program' to reguła początkowa 

    walker = ParseTreeWalker()
    interpreter = GreekInterpreter()
    walker.walk(interpreter, tree) # Przejdź po drzewie

if __name__ == '__main__':
    main(sys.argv)

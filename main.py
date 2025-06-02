import sys, os
from antlr4 import FileStream, CommonTokenStream

#GUI
from gui import gui
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'antlr', 'generated')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src')))

from GreekBaseLexer import GreekBaseLexer
from GreekBaseParser import GreekBaseParser
from ast_builder import GreekASTBuilder
from semantic_checker import SemanticChecker
from codegen import CGenerator

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print(
            """
            Compile GreekBase .gb file to C language source file .c
            Usage:
            * --help                                                    -> print this info
            * inputs/example1.gb                                        -> compile example1.gb to output/example1.c
            * inputs/example1.gb -o custom_catalogue/custom_file.c      -> specify output path
            """
        )
        exit(0)
    try:
        input_stream = FileStream(sys.argv[1])
    except:
        print("Please provide a proper source file path!")

    lexer = GreekBaseLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GreekBaseParser(token_stream)

    tree = parser.program()

    ast_builder = GreekASTBuilder()
    ast = ast_builder.visit(tree)

    print(ast)

    checker = SemanticChecker()
    tab, errors_and_warnings = checker.analyze(ast)
    print(errors_and_warnings)
    checker.finalise()

    codegen = CGenerator(tab)
    code = codegen.generate(ast)
    

    if len(sys.argv) > 2 and sys.argv[2] == "-o":
        try:
            output_path_str = sys.argv[3]
        except:
            print("Please provide a proper output path!")
    else:
        output_path_str = "output/" + sys.argv[1].split('/')[-1][:-3] + ".c"
    
    output_file = Path(output_path_str)
    output_file.parent.mkdir(exist_ok = True, parents = True)
    
    with open(output_path_str, 'w') as filehandler:
        filehandler.write(code)


if __name__ == '__main__':
    main()
    gui = gui()
    gui.run()

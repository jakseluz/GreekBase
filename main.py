import sys, os
from antlr4 import FileStream


from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'antlr', 'generated')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src')))

from GreekBaseLexer import GreekBaseLexer
from compiler_core import compile_code
#GUI
from gui import gui
def compile_code_from_IDE():
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
    code, errors_and_warnings = compile_code(lexer)
    print(errors_and_warnings)
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


def main():
        #compile_code_from_IDE()  # Uncomment this line to run the compilation directly from the IDE
        app = gui()
        app.run()
if __name__ == '__main__':
    main()

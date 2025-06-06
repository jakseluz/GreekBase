import sys, os
from antlr4 import FileStream
from pathlib import Path
from src import *


class Main:
    
    def compile_code_cli(self) -> bool:

        output_path_str = self.handle_arguments()
        if not output_path_str:
            return False

        try:
            input_stream = FileStream(sys.argv[1])
        except:
            print("Please provide a proper source file path!")
            return False

        code, errors_and_warnings = compile_code(input_stream)
        print(errors_and_warnings)

        output_file = Path(output_path_str)
        output_file.parent.mkdir(exist_ok = True, parents = True)
        
        with open(output_path_str, 'w') as filehandler:
            filehandler.write(code)
        
        return True


    def handle_arguments(self) -> str | bool:

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
        
        if len(sys.argv) > 2 and sys.argv[2] == "-o":
            try:
                output_path_str = sys.argv[3]
            except:
                print("Please provide a proper output path!")
                return False
        else:
            output_path_str = "output/" + sys.argv[1].split('/')[-1][:-3] + ".c"
        
        return output_path_str


    def main(self) -> None:
            
            if len(sys.argv) > 1:
                self.compile_code_cli()
            else:
                app = gui()
                app.run()



if __name__ == '__main__':
    main = Main()
    main.main()

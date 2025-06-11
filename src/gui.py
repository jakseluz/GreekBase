import tkinter as tk
from tkinter import filedialog, messagebox

from antlr4 import InputStream
from src import compile_code

# C code highlighting
from pygments import lex
from pygments.lexers import CLexer
from pygments.token import Token
# For colouring GreekBase we WILL use AdaLexer since syntax is very simillar
from pygments.lexers import AdaLexer


class gui:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Greek Base Compiler")
        size = (1000, 700) # Default window size
        self.root.geometry(f"{size[0]}x{size[1]}")

        # Main frame with its grid
        self.frame = tk.Frame(self.root,)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left part
        self.input_line_numbers = TextLineNumbers(self.frame, None)
        self.input_line_numbers.grid(row=0, column=0, sticky="ns")
        self.input_text = CustomText(self.frame, width=50)
        self.input_line_numbers.attach(self.input_text)

        self.input_text.grid(row=0, column=1, sticky="nsew", padx=(0, 10))

        # Right part
        self.output_line_numbers = TextLineNumbers(self.frame, None)
        self.output_line_numbers.grid(row=0, column=2, sticky="ns")
        self.output_text = CustomText(self.frame, width=50, state=tk.DISABLED)
        self.output_line_numbers.attach(self.output_text)
        self.output_text.grid(row=0, column=3, sticky="nsew")

        # Przyciski pod odpowiednimi polami
        self.load_btn = tk.Button(self.frame, text="Wczytaj plik", command=self.load_file)
        self.load_btn.grid(row=1, column=1, pady=5)

        self.compile_btn = tk.Button(self.frame, text="Compile", command=self.compile_text)
        self.compile_btn.grid(row=1, column=3, pady=5)

        # Stretching the grid
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # Bottom part - logging
        self.down_frame = tk.Frame(self.root)
        self.down_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))

        self.log_text = CustomText(self.down_frame, width=100, height=10, state=tk.DISABLED)
        self.log_text.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


    def load_file(self):
        file_path = filedialog.askopenfilename(title="Wybierz plik",
                                               filetypes=[("Wszystkie pliki", "*.*"), ("Pliki tekstowe", "*.txt"),  ("Pliki adan", "*.adan"), ("Pliki greekBase", "*.gb")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert(tk.END, content)
                self.input_text.event_generate("<<Change>>")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku:\n{e}")


    def compile_text(self):
        input_content = self.input_text.get("1.0", tk.END).strip()
        if not input_content:
            messagebox.showinfo("Info", "Pole tekstowe po lewej jest puste!")
            return
        # Compilation logic
        processed, errors_and_warnings, success = compile_code_from_gui(input_content)
        # Debug
        print("Errors and warnings: " + errors_and_warnings)
        """
        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        label = tk.Label(self.log_text, text = errors_and_warnings, font = ("Arial", 14), bg = "lightgray", height=10)
        scrollbar.config(command=self.log_text.yview)
        label.pack()
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        if success: highlight_c_code(self.output_text, processed)
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.insert(tk.END, errors_and_warnings + "\n")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.event_generate("<<Change>>")


    def run(self):
        self.root.mainloop()



# Class for numbering lines inside the text field
class TextLineNumbers(tk.Canvas):

    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, width=30, **kwargs)
        self.text_widget = None


    # Funkcja do podłączenia z numerami linii do widgetu tekstowego
    def attach(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.bind("<<Change>>", self.redraw)
        self.text_widget.bind("<Configure>", self.redraw)
        self.text_widget.bind("<KeyRelease>", self.redraw)


    # Refreshing the numbering
    def redraw(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.text_widget.index(f"{i}+1line")



class CustomText(tk.Text):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<KeyRelease>", self.on_change)


    def on_change(self, event):
        self.event_generate("<<Change>>")


# This function is used to compile code from the GUI input
# It takes the GreekBase code as a string, processes it, and returns the generated C code and any errors or warnings
def compile_code_from_gui(GBcode: str) -> tuple[str, str]:
    return compile_code(InputStream(GBcode))


# this function uses pygments to hihglight output code written in C language
def highlight_c_code(text_widget: tk.Text, code: str):
    # Clean previous tags
    text_widget.tag_delete(*text_widget.tag_names())
    
    # Code tokenization
    for token_type, token_value in lex(code, CLexer()):
        start_index = text_widget.index(tk.INSERT)
        text_widget.insert(tk.INSERT, token_value)

        end_index = text_widget.index(tk.INSERT)
        tag_name = str(token_type)

        # Add tags to the text
        text_widget.tag_add(tag_name, start_index, end_index)

        # Tag styles
        if token_type in Token.Keyword:
            text_widget.tag_config(tag_name, foreground="blue")
        elif token_type in Token.String:
            text_widget.tag_config(tag_name, foreground="green")
        elif token_type in Token.Comment:
            text_widget.tag_config(tag_name, foreground="gray")
        elif token_type in Token.Number:
            text_widget.tag_config(tag_name, foreground="purple")
        elif token_type in Token.Operator:
            text_widget.tag_config(tag_name, foreground="orange")
        elif token_type in Token.Name.Function:
            text_widget.tag_config(tag_name, foreground="darkgreen")
        # Add more if needed

#TODO: Tkinter ma problem z kolorowaniem pojedynczych tokenów
# i chat sugeruje żeby za każdym razem kolorować cały kod, da się to na pewno zrobić wydajniej na razie nie używam tego
def highlight_ada_code(text_widget: tk.Text, code: str):
    # Clean previous tags
    text_widget.tag_delete(*text_widget.tag_names())
    
    # Code tokenization
    for token_type, token_value in lex(code, AdaLexer()):
        start_index = text_widget.index(tk.INSERT)
        text_widget.insert(tk.INSERT, token_value)

        end_index = text_widget.index(tk.INSERT)
        tag_name = str(token_type)

        # Add tag to the text
        text_widget.tag_add(tag_name, start_index, end_index)

        # Tag styles
        if token_type in Token.Keyword:
            text_widget.tag_config(tag_name, foreground="blue")
        elif token_type in Token.String:
            text_widget.tag_config(tag_name, foreground="green")
        elif token_type in Token.Comment:
            text_widget.tag_config(tag_name, foreground="gray")
        elif token_type in Token.Literal.Number:
            text_widget.tag_config(tag_name, foreground="purple")
        elif token_type in Token.Operator:
            text_widget.tag_config(tag_name, foreground="orange")
        elif token_type in Token.Name.Function:
            text_widget.tag_config(tag_name, foreground="darkgreen")
        elif token_type in Token.Name.Class:
            text_widget.tag_config(tag_name, foreground="darkblue")


if __name__ == "__main__":
    gui().run()

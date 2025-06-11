from antlr4.error.ErrorListener import ErrorListener

class GreekErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.syntax_errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"[Syntax error]: {msg} in line {line}, column {column}!"
        self.syntax_errors.append(error_msg)

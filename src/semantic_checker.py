from src import ast


class SemanticChecker:

    WHITE = "\x1b[0m"
    YELLOW = "\033[1;33m" # we need to change f.e. for "colorama" package due to compatibility issues with ANSI color codes in some weird terminals
    RED = "\033[0;31m"
    PURPLE = "\033[0;35m"


    def __init__(self):
        self.symbol_table = {} # remember about scopes etc. to implement them
        self.errors = {} # not to exit after one error


    def finalise(self):
        # should be called after program analyzing
        if(1 in self.errors.values()):
            exit(1)


    def analyze(self, node: ast.ASTNode):
        # main method of the class, starts AST traversal
        method = getattr(self, f'analyze_{type(node).__name__}', None)
        if method:
            return method(node)
        #else:
        #    raise NotImplementedError(f"No analyze method for {type(node).__name__}")


    def generic(self, node: ast.ASTNode):
        # Maybe I should delete this, but who cares in this case?
        self.errors[f"{self.YELLOW}[Warning]: {self.WHITE}Unsupported AST tree node: {type(node).__name__} {self.PURPLE}(line {node.line}, column {node.column}){self.WHITE}!"] = 0


    def analyze_Program(self, node: ast.Program) -> tuple[
                                                        dict[
                                                            ast.Identifier,
                                                            list[
                                                                ast.VariableType,
                                                                ast.Literal | None
                                                            ]
                                                        ],
                                                        dict[str, int]
                                                    ]:
        # Undoubtedly the first node. Here the fun starts.
        for statement in node.statements:
            self.analyze(statement)
        
        errors_and_warnings =  "\n".join([message for message in self.errors.keys()])
        return self.symbol_table, errors_and_warnings


    def analyze_VariableDeclaration(self, node: ast.VariableDeclaration):
        if(node.id in self.symbol_table):
            if(node.varType == self.symbol_table[node.id][0]):
                self.errors[f"{self.YELLOW}[Warning]: {self.WHITE}Variable {node.id} redeclared {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}."] = 0
            else:
                self.errors[f"{self.RED}[Error]: {self.WHITE}Variable {node.id} redeclared with a different type than earlier ({node.varType} instead of {self.symbol_table[node.id][0]}) {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}!"] = 1
        else:
            self.symbol_table[node.id] = (node.varType, node.varValue)
        if(node.varValue):
            node.varValue.type = node.varType.__name__


    def analyze_Assignment(self, node: ast.Assignment):
        # node_type = self.analyze(node.value)
        node_value = self.analyze(node.value)

        if(node.id not in self.symbol_table):
            self.errors[f"{self.RED}[Error]: {self.WHITE}Undeclared variable: {node.id} {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}."] = 1
        elif(True != node_value): # quick fix, please overview later
            self.errors[f"{self.RED}[Error]: {self.WHITE}Type {node_value} of the assigned value {node.value} differs from the {node.id} variable type, which is {self.symbol_table[node.id][0]}, {self.PURPLE}line {node.line}, column {node.column}{self.WHITE}."] = 1


    def analyze_AdditionOperator(self, node: ast.AdditionOperator) -> bool | None:
        left_type = self.analyze(node.left)
        right_type = self.analyze(node.right)
        if(left_type != right_type):
            self.errors[f"{self.RED}[Error]: {self.WHITE}Incorrect adding -> left expression type: {left_type} differs from the right expression type: {right_type} {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}!"] = 1
        else: return True


    def analyze_MultiplicationOperator(self, node: ast.MultiplicationOperator) -> bool | None:
        left_type = self.analyze(node.left)
        right_type = self.analyze(node.right)
        if(left_type != right_type):
            self.errors[f"{self.RED}[Error]: {self.WHITE}Incorrect action -> left expression type: {left_type} differs from the right expression type: {right_type} {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}!"] = 1
        else: return True


    def analyze_Identifier(self, node: ast.Identifier) -> ast.VariableType | None:
        if(node.value in self.symbol_table):
            ident_val_type = self.symbol_table[node.value][0]
            node.type = ident_val_type.__name__
            return ident_val_type
        else:
            self.errors[f"{self.RED}[ERROR]: {self.WHITE}Unknown identifier reference: {node.value} {self.PURPLE}in line {node.line}, column {node.column}{self.WHITE}!"] = 1


    def analyze_IntLiteral(self, node: ast.IntLiteral) -> type:
        return int


    def analyze_FloatLiteral(self, node: ast.FloatLiteral) -> type:
        return float


    def analyze_CharLiteral(self, node: ast.CharLiteral) -> type:
        return str


    def analyze_StringLiteral(self, node: ast.StringLiteral) -> type:
        return str


    def analyze_IfStatement(self, node: ast.IfStatement):
        self.analyze(node.condition)
        for statement in node.then_branch: self.analyze(statement)
        for statement in node.else_branch: self.analyze(statement)


    def analyze_Condition(self, node: ast.Condition):
        # comparing different types -> a thing to overthink (several ways)
        self.analyze(node.left)
        self.analyze(node.right)


    def analyze_LoopStatement(self, node: ast.LoopStatement):
        self.analyze(node.condition)
        for statement in node.then: self.analyze(statement)
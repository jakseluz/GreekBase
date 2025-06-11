from src import ast


class CGenerator:
    
    def __init__(self, table: dict):
        self.symbol_table = table
        self.functions = list()


    def generate(self, node: ast.ASTNode):
        method = f'gen_{type(node).__name__}'
        if method:
            return getattr(self, method)(node)


    def gen_Program(self, node : ast.ASTNode):
        body = "\n".join([self.generate(statement) for statement in node.statements])
        return (
            f'#include <stdio.h>\n'
            + "\n".join(self.functions)
            + f'\nint main(){{\n{body}\nreturn 0;\n}}'
        )


    def gen_IntLiteral(self, node: ast.IntLiteral):
        return str(node.value)


    def gen_FloatLiteral(self, node: ast.FloatLiteral):
        return str(node.value)


    def gen_CharLiteral(self, node: ast.CharLiteral):
        return '\'' + node.value + '\''
    

    def gen_BoolLiteral(self, node: ast.BoolLiteral):
        return node.value


    def gen_StringLiteral(self, node: ast.StringLiteral):
        return "\"" + node.value + "\""


    def gen_Condition(self, node: ast.Condition):
        return " ".join(
            [
                self.generate(node.left) if node.left else "",
                "==" if node.operator == '=' else ("!=" if node.operator == "/=" else ("||" if node.operator == 'or' else ("&&" if node.operator == "and" else ("!" if node.operator == "not" else (node.operator if node.operator else ""))))),
                self.generate(node.right) if node.right else ""
            ]
        )


    def gen_MultiplicationOperator(self, node: ast.MultiplicationOperator):
        return " ".join(
            [
                self.generate(node.left),
                node.operator,
                self.generate(node.right)
            ]
        )


    def gen_AdditionOperator(self, node: ast.AdditionOperator):
        return " ".join(
            [
                self.generate(node.left),
                node.operator,
                self.generate(node.right)
            ]
        )


    def gen_ParenthesisExpression(self, node: ast.ParenthesisExpression):
        return f"( {self.generate(node.value)} )"


    def gen_Identifier(self, node: ast.Identifier):
        return node.value


    def gen_IfStatement(self, node: ast.IfStatement):
        return "\n".join(
            [
                f"if({self.generate(node.condition)})" + '{',

                *[self.generate(statement) for statement in node.then_branch],
                
                "}else{ " if len(node.else_branch) > 0 else ("}else{" if len(node.else_branch) == 1 else None), # TODO

                *[self.generate(statement) for statement in node.else_branch if len(node.else_branch) > 0],
                "}"
            ]
        )


    def gen_LoopStatement(self, node: ast.LoopStatement):
        return "\n".join(
            [
                f"while({self.generate(node.condition)})" + '{',
                *[self.generate(statement) for statement in node.then],
                '}'
            ]
        )


    def gen_Assignment(self, node: ast.Assignment):
        return f"{node.id} = {self.generate(node.value)};"


    def gen_PrintStatement(self, node: ast.PrintStatement): # TODO
        value_type = int
        value = 5
        if isinstance(node.value, ast.Identifier):
            value_type = self.symbol_table[node.value.value][0]
            value = node.value.value
        elif isinstance(node.value, ast.Literal):
            value_type = self.symbol_table[node.value.value][0]
            value = node.value.value
        elif isinstance(node.value, ast.FunctionCall):
            value_type = self.symbol_table[node.value.name][0]
            value = self.generate(node.value)
        else:
            value_type = self.symbol_table[node.value][0]
            value = node.value

        
        if(value_type == int):
            echo = f"\"%d\", {value}"
        elif(value_type == float):
            echo = f"\"%lf\", {value}"
        elif(value_type == str):
            echo = f"\"%s\", {value}"
        elif(value_type == bool):
            echo = f"\"%d\", {value}"

        return f"printf({echo});"


    def gen_VariableDeclaration(self, node: ast.VariableDeclaration):
        return f"{node.varType.__name__} {node.id}" + ((f" = {node.varValue.value}") if node.varValue is not None else '') + ';'
    

    def gen_FunctionDeclaration(self, node: ast.FunctionDeclaration):
        self.functions.append("\n".join(
            [
                (node.return_type if node.return_type != None else "void")
                    + " " + node.name
                    + "("
                    + ", ".join([self.generate(param) for param in node.parameters])
                    + "){",
                *[self.generate(statement) for statement in node.statements],
                "}"
            ]
        ))
        return ""
    

    def gen_FunctionCall(self, node: ast.FunctionCall):
        return f"{node.name}({", ".join([self.generate(param) for param in node.parameters] if node.parameters else [])});"
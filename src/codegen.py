from src import ast


class CGenerator:
    
    def __init__(self, table: dict):
        self.symbol_table = table


    def generate(self, node: ast.ASTNode):
        method = f'gen_{type(node).__name__}'
        if method:
            return getattr(self, method)(node)


    def gen_Program(self, node : ast.ASTNode):
        body = "\n".join([self.generate(statement) for statement in node.statements])
        return f'#include <stdio.h>\nint main(){{\n{body}\nreturn 0;\n}}'


    def gen_IntLiteral(self, node: ast.IntLiteral):
        return str(node.value)


    def gen_FloatLiteral(self, node: ast.FloatLiteral):
        return str(node.value)


    def gen_CharLiteral(self, node: ast.CharLiteral):
        return '\'' + node.value + '\''


    def gen_StringLiteral(self, node: ast.StringLiteral):
        return "\"" + node.value + "\""


    def gen_Condition(self, node: ast.Condition):
        return " ".join(
            [
                self.generate(node.left) if node.left else "",
                "==" if node.operator == '=' else ("!=" if node.operator == "/=" else ("||" if node.operator == 'or' else ("&&" if node.operator == "and" else ("!" if node.operator == "not" else node.operator)))),
                self.generate(node.right)
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
        value_type = self.symbol_table[node.value.value][0]
        if(value_type == int):
            value = f"\"%d\", {node.value.value}"
        elif(value_type == float):
            value = f"\"%lf\", {node.value.value}"
        elif(value_type == str):
            value = f"\"%s\", {node.value.value}"

        return f"printf({value});"


    def gen_VariableDeclaration(self, node: ast.VariableDeclaration):
        return f"{node.varType.__name__} {node.id}" + ((f" = {node.varValue.value}") if node.varValue is not None else '') + ';'
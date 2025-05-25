import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'antlr', 'generated')))
from GreekBaseParserVisitor import GreekBaseParserVisitor
from GreekBaseParser import GreekBaseParser
import ast

class GreekASTBuilder(GreekBaseParserVisitor):
    def visitProgram(self, ctx: GreekBaseParser.ProgramContext):
        # Visit all statements in the program
        return ast.Program([self.visit(stmt) for stmt in ctx.statement()])

    def visitVariableDeclaration(self, ctx: GreekBaseParser.VariableDeclarationContext):
        var_name = ctx.Identifier().getText()
        var_type = self.visit(ctx.literal())
        return ast.VariableDeclaration(var_type, var_name)

    def visitAssignment(self, ctx: GreekBaseParser.AssignmentContext):
        # Handles: IDENTIFIER := expression;
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        return ast.Assignment(var_name, value)


    """REMAINS OF THE INTERPRETER - to be changed"""
    def visitExpression(self, ctx: GreekBaseParser.ExpressionContext):
        # Returns value of literal or identifier
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            return self.memory.get(var_name, 0)  # default to 0 if undefined
        elif ctx.LIT_INT():
            return int(ctx.LIT_INT().getText())
        elif ctx.LIT_FLOAT():
            return float(ctx.LIT_FLOAT().getText())
        elif ctx.LIT_STRING():
            return ctx.LIT_STRING().getText().strip('"')
        else:
            return None

    def visitIfStatement(self, ctx: GreekBaseParser.IfStatementContext):
        # Handles if <cond> then {statements} [else {statements}] end if;
        condition_result = self.visit(ctx.condition())
        if condition_result:
            for stmt in ctx.nonDeclarativeStatement():
                self.visit(stmt)
        elif ctx.KW_ELSE():
            for stmt in ctx.nonDeclarativeStatement(1):  # 2nd block is else
                self.visit(stmt)

    def visitLoopStatement(self, ctx: GreekBaseParser.LoopStatementContext):
        # Handles while <cond> loop {statements} end loop;
        while self.visit(ctx.condition()):
            for stmt in ctx.nonDeclarativeStatement():
                self.visit(stmt)

    def visitCondition(self, ctx: GreekBaseParser.ConditionContext):
        # Evaluates condition: expr <relop> expr
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.relop().getText()
        return self.evalRelOp(left, right, op)

    def evalRelOp(self, left, right, op):
        # Evaluates relational operators
        if op == "=":
            return left == right
        elif op == "/=":
            return left != right
        elif op == "<":
            return left < right
        elif op == "<=":
            return left <= right
        elif op == ">":
            return left > right
        elif op == ">=":
            return left >= right
        else:
            raise Exception(f"Unknown operator {op}")

    def visitProcedureDeclaration(self, ctx: GreekBaseParser.ProcedureDeclarationContext):
        # Store the procedure definition by its name
        name = ctx.IDENTIFIER().getText()
        self.procedures[name] = ctx
        print(f"[define] procedure {name} stored.")

    def callProcedure(self, name, args):
        # Calls a previously stored procedure
        if name not in self.procedures:
            raise Exception(f"Undefined procedure: {name}")

        ctx = self.procedures[name]
        param_ctx = ctx.formalParameterPart()
        old_memory = self.memory.copy()

        # Bind arguments to parameter names
        if param_ctx:
            param_specs = param_ctx.parameterSpecification()
            for spec, value in zip(param_specs, args):
                ids = [id_tok.getText() for id_tok in spec.IDENTIFIER()]
                for id_ in ids:
                    self.memory[id_] = value

        # Run body
        for stmt in ctx.nonDeclarativeStatement():
            self.visit(stmt)

        # Restore previous memory (no side effects)
        self.memory = old_memory

    # Optional: stub for functionDeclaration if added
    def visitFunctionDeclaration(self, ctx: GreekBaseParser.FunctionDeclarationContext):
        print("[warn] Function support not implemented.")
    # Arithmetic
    def visitAddExpr(self, ctx: GreekBaseParser.AddExprContext):
        return self.visit(ctx.expression(0)) + self.visit(ctx.expression(1))

    def visitMinusExpr(self, ctx: GreekBaseParser.SubExprContext):
        return self.visit(ctx.expression(0)) - self.visit(ctx.expression(1))

    def visitMulExpr(self, ctx: GreekBaseParser.MulExprContext):
        return self.visit(ctx.expression(0)) * self.visit(ctx.expression(1))

    def visitDivExpr(self, ctx: GreekBaseParser.DivExprContext):
        return self.visit(ctx.expression(0)) / self.visit(ctx.expression(1))

    # Grouping
    def visitParensExpr(self, ctx: GreekBaseParser.ParensExprContext):
        return self.visit(ctx.expression())

    # Literals and identifiers
    def visitIntExpr(self, ctx: GreekBaseParser.IntExprContext):
        return int(ctx.LIT_INT().getText())

    def visitFloatExpr(self, ctx: GreekBaseParser.FloatExprContext):
        return float(ctx.LIT_FLOAT().getText())

    def visitStringExpr(self, ctx: GreekBaseParser.StringExprContext):
        return ctx.LIT_STRING().getText().strip('"')

    def visitIdExpr(self, ctx: GreekBaseParser.IdExprContext):
        var_name = ctx.IDENTIFIER().getText()
        return self.memory.get(var_name, 0)

    def visitPrintStatement(self, ctx:GreekBaseParser.PrintStatementContext):
        text = self.visit(ctx.expression())
        print(text)
        return None

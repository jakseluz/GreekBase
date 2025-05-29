import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'antlr', 'generated')))
from GreekBaseParserVisitor import GreekBaseParserVisitor
from GreekBaseParser import GreekBaseParser
import astGreek as ast

class GreekASTBuilder(GreekBaseParserVisitor):
    def visitProgram(self, ctx: GreekBaseParser.ProgramContext):
        # Visit all statements in the program
        return ast.Program(ctx.start.line, ctx.start.column, [self.visit(stmt) for stmt in ctx.statement()])

    def visitVariableDeclaration(self, ctx: GreekBaseParser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.varType())
        if ctx.expression():
            var_value = self.visit(ctx.expression())
        else:
            var_value = None
        return ast.VariableDeclaration(ctx.start.line, ctx.start.column, var_type, var_name, var_value)
    
    def visitVarType(self, ctx: GreekBaseParser.VarTypeContext):
        if ctx.KW_INT():
            return int
        elif ctx.KW_FLOAT():
            return float
        elif ctx.KW_CHAR():
            return str
        elif ctx.KW_STRING():
            return str
        else:
            return None


    def visitAssignment(self, ctx: GreekBaseParser.AssignmentContext):
        # Handles: IDENTIFIER := expression;
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        return ast.Assignment(ctx.start.line, ctx.start.column, var_name, value)


    def visitExpression(self, ctx: GreekBaseParser.ExpressionContext):
        token = ctx.IDENTIFIER
        if ctx.literal():
            return self.visit(ctx.literal())
        
    def visitIdExpr(self, ctx: GreekBaseParser.IdExprContext):
        if ctx.IDENTIFIER():
            return ast.Identifier(ctx.start.line, ctx.start.column, ctx.IDENTIFIER().getText(), None)

    def visitLiteral(self, ctx: GreekBaseParser.LiteralContext):
        if ctx.LIT_INT():
            return ast.IntLiteral(ctx.start.line, ctx.start.column, int(ctx.LIT_INT().getText()))
        elif ctx.LIT_FLOAT():
            return ast.FloatLiteral(ctx.start.line, ctx.start.column, float(ctx.LIT_FLOAT().getText()))
        elif ctx.LIT_STRING():
            return ast.StringLiteral(ctx.start.line, ctx.start.column, ctx.LIT_STRING().getText().strip('"'))
        elif ctx.LIT_CHAR():
            return ast.CharLiteral(ctx.start.line, ctx.start.column, ctx.LIT_CHAR().getText().strip("'")[0])

    def visitIfStatement(self, ctx: GreekBaseParser.IfStatementContext):
        # note that there are two possibilities of IF "scoping"
        # Handles if <cond> then {statements} [else {statements}] end if;
        condition = self.visit(ctx.condition())
        then_branch = [self.visit(nondecl_stmt) for nondecl_stmt in ctx.thenBranch]
        else_branch = [self.visit(nondecl_stmt) for nondecl_stmt in ctx.elseBranch] if ctx.elseBranch else []
        return ast.IfStatement(ctx.start.line, ctx.start.column, condition, then_branch, else_branch)

    def visitLoopStatement(self, ctx: GreekBaseParser.LoopStatementContext):
        # Handles while <cond> loop {statements} end loop;
        condition = self.visit(ctx.condition())
        then = [self.visit(nondecl_stmt) for nondecl_stmt in ctx.nonDeclarativeStatement()]
        return ast.LoopStatement(ctx.start.line, ctx.start.column, condition, then)

    def visitCondition(self, ctx: GreekBaseParser.ConditionContext):
        # Handles condition: expr <relop> expr
        left = self.visit(ctx.expression(0))
        operator = ctx.relop().getText()
        right = self.visit(ctx.expression(1))
        return ast.Condition(ctx.start.line, ctx.start.column, left, operator, right)


    def visitProcedureDeclaration(self, ctx: GreekBaseParser.ProcedureDeclarationContext):
        # Store the procedure definition by its name
        name = ctx.IDENTIFIER().getText()
        formalParameterPart = self.visit(ctx.formalParameterPart()) if ctx.formalParameterPart() else []
        body = [self.visit(nondecl_stmt) for nondecl_stmt in ctx.nonDeclarativeStatement()]
        return ast.Procedure(ctx.start.line, ctx.start.column, name, formalParameterPart, body)


    # Optional: stub for functionDeclaration if added
    def visitFunctionDeclaration(self, ctx: GreekBaseParser.FunctionDeclarationContext):
        print("[warn] Function support not implemented.")
        # return NotImplementedError("[warn] Function support not implemented.")
        return None
    
    # Arithmetic
    def visitAddExpr(self, ctx: GreekBaseParser.AddExprContext):
        left = self.visit(ctx.expression(0))
        operator = '+'
        right = self.visit(ctx.expression(1))
        return ast.AdditionOperator(ctx.start.line, ctx.start.column, left, operator, right)

    def visitSubExpr(self, ctx: GreekBaseParser.SubExprContext):
        left = self.visit(ctx.expression(0))
        operator = '-'
        right = self.visit(ctx.expression(1))
        return ast.AdditionOperator(ctx.start.line, ctx.start.column, left, operator, right)

    def visitMulExpr(self, ctx: GreekBaseParser.MulExprContext):
        left = self.visit(ctx.expression(0))
        operator = '*'
        right = self.visit(ctx.expression(1))
        return ast.MultiplicationOperator(ctx.start.line, ctx.start.column, left, operator, right)

    def visitDivExpr(self, ctx: GreekBaseParser.DivExprContext):
        left = self.visit(ctx.expression(0))
        operator = '/'
        right = self.visit(ctx.expression(1))
        return ast.MultiplicationOperator(ctx.start.line, ctx.start.column, left, operator, right)

    # Grouping
    def visitParensExpr(self, ctx: GreekBaseParser.ParensExprContext):
        return ast.ParenthesisExpression(
            ctx.start.line, ctx.start.column, 
            self.visit(ctx.expression())
        )

    # Printing
    def visitPrintStatement(self, ctx:GreekBaseParser.PrintStatementContext):
        return ast.PrintStatement(
            ctx.start.line, ctx.start.column, 
            self.visit(ctx.expression())
        )

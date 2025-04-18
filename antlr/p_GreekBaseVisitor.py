# Generated from p_GreekBase.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .p_GreekBase import p_GreekBase
else:
    from p_GreekBase import p_GreekBase

# This class defines a complete generic visitor for a parse tree produced by p_GreekBase.

class p_GreekBaseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by p_GreekBase#program.
    def visitProgram(self, ctx:p_GreekBase.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#statement.
    def visitStatement(self, ctx:p_GreekBase.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#ifStatement.
    def visitIfStatement(self, ctx:p_GreekBase.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#loopStatement.
    def visitLoopStatement(self, ctx:p_GreekBase.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#assignment.
    def visitAssignment(self, ctx:p_GreekBase.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:p_GreekBase.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:p_GreekBase.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#condition.
    def visitCondition(self, ctx:p_GreekBase.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#expression.
    def visitExpression(self, ctx:p_GreekBase.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by p_GreekBase#relop.
    def visitRelop(self, ctx:p_GreekBase.RelopContext):
        return self.visitChildren(ctx)



del p_GreekBase
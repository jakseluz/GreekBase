# Generated from GreekBaseParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GreekBaseParser import GreekBaseParser
else:
    from GreekBaseParser import GreekBaseParser

# This class defines a complete generic visitor for a parse tree produced by GreekBaseParser.

class GreekBaseParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GreekBaseParser#program.
    def visitProgram(self, ctx:GreekBaseParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#literal.
    def visitLiteral(self, ctx:GreekBaseParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#statement.
    def visitStatement(self, ctx:GreekBaseParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#nonDeclarativeStatement.
    def visitNonDeclarativeStatement(self, ctx:GreekBaseParser.NonDeclarativeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#ifStatement.
    def visitIfStatement(self, ctx:GreekBaseParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#loopStatement.
    def visitLoopStatement(self, ctx:GreekBaseParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#printStatement.
    def visitPrintStatement(self, ctx:GreekBaseParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#assignment.
    def visitAssignment(self, ctx:GreekBaseParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#formalParameterPart.
    def visitFormalParameterPart(self, ctx:GreekBaseParser.FormalParameterPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#parameterSpecification.
    def visitParameterSpecification(self, ctx:GreekBaseParser.ParameterSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#modeSpecifier.
    def visitModeSpecifier(self, ctx:GreekBaseParser.ModeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:GreekBaseParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:GreekBaseParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#condition.
    def visitCondition(self, ctx:GreekBaseParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#stringExpr.
    def visitStringExpr(self, ctx:GreekBaseParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#floatExpr.
    def visitFloatExpr(self, ctx:GreekBaseParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#intExpr.
    def visitIntExpr(self, ctx:GreekBaseParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#addExpr.
    def visitAddExpr(self, ctx:GreekBaseParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#mulExpr.
    def visitMulExpr(self, ctx:GreekBaseParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#divExpr.
    def visitDivExpr(self, ctx:GreekBaseParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#parensExpr.
    def visitParensExpr(self, ctx:GreekBaseParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#subExpr.
    def visitSubExpr(self, ctx:GreekBaseParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#idExpr.
    def visitIdExpr(self, ctx:GreekBaseParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#relop.
    def visitRelop(self, ctx:GreekBaseParser.RelopContext):
        return self.visitChildren(ctx)



del GreekBaseParser
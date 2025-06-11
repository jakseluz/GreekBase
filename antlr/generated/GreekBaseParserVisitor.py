# Generated from antlr/GreekBaseParser.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by GreekBaseParser#expressionStatement.
    def visitExpressionStatement(self, ctx:GreekBaseParser.ExpressionStatementContext):
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


    # Visit a parse tree produced by GreekBaseParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:GreekBaseParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#returnStatement.
    def visitReturnStatement(self, ctx:GreekBaseParser.ReturnStatementContext):
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


    # Visit a parse tree produced by GreekBaseParser#functionCall.
    def visitFunctionCall(self, ctx:GreekBaseParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#condition.
    def visitCondition(self, ctx:GreekBaseParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#conditionOr.
    def visitConditionOr(self, ctx:GreekBaseParser.ConditionOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#conditionAnd.
    def visitConditionAnd(self, ctx:GreekBaseParser.ConditionAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#conditionNot.
    def visitConditionNot(self, ctx:GreekBaseParser.ConditionNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#conditionAtom.
    def visitConditionAtom(self, ctx:GreekBaseParser.ConditionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#expression.
    def visitExpression(self, ctx:GreekBaseParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#addExpr.
    def visitAddExpr(self, ctx:GreekBaseParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#mulExpr.
    def visitMulExpr(self, ctx:GreekBaseParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#atom.
    def visitAtom(self, ctx:GreekBaseParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#relop.
    def visitRelop(self, ctx:GreekBaseParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GreekBaseParser#varType.
    def visitVarType(self, ctx:GreekBaseParser.VarTypeContext):
        return self.visitChildren(ctx)



del GreekBaseParser
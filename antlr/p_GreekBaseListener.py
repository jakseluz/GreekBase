# Generated from p_GreekBase.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .p_GreekBase import p_GreekBase
else:
    from p_GreekBase import p_GreekBase

# This class defines a complete listener for a parse tree produced by p_GreekBase.
class p_GreekBaseListener(ParseTreeListener):

    # Enter a parse tree produced by p_GreekBase#program.
    def enterProgram(self, ctx:p_GreekBase.ProgramContext):
        pass

    # Exit a parse tree produced by p_GreekBase#program.
    def exitProgram(self, ctx:p_GreekBase.ProgramContext):
        pass


    # Enter a parse tree produced by p_GreekBase#statement.
    def enterStatement(self, ctx:p_GreekBase.StatementContext):
        pass

    # Exit a parse tree produced by p_GreekBase#statement.
    def exitStatement(self, ctx:p_GreekBase.StatementContext):
        pass


    # Enter a parse tree produced by p_GreekBase#ifStatement.
    def enterIfStatement(self, ctx:p_GreekBase.IfStatementContext):
        pass

    # Exit a parse tree produced by p_GreekBase#ifStatement.
    def exitIfStatement(self, ctx:p_GreekBase.IfStatementContext):
        pass


    # Enter a parse tree produced by p_GreekBase#loopStatement.
    def enterLoopStatement(self, ctx:p_GreekBase.LoopStatementContext):
        pass

    # Exit a parse tree produced by p_GreekBase#loopStatement.
    def exitLoopStatement(self, ctx:p_GreekBase.LoopStatementContext):
        pass


    # Enter a parse tree produced by p_GreekBase#assignment.
    def enterAssignment(self, ctx:p_GreekBase.AssignmentContext):
        pass

    # Exit a parse tree produced by p_GreekBase#assignment.
    def exitAssignment(self, ctx:p_GreekBase.AssignmentContext):
        pass


    # Enter a parse tree produced by p_GreekBase#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx:p_GreekBase.ProcedureDeclarationContext):
        pass

    # Exit a parse tree produced by p_GreekBase#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx:p_GreekBase.ProcedureDeclarationContext):
        pass


    # Enter a parse tree produced by p_GreekBase#condition.
    def enterCondition(self, ctx:p_GreekBase.ConditionContext):
        pass

    # Exit a parse tree produced by p_GreekBase#condition.
    def exitCondition(self, ctx:p_GreekBase.ConditionContext):
        pass


    # Enter a parse tree produced by p_GreekBase#expression.
    def enterExpression(self, ctx:p_GreekBase.ExpressionContext):
        pass

    # Exit a parse tree produced by p_GreekBase#expression.
    def exitExpression(self, ctx:p_GreekBase.ExpressionContext):
        pass


    # Enter a parse tree produced by p_GreekBase#relop.
    def enterRelop(self, ctx:p_GreekBase.RelopContext):
        pass

    # Exit a parse tree produced by p_GreekBase#relop.
    def exitRelop(self, ctx:p_GreekBase.RelopContext):
        pass



del p_GreekBase
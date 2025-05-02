from antlr4 import *
from .p_GreekBaseVisitor import p_GreekBaseVisitor #import wewnątrz pakietu (kropka na poczatku)
from .p_GreekBase import p_GreekBase #import wewnątrz pakietu (kropka na poczatku)
class GreekInterpreter(p_GreekBaseVisitor):
    def __init__(self):
        self.memory = {} # Dictionary for variables
    def enterAssignment(self, ctx:p_GreekBaseParser.AssignmentContext):
        variable_name = ctx.ID().getText()
    def exitAssignment(self, ctx:p_GreekBaseParser.AssignmentContext):
        value = self.visit(ctx.expression())
        self.memory[self.current_variable] = value
        print(f"Przypisano {value} do zmiennej {self.current_variable}")
        del self.current_variable
#TODO add enter and exit methods override them from listener 

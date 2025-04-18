from antlr4 import *
from .p_GreekBaseListener import p_GreekBaseListener #import wewnątrz pakietu (kropka na poczatku)
from .p_GreekBaseParser import p_GreekBaseParser #import wewnątrz pakietu (kropka na poczatku)
class GreekInterpreter(p_GreekBaseListener):
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

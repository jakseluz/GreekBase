from antlr.generated import GreekBaseParser, GreekBaseParserVisitor
from src import ast


class GreekASTBuilder(GreekBaseParserVisitor):
    def visitProgram(self, ctx: GreekBaseParser.ProgramContext):
        # Visit all statements in the program
        return ast.Program(ctx.start.line, ctx.start.column, [self.visit(stmt) for stmt in ctx.statement()])


    def visitVariableDeclaration(self, ctx: GreekBaseParser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.varType())
        if ctx.expression():
            if ctx.expression():
                var_value = self.visit(ctx.expression())
            elif ctx.condition():
                var_value = self.visit(ctx.condition())
        else:
            var_value = None
        return ast.VariableDeclaration(ctx.start.line, ctx.start.column, var_type, var_name, var_value)


    def visitVarType(self, ctx: GreekBaseParser.VarTypeContext):
        if ctx.KW_INT():
            return int
        elif ctx.KW_FLOAT():
            return float
        elif ctx.KW_CHAR():
            return "char"
        elif ctx.KW_BOOL():
            return bool
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
        return self.visit(ctx.addExpr())


    def visitLiteral(self, ctx: GreekBaseParser.LiteralContext):
        if ctx.LIT_INT():
            return ast.IntLiteral(ctx.start.line, ctx.start.column, int(ctx.LIT_INT().getText()))
        elif ctx.LIT_FLOAT():
            return ast.FloatLiteral(ctx.start.line, ctx.start.column, float(ctx.LIT_FLOAT().getText()))
        elif ctx.LIT_BOOL():
            return ast.BoolLiteral(ctx.start.line, ctx.start.column, ctx.LIT_BOOL().getText())
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

    """
    def visitCondition(self, ctx: GreekBaseParser.ConditionContext):
        # Handles condition: expr <relop> expr
        left = self.visit(ctx.left_expr)\
            if ctx.left_expr\
              else (None if ctx.negated\
                    else (self.visit(ctx.condition(0))))
        operator = ctx.relop().getText()\
            if ctx.relop()\
                else (ctx.OP_OR().getText() if ctx.OP_OR()\
                      else (ctx.OP_AND().getText() if ctx.OP_AND()\
                            else (ctx.OP_NOT().getText() if ctx.OP_NOT()\
                                  else None)))
        right = self.visit(ctx.right_expr) if ctx.left_expr\
            else (self.visit(ctx.negated) if ctx.negated\
                  else (self.visit(ctx.condition(1))))
        return ast.Condition(ctx.start.line, ctx.start.column, left, operator, right)
    """
    def visitCondition(self, ctx):
        return self.visit(ctx.conditionOr())

    def visitConditionOr(self, ctx: GreekBaseParser.ConditionOrContext):
        terms = [self.visit(term) for term in ctx.conditionAnd()]
        if len(terms) == 1:
            return terms[0]
        
        astnode = terms[0]
        for i, right in enumerate(terms[1:], start = 1):
            operator = ctx.OP_OR()[i - 1].getText()
            astnode = ast.Condition(
                line = ctx.start.line,
                column = ctx.start.column,
                left = astnode,
                operator = operator,
                right = right
            )
        return astnode


    def visitConditionAnd(self, ctx: GreekBaseParser.ConditionAndContext):
        factors = [self.visit(factor) for factor in ctx.conditionNot()]
        if len(factors) == 1:
            return factors[0]
        
        astnode = factors[0]
        for i, right in enumerate(factors[1:], start = 1):
            operator = ctx.OP_AND()[i - 1].getText()
            astnode = ast.Condition(
                line = ctx.start.line,
                column = ctx.start.column,
                left = astnode,
                operator = operator,
                right = right
            )
        return astnode
    
    def visitConditionNot(self, ctx: GreekBaseParser.ConditionNotContext):
        if ctx.OP_NOT():
            operator = ctx.OP_NOT().getText()  
            right = self.visit(ctx.conditionNot())  
            return ast.Condition(ctx.start.line, ctx.start.column, None, operator, right)
        else:
            return self.visit(ctx.conditionAtom())
    

    def visitConditionAtom(self, ctx: GreekBaseParser.ConditionAtomContext):
        if ctx.relop():
            left = self.visit(ctx.expression(0))
            operator = ctx.relop().getText()
            right = self.visit(ctx.expression(1))
            return ast.Condition(ctx.start.line, ctx.start.column, left, operator, right)
        elif ctx.OP_LPAREN():
            return self.visit(ctx.condition())


    def visitExpressionStatement(self, ctx: GreekBaseParser.ExpressionStatementContext):
        return self.visit(ctx.expression())


    def visitProcedureDeclaration(self, ctx: GreekBaseParser.ProcedureDeclarationContext):
        # Store the procedure definition by its name
        name = ctx.IDENTIFIER().getText()
        formalParameterPart = self.visit(ctx.formalParameterPart()) if ctx.formalParameterPart() else []
        body = [self.visit(nondecl_stmt) for nondecl_stmt in ctx.nonDeclarativeStatement()]
        return ast.Procedure(ctx.start.line, ctx.start.column, name, formalParameterPart, body)


    # functions
    def visitFunctionDeclaration(self, ctx: GreekBaseParser.FunctionDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        type = self.visit(ctx.varType()) if ctx.varType() else None
        parameter_decl = [self.visit(decl) for decl in ctx.variableDeclaration()]
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        return ast.FunctionDeclaration(ctx.start.line, ctx.start.column, name, parameter_decl, type, statements)
    

    def visitFunctionCall(self, ctx: GreekBaseParser.FunctionCallContext):
        name = ctx.IDENTIFIER().getText()
        parameters = [self.visit(param) for param in ctx.expression()] if ctx.expression() else []
        return ast.FunctionCall(ctx.start.line, ctx.start.column, name, parameters)


    # Arithmetic and not only
    def visitAddExpr(self, ctx: GreekBaseParser.AddExprContext):
        if len(ctx.mulExpr()) == 1:
            return self.visit(ctx.mulExpr(0))
        
        left = self.visit(ctx.mulExpr(0))
        operator = ctx.OP_ADD()[0].getText()\
            if ctx.OP_ADD()\
                else (ctx.OP_SUB()[0].getText() if ctx.OP_SUB()\
                      else None)
        right = self.visit(ctx.mulExpr(1)) if ctx.mulExpr(1) else None
        return ast.AdditionOperator(ctx.start.line, ctx.start.column, left, operator, right)


    def visitMulExpr(self, ctx: GreekBaseParser.MulExprContext):
        if len(ctx.atom()) == 1:
            return self.visit(ctx.atom(0))
        
        left = self.visit(ctx.atom(0))
        operator = ctx.OP_MUL()[0].getText()\
            if ctx.OP_MUL()\
                else (ctx.OP_DIV()[0].getText() if ctx.OP_DIV()\
                      else (ctx.OP_MOD()[0].getText() if ctx.OP_MOD()\
                            else None))
        right = self.visit(ctx.atom(1)) if ctx.atom(1) else None
        return ast.MultiplicationOperator(ctx.start.line, ctx.start.column, left, operator, right)
    

    def visitAtom(self, ctx: GreekBaseParser.AtomContext):
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.IDENTIFIER():
            return ast.Identifier(ctx.start.line, ctx.start.column, ctx.IDENTIFIER().getText(), None)
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression() and ctx.OP_LPAREN() and ctx.OP_RPAREN():
            return ast.ParenthesisExpression(
                ctx.start.line, ctx.start.column, 
                self.visit(ctx.expression())
            )


    # Printing
    def visitPrintStatement(self, ctx:GreekBaseParser.PrintStatementContext):
        if ctx.IDENTIFIER():
            value = ctx.IDENTIFIER().getText()
        elif ctx.literal():
            value = self.visit(ctx.literal())
        elif ctx.functionCall():
            value = self.visit(ctx.functionCall())

        return ast.PrintStatement(
            ctx.start.line, ctx.start.column,
            value
        )

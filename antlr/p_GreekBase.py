# Generated from p_GreekBase.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,3,2,51,8,2,1,2,1,2,
        1,2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,2,1,2,5,2,65,8,2,10,2,
        12,2,68,9,2,3,2,70,8,2,1,2,3,2,73,8,2,1,3,1,3,1,3,1,3,5,3,79,8,3,
        10,3,12,3,82,9,3,1,3,1,3,1,3,1,3,1,3,5,3,89,8,3,10,3,12,3,92,9,3,
        1,3,3,3,95,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,107,8,
        5,10,5,12,5,110,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        122,8,6,10,6,12,6,125,9,6,3,6,127,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,
        6,135,8,6,10,6,12,6,138,9,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,2,0,55,57,59,
        59,1,0,32,37,159,0,23,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,74,1,0,
        0,0,8,96,1,0,0,0,10,101,1,0,0,0,12,115,1,0,0,0,14,143,1,0,0,0,16,
        147,1,0,0,0,18,149,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,
        0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,
        5,0,0,1,27,1,1,0,0,0,28,33,3,4,2,0,29,33,3,6,3,0,30,33,3,8,4,0,31,
        33,3,10,5,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,
        0,0,33,3,1,0,0,0,34,35,5,3,0,0,35,72,3,14,7,0,36,40,5,4,0,0,37,39,
        3,2,1,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,
        41,50,1,0,0,0,42,40,1,0,0,0,43,47,5,5,0,0,44,46,3,2,1,0,45,44,1,
        0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,51,1,0,0,0,49,
        47,1,0,0,0,50,43,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,2,0,
        0,53,54,5,3,0,0,54,73,5,48,0,0,55,59,5,29,0,0,56,58,3,2,1,0,57,56,
        1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,69,1,0,0,0,
        61,59,1,0,0,0,62,66,5,5,0,0,63,65,3,2,1,0,64,63,1,0,0,0,65,68,1,
        0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,69,
        62,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,30,0,0,72,36,1,0,
        0,0,72,55,1,0,0,0,73,5,1,0,0,0,74,75,5,7,0,0,75,94,3,14,7,0,76,80,
        5,6,0,0,77,79,3,2,1,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,
        80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,2,0,0,84,85,5,
        6,0,0,85,95,5,48,0,0,86,90,5,29,0,0,87,89,3,2,1,0,88,87,1,0,0,0,
        89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,
        0,0,0,93,95,5,30,0,0,94,76,1,0,0,0,94,86,1,0,0,0,95,7,1,0,0,0,96,
        97,5,59,0,0,97,98,5,31,0,0,98,99,3,16,8,0,99,100,5,48,0,0,100,9,
        1,0,0,0,101,102,5,11,0,0,102,103,5,59,0,0,103,104,5,13,0,0,104,108,
        5,1,0,0,105,107,3,2,1,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,
        5,2,0,0,112,113,5,11,0,0,113,114,5,48,0,0,114,11,1,0,0,0,115,116,
        5,12,0,0,116,117,5,59,0,0,117,126,5,51,0,0,118,123,5,59,0,0,119,
        120,5,49,0,0,120,122,5,59,0,0,121,119,1,0,0,0,122,125,1,0,0,0,123,
        121,1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,126,
        118,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,5,52,0,0,129,
        130,5,47,0,0,130,131,5,59,0,0,131,132,5,13,0,0,132,136,5,1,0,0,133,
        135,3,2,1,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,
        137,1,0,0,0,137,139,1,0,0,0,138,136,1,0,0,0,139,140,5,2,0,0,140,
        141,5,12,0,0,141,142,5,48,0,0,142,13,1,0,0,0,143,144,3,16,8,0,144,
        145,3,18,9,0,145,146,3,16,8,0,146,15,1,0,0,0,147,148,7,0,0,0,148,
        17,1,0,0,0,149,150,7,1,0,0,150,19,1,0,0,0,16,23,32,40,47,50,59,66,
        69,72,80,90,94,108,123,126,136
    ]

class p_GreekBase ( Parser ):

    grammarFileName = "p_GreekBase.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'begin'", "'end'", "'if'", "'then'", 
                     "'else'", "'loop'", "'while'", "'for'", "'in'", "'return'", 
                     "'procedure'", "'function'", "'is'", "'type'", "'record'", 
                     "'array'", "'of'", "'var'", "'const'", "'generic'", 
                     "'package'", "'use'", "'with'", "'private'", "'protected'", 
                     "'override'", "'class'", "'new'", "'{'", "'}'", "':='", 
                     "'='", "'/='", "'<'", "'<='", "'>'", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'mod'", "'and'", "'or'", "'not'", 
                     "'.'", "':'", "';'", "','", "'=>'", "'('", "')'", "'['", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "KW_BEGIN", "KW_END", "KW_IF", "KW_THEN", 
                      "KW_ELSE", "KW_LOOP", "KW_WHILE", "KW_FOR", "KW_IN", 
                      "KW_RETURN", "KW_PROCEDURE", "KW_FUNCTION", "KW_IS", 
                      "KW_TYPE", "KW_RECORD", "KW_ARRAY", "KW_OF", "KW_VAR", 
                      "KW_CONST", "KW_GENERIC", "KW_PACKAGE", "KW_USE", 
                      "KW_WITH", "KW_PRIVATE", "KW_PROTECTED", "KW_OVERRIDE", 
                      "KW_CLASS", "KW_NEW", "KW_LCURL", "KW_RCURL", "OP_ASSIGN", 
                      "OP_EQUAL", "OP_NOT_EQUAL", "OP_LESS", "OP_LESS_EQ", 
                      "OP_GREATER", "OP_GREATER_EQ", "OP_PLUS", "OP_MINUS", 
                      "OP_MUL", "OP_DIV", "OP_MOD", "OP_AND", "OP_OR", "OP_NOT", 
                      "OP_DOT", "OP_COLON", "OP_SEMICOLON", "OP_COMMA", 
                      "OP_ARROW", "OP_LPAREN", "OP_RPAREN", "OP_LBRACKET", 
                      "OP_RBRACKET", "LIT_INT", "LIT_FLOAT", "LIT_STRING", 
                      "LIT_CHAR", "IDENTIFIER", "LINE_COMMENT", "MULTILINE_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_ifStatement = 2
    RULE_loopStatement = 3
    RULE_assignment = 4
    RULE_procedureDeclaration = 5
    RULE_functionDeclaration = 6
    RULE_condition = 7
    RULE_expression = 8
    RULE_relop = 9

    ruleNames =  [ "program", "statement", "ifStatement", "loopStatement", 
                   "assignment", "procedureDeclaration", "functionDeclaration", 
                   "condition", "expression", "relop" ]

    EOF = Token.EOF
    KW_BEGIN=1
    KW_END=2
    KW_IF=3
    KW_THEN=4
    KW_ELSE=5
    KW_LOOP=6
    KW_WHILE=7
    KW_FOR=8
    KW_IN=9
    KW_RETURN=10
    KW_PROCEDURE=11
    KW_FUNCTION=12
    KW_IS=13
    KW_TYPE=14
    KW_RECORD=15
    KW_ARRAY=16
    KW_OF=17
    KW_VAR=18
    KW_CONST=19
    KW_GENERIC=20
    KW_PACKAGE=21
    KW_USE=22
    KW_WITH=23
    KW_PRIVATE=24
    KW_PROTECTED=25
    KW_OVERRIDE=26
    KW_CLASS=27
    KW_NEW=28
    KW_LCURL=29
    KW_RCURL=30
    OP_ASSIGN=31
    OP_EQUAL=32
    OP_NOT_EQUAL=33
    OP_LESS=34
    OP_LESS_EQ=35
    OP_GREATER=36
    OP_GREATER_EQ=37
    OP_PLUS=38
    OP_MINUS=39
    OP_MUL=40
    OP_DIV=41
    OP_MOD=42
    OP_AND=43
    OP_OR=44
    OP_NOT=45
    OP_DOT=46
    OP_COLON=47
    OP_SEMICOLON=48
    OP_COMMA=49
    OP_ARROW=50
    OP_LPAREN=51
    OP_RPAREN=52
    OP_LBRACKET=53
    OP_RBRACKET=54
    LIT_INT=55
    LIT_FLOAT=56
    LIT_STRING=57
    LIT_CHAR=58
    IDENTIFIER=59
    LINE_COMMENT=60
    MULTILINE_COMMENT=61
    WS=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(p_GreekBase.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.StatementContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.StatementContext,i)


        def getRuleIndex(self):
            return p_GreekBase.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = p_GreekBase.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(p_GreekBase.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(p_GreekBase.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(p_GreekBase.LoopStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(p_GreekBase.AssignmentContext,0)


        def procedureDeclaration(self):
            return self.getTypedRuleContext(p_GreekBase.ProcedureDeclarationContext,0)


        def getRuleIndex(self):
            return p_GreekBase.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = p_GreekBase.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.loopStatement()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.assignment()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.procedureDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.KW_IF)
            else:
                return self.getToken(p_GreekBase.KW_IF, i)

        def condition(self):
            return self.getTypedRuleContext(p_GreekBase.ConditionContext,0)


        def KW_THEN(self):
            return self.getToken(p_GreekBase.KW_THEN, 0)

        def KW_END(self):
            return self.getToken(p_GreekBase.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(p_GreekBase.OP_SEMICOLON, 0)

        def KW_LCURL(self):
            return self.getToken(p_GreekBase.KW_LCURL, 0)

        def KW_RCURL(self):
            return self.getToken(p_GreekBase.KW_RCURL, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.StatementContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.StatementContext,i)


        def KW_ELSE(self):
            return self.getToken(p_GreekBase.KW_ELSE, 0)

        def getRuleIndex(self):
            return p_GreekBase.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = p_GreekBase.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(p_GreekBase.KW_IF)
            self.state = 35
            self.condition()
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 36
                self.match(p_GreekBase.KW_THEN)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 37
                    self.statement()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 43
                    self.match(p_GreekBase.KW_ELSE)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                        self.state = 44
                        self.statement()
                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 52
                self.match(p_GreekBase.KW_END)
                self.state = 53
                self.match(p_GreekBase.KW_IF)
                self.state = 54
                self.match(p_GreekBase.OP_SEMICOLON)
                pass
            elif token in [29]:
                self.state = 55
                self.match(p_GreekBase.KW_LCURL)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 56
                    self.statement()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 62
                    self.match(p_GreekBase.KW_ELSE)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                        self.state = 63
                        self.statement()
                        self.state = 68
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 71
                self.match(p_GreekBase.KW_RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHILE(self):
            return self.getToken(p_GreekBase.KW_WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(p_GreekBase.ConditionContext,0)


        def KW_LOOP(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.KW_LOOP)
            else:
                return self.getToken(p_GreekBase.KW_LOOP, i)

        def KW_LCURL(self):
            return self.getToken(p_GreekBase.KW_LCURL, 0)

        def KW_RCURL(self):
            return self.getToken(p_GreekBase.KW_RCURL, 0)

        def KW_END(self):
            return self.getToken(p_GreekBase.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(p_GreekBase.OP_SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.StatementContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.StatementContext,i)


        def getRuleIndex(self):
            return p_GreekBase.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = p_GreekBase.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(p_GreekBase.KW_WHILE)
            self.state = 75
            self.condition()
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 76
                self.match(p_GreekBase.KW_LOOP)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 77
                    self.statement()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                self.match(p_GreekBase.KW_END)
                self.state = 84
                self.match(p_GreekBase.KW_LOOP)
                self.state = 85
                self.match(p_GreekBase.OP_SEMICOLON)
                pass
            elif token in [29]:
                self.state = 86
                self.match(p_GreekBase.KW_LCURL)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 87
                    self.statement()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 93
                self.match(p_GreekBase.KW_RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(p_GreekBase.IDENTIFIER, 0)

        def OP_ASSIGN(self):
            return self.getToken(p_GreekBase.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(p_GreekBase.ExpressionContext,0)


        def OP_SEMICOLON(self):
            return self.getToken(p_GreekBase.OP_SEMICOLON, 0)

        def getRuleIndex(self):
            return p_GreekBase.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = p_GreekBase.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 97
            self.match(p_GreekBase.OP_ASSIGN)
            self.state = 98
            self.expression()
            self.state = 99
            self.match(p_GreekBase.OP_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PROCEDURE(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.KW_PROCEDURE)
            else:
                return self.getToken(p_GreekBase.KW_PROCEDURE, i)

        def IDENTIFIER(self):
            return self.getToken(p_GreekBase.IDENTIFIER, 0)

        def KW_IS(self):
            return self.getToken(p_GreekBase.KW_IS, 0)

        def KW_BEGIN(self):
            return self.getToken(p_GreekBase.KW_BEGIN, 0)

        def KW_END(self):
            return self.getToken(p_GreekBase.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(p_GreekBase.OP_SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.StatementContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.StatementContext,i)


        def getRuleIndex(self):
            return p_GreekBase.RULE_procedureDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureDeclaration" ):
                listener.enterProcedureDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureDeclaration" ):
                listener.exitProcedureDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureDeclaration" ):
                return visitor.visitProcedureDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def procedureDeclaration(self):

        localctx = p_GreekBase.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(p_GreekBase.KW_PROCEDURE)
            self.state = 102
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 103
            self.match(p_GreekBase.KW_IS)
            self.state = 104
            self.match(p_GreekBase.KW_BEGIN)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                self.state = 105
                self.statement()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(p_GreekBase.KW_END)
            self.state = 112
            self.match(p_GreekBase.KW_PROCEDURE)
            self.state = 113
            self.match(p_GreekBase.OP_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNCTION(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.KW_FUNCTION)
            else:
                return self.getToken(p_GreekBase.KW_FUNCTION, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.IDENTIFIER)
            else:
                return self.getToken(p_GreekBase.IDENTIFIER, i)

        def OP_LPAREN(self):
            return self.getToken(p_GreekBase.OP_LPAREN, 0)

        def OP_RPAREN(self):
            return self.getToken(p_GreekBase.OP_RPAREN, 0)

        def OP_COLON(self):
            return self.getToken(p_GreekBase.OP_COLON, 0)

        def KW_IS(self):
            return self.getToken(p_GreekBase.KW_IS, 0)

        def KW_BEGIN(self):
            return self.getToken(p_GreekBase.KW_BEGIN, 0)

        def KW_END(self):
            return self.getToken(p_GreekBase.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(p_GreekBase.OP_SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.StatementContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.StatementContext,i)


        def OP_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(p_GreekBase.OP_COMMA)
            else:
                return self.getToken(p_GreekBase.OP_COMMA, i)

        def getRuleIndex(self):
            return p_GreekBase.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = p_GreekBase.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(p_GreekBase.KW_FUNCTION)
            self.state = 116
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 117
            self.match(p_GreekBase.OP_LPAREN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 118
                self.match(p_GreekBase.IDENTIFIER)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 119
                    self.match(p_GreekBase.OP_COMMA)
                    self.state = 120
                    self.match(p_GreekBase.IDENTIFIER)
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 128
            self.match(p_GreekBase.OP_RPAREN)
            self.state = 129
            self.match(p_GreekBase.OP_COLON)
            self.state = 130
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 131
            self.match(p_GreekBase.KW_IS)
            self.state = 132
            self.match(p_GreekBase.KW_BEGIN)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                self.state = 133
                self.statement()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(p_GreekBase.KW_END)
            self.state = 140
            self.match(p_GreekBase.KW_FUNCTION)
            self.state = 141
            self.match(p_GreekBase.OP_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(p_GreekBase.ExpressionContext)
            else:
                return self.getTypedRuleContext(p_GreekBase.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(p_GreekBase.RelopContext,0)


        def getRuleIndex(self):
            return p_GreekBase.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = p_GreekBase.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.expression()
            self.state = 144
            self.relop()
            self.state = 145
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(p_GreekBase.IDENTIFIER, 0)

        def LIT_INT(self):
            return self.getToken(p_GreekBase.LIT_INT, 0)

        def LIT_FLOAT(self):
            return self.getToken(p_GreekBase.LIT_FLOAT, 0)

        def LIT_STRING(self):
            return self.getToken(p_GreekBase.LIT_STRING, 0)

        def getRuleIndex(self):
            return p_GreekBase.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = p_GreekBase.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 828662331436171264) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EQUAL(self):
            return self.getToken(p_GreekBase.OP_EQUAL, 0)

        def OP_NOT_EQUAL(self):
            return self.getToken(p_GreekBase.OP_NOT_EQUAL, 0)

        def OP_LESS(self):
            return self.getToken(p_GreekBase.OP_LESS, 0)

        def OP_LESS_EQ(self):
            return self.getToken(p_GreekBase.OP_LESS_EQ, 0)

        def OP_GREATER(self):
            return self.getToken(p_GreekBase.OP_GREATER, 0)

        def OP_GREATER_EQ(self):
            return self.getToken(p_GreekBase.OP_GREATER_EQ, 0)

        def getRuleIndex(self):
            return p_GreekBase.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = p_GreekBase.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






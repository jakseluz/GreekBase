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
        4,1,62,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,
        1,2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,
        2,5,2,56,8,2,10,2,12,2,59,9,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,
        2,3,2,68,8,2,1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,5,3,77,8,3,10,3,12,3,
        80,9,3,1,3,1,3,1,3,1,3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,3,3,3,93,
        8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,105,8,5,10,5,12,
        5,108,9,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,
        0,9,0,2,4,6,8,10,12,14,16,0,2,2,0,55,57,59,59,1,0,32,37,127,0,21,
        1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,72,1,0,0,0,8,94,1,0,0,0,10,99,
        1,0,0,0,12,113,1,0,0,0,14,117,1,0,0,0,16,119,1,0,0,0,18,20,3,2,1,
        0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,
        1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,31,3,4,2,0,27,
        31,3,6,3,0,28,31,3,8,4,0,29,31,3,10,5,0,30,26,1,0,0,0,30,27,1,0,
        0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,3,0,0,33,70,
        3,12,6,0,34,38,5,4,0,0,35,37,3,2,1,0,36,35,1,0,0,0,37,40,1,0,0,0,
        38,36,1,0,0,0,38,39,1,0,0,0,39,48,1,0,0,0,40,38,1,0,0,0,41,45,5,
        5,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,
        46,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,48,41,1,0,0,0,48,49,1,0,0,
        0,49,50,1,0,0,0,50,51,5,2,0,0,51,52,5,3,0,0,52,71,5,48,0,0,53,57,
        5,29,0,0,54,56,3,2,1,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,67,1,0,0,0,59,57,1,0,0,0,60,64,5,5,0,0,61,63,3,
        2,1,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,
        68,1,0,0,0,66,64,1,0,0,0,67,60,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,
        0,69,71,5,30,0,0,70,34,1,0,0,0,70,53,1,0,0,0,71,5,1,0,0,0,72,73,
        5,7,0,0,73,92,3,12,6,0,74,78,5,6,0,0,75,77,3,2,1,0,76,75,1,0,0,0,
        77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,
        0,0,0,81,82,5,2,0,0,82,83,5,6,0,0,83,93,5,48,0,0,84,88,5,29,0,0,
        85,87,3,2,1,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,
        0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,93,5,30,0,0,92,74,1,0,0,0,92,
        84,1,0,0,0,93,7,1,0,0,0,94,95,5,59,0,0,95,96,5,31,0,0,96,97,3,14,
        7,0,97,98,5,48,0,0,98,9,1,0,0,0,99,100,5,11,0,0,100,101,5,59,0,0,
        101,102,5,13,0,0,102,106,5,1,0,0,103,105,3,2,1,0,104,103,1,0,0,0,
        105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,
        108,106,1,0,0,0,109,110,5,2,0,0,110,111,5,11,0,0,111,112,5,48,0,
        0,112,11,1,0,0,0,113,114,3,14,7,0,114,115,3,16,8,0,115,116,3,14,
        7,0,116,13,1,0,0,0,117,118,7,0,0,0,118,15,1,0,0,0,119,120,7,1,0,
        0,120,17,1,0,0,0,13,21,30,38,45,48,57,64,67,70,78,88,92,106
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
    RULE_condition = 6
    RULE_expression = 7
    RULE_relop = 8

    ruleNames =  [ "program", "statement", "ifStatement", "loopStatement", 
                   "assignment", "procedureDeclaration", "condition", "expression", 
                   "relop" ]

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




    def program(self):

        localctx = p_GreekBase.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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




    def statement(self):

        localctx = p_GreekBase.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.loopStatement()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.assignment()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
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




    def ifStatement(self):

        localctx = p_GreekBase.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(p_GreekBase.KW_IF)
            self.state = 33
            self.condition()
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 34
                self.match(p_GreekBase.KW_THEN)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 35
                    self.statement()
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 41
                    self.match(p_GreekBase.KW_ELSE)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                        self.state = 42
                        self.statement()
                        self.state = 47
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 50
                self.match(p_GreekBase.KW_END)
                self.state = 51
                self.match(p_GreekBase.KW_IF)
                self.state = 52
                self.match(p_GreekBase.OP_SEMICOLON)
                pass
            elif token in [29]:
                self.state = 53
                self.match(p_GreekBase.KW_LCURL)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 54
                    self.statement()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 60
                    self.match(p_GreekBase.KW_ELSE)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                        self.state = 61
                        self.statement()
                        self.state = 66
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 69
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




    def loopStatement(self):

        localctx = p_GreekBase.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(p_GreekBase.KW_WHILE)
            self.state = 73
            self.condition()
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 74
                self.match(p_GreekBase.KW_LOOP)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 75
                    self.statement()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(p_GreekBase.KW_END)
                self.state = 82
                self.match(p_GreekBase.KW_LOOP)
                self.state = 83
                self.match(p_GreekBase.OP_SEMICOLON)
                pass
            elif token in [29]:
                self.state = 84
                self.match(p_GreekBase.KW_LCURL)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                    self.state = 85
                    self.statement()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 91
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




    def assignment(self):

        localctx = p_GreekBase.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 95
            self.match(p_GreekBase.OP_ASSIGN)
            self.state = 96
            self.expression()
            self.state = 97
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




    def procedureDeclaration(self):

        localctx = p_GreekBase.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(p_GreekBase.KW_PROCEDURE)
            self.state = 100
            self.match(p_GreekBase.IDENTIFIER)
            self.state = 101
            self.match(p_GreekBase.KW_IS)
            self.state = 102
            self.match(p_GreekBase.KW_BEGIN)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576460752303425672) != 0):
                self.state = 103
                self.statement()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(p_GreekBase.KW_END)
            self.state = 110
            self.match(p_GreekBase.KW_PROCEDURE)
            self.state = 111
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




    def condition(self):

        localctx = p_GreekBase.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.expression()
            self.state = 114
            self.relop()
            self.state = 115
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




    def expression(self):

        localctx = p_GreekBase.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
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




    def relop(self):

        localctx = p_GreekBase.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
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






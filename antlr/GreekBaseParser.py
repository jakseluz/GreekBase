# Generated from GreekBaseParser.g4 by ANTLR 4.13.2
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
        4,1,56,234,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,3,3,53,8,3,1,4,1,
        4,1,4,1,4,5,4,59,8,4,10,4,12,4,62,9,4,1,4,1,4,5,4,66,8,4,10,4,12,
        4,69,9,4,3,4,71,8,4,1,4,1,4,1,4,1,4,1,4,5,4,78,8,4,10,4,12,4,81,
        9,4,1,4,1,4,5,4,85,8,4,10,4,12,4,88,9,4,3,4,90,8,4,1,4,3,4,93,8,
        4,1,5,1,5,1,5,1,5,5,5,99,8,5,10,5,12,5,102,9,5,1,5,1,5,1,5,1,5,1,
        5,5,5,109,8,5,10,5,12,5,112,9,5,1,5,3,5,115,8,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,130,8,8,10,8,12,8,133,9,
        8,1,8,1,8,1,9,1,9,1,9,5,9,140,8,9,10,9,12,9,143,9,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,3,10,153,8,10,1,11,1,11,1,11,3,11,158,8,
        11,1,11,1,11,1,11,5,11,163,8,11,10,11,12,11,166,9,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,178,8,12,10,12,12,12,
        181,9,12,3,12,183,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,191,8,
        12,10,12,12,12,194,9,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,213,8,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,227,
        8,14,10,14,12,14,230,9,14,1,15,1,15,1,15,0,1,28,16,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,0,2,1,0,48,51,1,0,25,30,251,0,35,1,
        0,0,0,2,40,1,0,0,0,4,47,1,0,0,0,6,52,1,0,0,0,8,54,1,0,0,0,10,94,
        1,0,0,0,12,116,1,0,0,0,14,120,1,0,0,0,16,125,1,0,0,0,18,136,1,0,
        0,0,20,152,1,0,0,0,22,154,1,0,0,0,24,171,1,0,0,0,26,199,1,0,0,0,
        28,212,1,0,0,0,30,231,1,0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,
        38,39,5,0,0,1,39,1,1,0,0,0,40,41,7,0,0,0,41,3,1,0,0,0,42,48,3,8,
        4,0,43,48,3,10,5,0,44,48,3,14,7,0,45,48,3,22,11,0,46,48,3,12,6,0,
        47,42,1,0,0,0,47,43,1,0,0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,
        0,0,0,48,5,1,0,0,0,49,53,3,8,4,0,50,53,3,10,5,0,51,53,3,14,7,0,52,
        49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,7,1,0,0,0,54,55,5,3,0,
        0,55,92,3,26,13,0,56,60,5,4,0,0,57,59,3,6,3,0,58,57,1,0,0,0,59,62,
        1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,70,1,0,0,0,62,60,1,0,0,0,
        63,67,5,5,0,0,64,66,3,6,3,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,
        0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,70,63,1,0,0,0,70,
        71,1,0,0,0,71,72,1,0,0,0,72,73,5,2,0,0,73,74,5,3,0,0,74,93,5,41,
        0,0,75,79,5,22,0,0,76,78,3,6,3,0,77,76,1,0,0,0,78,81,1,0,0,0,79,
        77,1,0,0,0,79,80,1,0,0,0,80,89,1,0,0,0,81,79,1,0,0,0,82,86,5,5,0,
        0,83,85,3,6,3,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,
        1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,89,82,1,0,0,0,89,90,1,0,0,0,
        90,91,1,0,0,0,91,93,5,23,0,0,92,56,1,0,0,0,92,75,1,0,0,0,93,9,1,
        0,0,0,94,95,5,7,0,0,95,114,3,26,13,0,96,100,5,6,0,0,97,99,3,6,3,
        0,98,97,1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,
        103,1,0,0,0,102,100,1,0,0,0,103,104,5,2,0,0,104,105,5,6,0,0,105,
        115,5,41,0,0,106,110,5,22,0,0,107,109,3,6,3,0,108,107,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,
        110,1,0,0,0,113,115,5,23,0,0,114,96,1,0,0,0,114,106,1,0,0,0,115,
        11,1,0,0,0,116,117,5,56,0,0,117,118,3,28,14,0,118,119,5,41,0,0,119,
        13,1,0,0,0,120,121,5,52,0,0,121,122,5,24,0,0,122,123,3,28,14,0,123,
        124,5,41,0,0,124,15,1,0,0,0,125,126,5,44,0,0,126,131,3,18,9,0,127,
        128,5,41,0,0,128,130,3,18,9,0,129,127,1,0,0,0,130,133,1,0,0,0,131,
        129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,
        135,5,45,0,0,135,17,1,0,0,0,136,141,5,52,0,0,137,138,5,42,0,0,138,
        140,5,52,0,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,40,0,0,145,
        146,3,20,10,0,146,147,3,2,1,0,147,19,1,0,0,0,148,153,5,9,0,0,149,
        153,5,10,0,0,150,151,5,9,0,0,151,153,5,10,0,0,152,148,1,0,0,0,152,
        149,1,0,0,0,152,150,1,0,0,0,153,21,1,0,0,0,154,155,5,12,0,0,155,
        157,5,52,0,0,156,158,3,16,8,0,157,156,1,0,0,0,157,158,1,0,0,0,158,
        159,1,0,0,0,159,160,5,14,0,0,160,164,5,1,0,0,161,163,3,6,3,0,162,
        161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,
        167,1,0,0,0,166,164,1,0,0,0,167,168,5,2,0,0,168,169,5,12,0,0,169,
        170,5,41,0,0,170,23,1,0,0,0,171,172,5,13,0,0,172,173,5,52,0,0,173,
        182,5,44,0,0,174,179,5,52,0,0,175,176,5,42,0,0,176,178,5,52,0,0,
        177,175,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,
        180,183,1,0,0,0,181,179,1,0,0,0,182,174,1,0,0,0,182,183,1,0,0,0,
        183,184,1,0,0,0,184,185,5,45,0,0,185,186,5,40,0,0,186,187,5,52,0,
        0,187,188,5,14,0,0,188,192,5,1,0,0,189,191,3,4,2,0,190,189,1,0,0,
        0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,
        0,194,192,1,0,0,0,195,196,5,2,0,0,196,197,5,13,0,0,197,198,5,41,
        0,0,198,25,1,0,0,0,199,200,3,28,14,0,200,201,3,30,15,0,201,202,3,
        28,14,0,202,27,1,0,0,0,203,204,6,14,-1,0,204,205,5,44,0,0,205,206,
        3,28,14,0,206,207,5,45,0,0,207,213,1,0,0,0,208,213,5,52,0,0,209,
        213,5,48,0,0,210,213,5,49,0,0,211,213,5,50,0,0,212,203,1,0,0,0,212,
        208,1,0,0,0,212,209,1,0,0,0,212,210,1,0,0,0,212,211,1,0,0,0,213,
        228,1,0,0,0,214,215,10,9,0,0,215,216,5,31,0,0,216,227,3,28,14,10,
        217,218,10,8,0,0,218,219,5,32,0,0,219,227,3,28,14,9,220,221,10,7,
        0,0,221,222,5,33,0,0,222,227,3,28,14,8,223,224,10,6,0,0,224,225,
        5,34,0,0,225,227,3,28,14,7,226,214,1,0,0,0,226,217,1,0,0,0,226,220,
        1,0,0,0,226,223,1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,228,229,
        1,0,0,0,229,29,1,0,0,0,230,228,1,0,0,0,231,232,7,1,0,0,232,31,1,
        0,0,0,24,35,47,52,60,67,70,79,86,89,92,100,110,114,131,141,152,157,
        164,179,182,192,212,226,228
    ]

class GreekBaseParser ( Parser ):

    grammarFileName = "GreekBaseParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'begin'", "'end'", "'if'", "'then'", 
                     "'else'", "'loop'", "'while'", "'for'", "'in'", "'out'", 
                     "'return'", "'procedure'", "'function'", "'is'", "'type'", 
                     "'array'", "'of'", "'const'", "'use'", "'with'", "'new'", 
                     "'{'", "'}'", "':='", "'='", "'/='", "'<'", "'<='", 
                     "'>'", "'>='", "'+'", "'-'", "'*'", "'/'", "'mod'", 
                     "'and'", "'or'", "'not'", "'.'", "':'", "';'", "','", 
                     "'=>'", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "KW_BEGIN", "KW_END", "KW_IF", "KW_THEN", 
                      "KW_ELSE", "KW_LOOP", "KW_WHILE", "KW_FOR", "KW_IN", 
                      "KW_OUT", "KW_RETURN", "KW_PROCEDURE", "KW_FUNCTION", 
                      "KW_IS", "KW_TYPE", "KW_ARRAY", "KW_OF", "KW_CONST", 
                      "KW_USE", "KW_WITH", "KW_NEW", "KW_LCURL", "KW_RCURL", 
                      "OP_ASSIGN", "OP_EQUAL", "OP_NOT_EQUAL", "OP_LESS", 
                      "OP_LESS_EQ", "OP_GREATER", "OP_GREATER_EQ", "OP_ADD", 
                      "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "OP_AND", 
                      "OP_OR", "OP_NOT", "OP_DOT", "OP_COLON", "OP_SEMICOLON", 
                      "OP_COMMA", "OP_ARROW", "OP_LPAREN", "OP_RPAREN", 
                      "OP_LBRACKET", "OP_RBRACKET", "LIT_INT", "LIT_FLOAT", 
                      "LIT_STRING", "LIT_CHAR", "IDENTIFIER", "LINE_COMMENT", 
                      "MULTILINE_COMMENT", "WS", "KW_PRINT" ]

    RULE_program = 0
    RULE_literal = 1
    RULE_statement = 2
    RULE_nonDeclarativeStatement = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_printStatement = 6
    RULE_assignment = 7
    RULE_formalParameterPart = 8
    RULE_parameterSpecification = 9
    RULE_modeSpecifier = 10
    RULE_procedureDeclaration = 11
    RULE_functionDeclaration = 12
    RULE_condition = 13
    RULE_expression = 14
    RULE_relop = 15

    ruleNames =  [ "program", "literal", "statement", "nonDeclarativeStatement", 
                   "ifStatement", "loopStatement", "printStatement", "assignment", 
                   "formalParameterPart", "parameterSpecification", "modeSpecifier", 
                   "procedureDeclaration", "functionDeclaration", "condition", 
                   "expression", "relop" ]

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
    KW_OUT=10
    KW_RETURN=11
    KW_PROCEDURE=12
    KW_FUNCTION=13
    KW_IS=14
    KW_TYPE=15
    KW_ARRAY=16
    KW_OF=17
    KW_CONST=18
    KW_USE=19
    KW_WITH=20
    KW_NEW=21
    KW_LCURL=22
    KW_RCURL=23
    OP_ASSIGN=24
    OP_EQUAL=25
    OP_NOT_EQUAL=26
    OP_LESS=27
    OP_LESS_EQ=28
    OP_GREATER=29
    OP_GREATER_EQ=30
    OP_ADD=31
    OP_SUB=32
    OP_MUL=33
    OP_DIV=34
    OP_MOD=35
    OP_AND=36
    OP_OR=37
    OP_NOT=38
    OP_DOT=39
    OP_COLON=40
    OP_SEMICOLON=41
    OP_COMMA=42
    OP_ARROW=43
    OP_LPAREN=44
    OP_RPAREN=45
    OP_LBRACKET=46
    OP_RBRACKET=47
    LIT_INT=48
    LIT_FLOAT=49
    LIT_STRING=50
    LIT_CHAR=51
    IDENTIFIER=52
    LINE_COMMENT=53
    MULTILINE_COMMENT=54
    WS=55
    KW_PRINT=56

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
            return self.getToken(GreekBaseParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.StatementContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.StatementContext,i)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_program

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

        localctx = GreekBaseParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 76561193665302664) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(GreekBaseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT_INT(self):
            return self.getToken(GreekBaseParser.LIT_INT, 0)

        def LIT_FLOAT(self):
            return self.getToken(GreekBaseParser.LIT_FLOAT, 0)

        def LIT_CHAR(self):
            return self.getToken(GreekBaseParser.LIT_CHAR, 0)

        def LIT_STRING(self):
            return self.getToken(GreekBaseParser.LIT_STRING, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = GreekBaseParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4222124650659840) != 0)):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(GreekBaseParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(GreekBaseParser.LoopStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GreekBaseParser.AssignmentContext,0)


        def procedureDeclaration(self):
            return self.getTypedRuleContext(GreekBaseParser.ProcedureDeclarationContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(GreekBaseParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_statement

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

        localctx = GreekBaseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.loopStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.assignment()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.procedureDeclaration()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.printStatement()
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


    class NonDeclarativeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(GreekBaseParser.IfStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(GreekBaseParser.LoopStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GreekBaseParser.AssignmentContext,0)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_nonDeclarativeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonDeclarativeStatement" ):
                listener.enterNonDeclarativeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonDeclarativeStatement" ):
                listener.exitNonDeclarativeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonDeclarativeStatement" ):
                return visitor.visitNonDeclarativeStatement(self)
            else:
                return visitor.visitChildren(self)




    def nonDeclarativeStatement(self):

        localctx = GreekBaseParser.NonDeclarativeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nonDeclarativeStatement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.loopStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.assignment()
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
                return self.getTokens(GreekBaseParser.KW_IF)
            else:
                return self.getToken(GreekBaseParser.KW_IF, i)

        def condition(self):
            return self.getTypedRuleContext(GreekBaseParser.ConditionContext,0)


        def KW_THEN(self):
            return self.getToken(GreekBaseParser.KW_THEN, 0)

        def KW_END(self):
            return self.getToken(GreekBaseParser.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def KW_LCURL(self):
            return self.getToken(GreekBaseParser.KW_LCURL, 0)

        def KW_RCURL(self):
            return self.getToken(GreekBaseParser.KW_RCURL, 0)

        def nonDeclarativeStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.NonDeclarativeStatementContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.NonDeclarativeStatementContext,i)


        def KW_ELSE(self):
            return self.getToken(GreekBaseParser.KW_ELSE, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_ifStatement

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

        localctx = GreekBaseParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(GreekBaseParser.KW_IF)
            self.state = 55
            self.condition()
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 56
                self.match(GreekBaseParser.KW_THEN)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 57
                    self.nonDeclarativeStatement()
                    self.state = 62
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 63
                    self.match(GreekBaseParser.KW_ELSE)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                        self.state = 64
                        self.nonDeclarativeStatement()
                        self.state = 69
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 72
                self.match(GreekBaseParser.KW_END)
                self.state = 73
                self.match(GreekBaseParser.KW_IF)
                self.state = 74
                self.match(GreekBaseParser.OP_SEMICOLON)
                pass
            elif token in [22]:
                self.state = 75
                self.match(GreekBaseParser.KW_LCURL)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 76
                    self.nonDeclarativeStatement()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 82
                    self.match(GreekBaseParser.KW_ELSE)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                        self.state = 83
                        self.nonDeclarativeStatement()
                        self.state = 88
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 91
                self.match(GreekBaseParser.KW_RCURL)
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
            return self.getToken(GreekBaseParser.KW_WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(GreekBaseParser.ConditionContext,0)


        def KW_LOOP(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.KW_LOOP)
            else:
                return self.getToken(GreekBaseParser.KW_LOOP, i)

        def KW_LCURL(self):
            return self.getToken(GreekBaseParser.KW_LCURL, 0)

        def KW_RCURL(self):
            return self.getToken(GreekBaseParser.KW_RCURL, 0)

        def KW_END(self):
            return self.getToken(GreekBaseParser.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def nonDeclarativeStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.NonDeclarativeStatementContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.NonDeclarativeStatementContext,i)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_loopStatement

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

        localctx = GreekBaseParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loopStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GreekBaseParser.KW_WHILE)
            self.state = 95
            self.condition()
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 96
                self.match(GreekBaseParser.KW_LOOP)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 97
                    self.nonDeclarativeStatement()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(GreekBaseParser.KW_END)
                self.state = 104
                self.match(GreekBaseParser.KW_LOOP)
                self.state = 105
                self.match(GreekBaseParser.OP_SEMICOLON)
                pass
            elif token in [22]:
                self.state = 106
                self.match(GreekBaseParser.KW_LCURL)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 107
                    self.nonDeclarativeStatement()
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(GreekBaseParser.KW_RCURL)
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


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PRINT(self):
            return self.getToken(GreekBaseParser.KW_PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,0)


        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = GreekBaseParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GreekBaseParser.KW_PRINT)
            self.state = 117
            self.expression(0)
            self.state = 118
            self.match(GreekBaseParser.OP_SEMICOLON)
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
            return self.getToken(GreekBaseParser.IDENTIFIER, 0)

        def OP_ASSIGN(self):
            return self.getToken(GreekBaseParser.OP_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,0)


        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_assignment

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

        localctx = GreekBaseParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 121
            self.match(GreekBaseParser.OP_ASSIGN)
            self.state = 122
            self.expression(0)
            self.state = 123
            self.match(GreekBaseParser.OP_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LPAREN(self):
            return self.getToken(GreekBaseParser.OP_LPAREN, 0)

        def parameterSpecification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.ParameterSpecificationContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ParameterSpecificationContext,i)


        def OP_RPAREN(self):
            return self.getToken(GreekBaseParser.OP_RPAREN, 0)

        def OP_SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.OP_SEMICOLON)
            else:
                return self.getToken(GreekBaseParser.OP_SEMICOLON, i)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_formalParameterPart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterPart" ):
                listener.enterFormalParameterPart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterPart" ):
                listener.exitFormalParameterPart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterPart" ):
                return visitor.visitFormalParameterPart(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterPart(self):

        localctx = GreekBaseParser.FormalParameterPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_formalParameterPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(GreekBaseParser.OP_LPAREN)
            self.state = 126
            self.parameterSpecification()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 127
                self.match(GreekBaseParser.OP_SEMICOLON)
                self.state = 128
                self.parameterSpecification()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(GreekBaseParser.OP_RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.IDENTIFIER)
            else:
                return self.getToken(GreekBaseParser.IDENTIFIER, i)

        def OP_COLON(self):
            return self.getToken(GreekBaseParser.OP_COLON, 0)

        def modeSpecifier(self):
            return self.getTypedRuleContext(GreekBaseParser.ModeSpecifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(GreekBaseParser.LiteralContext,0)


        def OP_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.OP_COMMA)
            else:
                return self.getToken(GreekBaseParser.OP_COMMA, i)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_parameterSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterSpecification" ):
                listener.enterParameterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterSpecification" ):
                listener.exitParameterSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterSpecification" ):
                return visitor.visitParameterSpecification(self)
            else:
                return visitor.visitChildren(self)




    def parameterSpecification(self):

        localctx = GreekBaseParser.ParameterSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameterSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 137
                self.match(GreekBaseParser.OP_COMMA)
                self.state = 138
                self.match(GreekBaseParser.IDENTIFIER)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(GreekBaseParser.OP_COLON)
            self.state = 145
            self.modeSpecifier()
            self.state = 146
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IN(self):
            return self.getToken(GreekBaseParser.KW_IN, 0)

        def KW_OUT(self):
            return self.getToken(GreekBaseParser.KW_OUT, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_modeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModeSpecifier" ):
                listener.enterModeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModeSpecifier" ):
                listener.exitModeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModeSpecifier" ):
                return visitor.visitModeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def modeSpecifier(self):

        localctx = GreekBaseParser.ModeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_modeSpecifier)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(GreekBaseParser.KW_IN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(GreekBaseParser.KW_OUT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(GreekBaseParser.KW_IN)
                self.state = 151
                self.match(GreekBaseParser.KW_OUT)
                pass


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
                return self.getTokens(GreekBaseParser.KW_PROCEDURE)
            else:
                return self.getToken(GreekBaseParser.KW_PROCEDURE, i)

        def IDENTIFIER(self):
            return self.getToken(GreekBaseParser.IDENTIFIER, 0)

        def KW_IS(self):
            return self.getToken(GreekBaseParser.KW_IS, 0)

        def KW_BEGIN(self):
            return self.getToken(GreekBaseParser.KW_BEGIN, 0)

        def KW_END(self):
            return self.getToken(GreekBaseParser.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def formalParameterPart(self):
            return self.getTypedRuleContext(GreekBaseParser.FormalParameterPartContext,0)


        def nonDeclarativeStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.NonDeclarativeStatementContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.NonDeclarativeStatementContext,i)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_procedureDeclaration

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

        localctx = GreekBaseParser.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(GreekBaseParser.KW_PROCEDURE)
            self.state = 155
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 156
                self.formalParameterPart()


            self.state = 159
            self.match(GreekBaseParser.KW_IS)
            self.state = 160
            self.match(GreekBaseParser.KW_BEGIN)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                self.state = 161
                self.nonDeclarativeStatement()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(GreekBaseParser.KW_END)
            self.state = 168
            self.match(GreekBaseParser.KW_PROCEDURE)
            self.state = 169
            self.match(GreekBaseParser.OP_SEMICOLON)
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
                return self.getTokens(GreekBaseParser.KW_FUNCTION)
            else:
                return self.getToken(GreekBaseParser.KW_FUNCTION, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.IDENTIFIER)
            else:
                return self.getToken(GreekBaseParser.IDENTIFIER, i)

        def OP_LPAREN(self):
            return self.getToken(GreekBaseParser.OP_LPAREN, 0)

        def OP_RPAREN(self):
            return self.getToken(GreekBaseParser.OP_RPAREN, 0)

        def OP_COLON(self):
            return self.getToken(GreekBaseParser.OP_COLON, 0)

        def KW_IS(self):
            return self.getToken(GreekBaseParser.KW_IS, 0)

        def KW_BEGIN(self):
            return self.getToken(GreekBaseParser.KW_BEGIN, 0)

        def KW_END(self):
            return self.getToken(GreekBaseParser.KW_END, 0)

        def OP_SEMICOLON(self):
            return self.getToken(GreekBaseParser.OP_SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.StatementContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.StatementContext,i)


        def OP_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GreekBaseParser.OP_COMMA)
            else:
                return self.getToken(GreekBaseParser.OP_COMMA, i)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_functionDeclaration

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

        localctx = GreekBaseParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(GreekBaseParser.KW_FUNCTION)
            self.state = 172
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 173
            self.match(GreekBaseParser.OP_LPAREN)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 174
                self.match(GreekBaseParser.IDENTIFIER)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 175
                    self.match(GreekBaseParser.OP_COMMA)
                    self.state = 176
                    self.match(GreekBaseParser.IDENTIFIER)
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 184
            self.match(GreekBaseParser.OP_RPAREN)
            self.state = 185
            self.match(GreekBaseParser.OP_COLON)
            self.state = 186
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 187
            self.match(GreekBaseParser.KW_IS)
            self.state = 188
            self.match(GreekBaseParser.KW_BEGIN)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 76561193665302664) != 0):
                self.state = 189
                self.statement()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(GreekBaseParser.KW_END)
            self.state = 196
            self.match(GreekBaseParser.KW_FUNCTION)
            self.state = 197
            self.match(GreekBaseParser.OP_SEMICOLON)
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
                return self.getTypedRuleContexts(GreekBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(GreekBaseParser.RelopContext,0)


        def getRuleIndex(self):
            return GreekBaseParser.RULE_condition

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

        localctx = GreekBaseParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expression(0)
            self.state = 200
            self.relop()
            self.state = 201
            self.expression(0)
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


        def getRuleIndex(self):
            return GreekBaseParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_STRING(self):
            return self.getToken(GreekBaseParser.LIT_STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_FLOAT(self):
            return self.getToken(GreekBaseParser.LIT_FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIT_INT(self):
            return self.getToken(GreekBaseParser.LIT_INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,i)

        def OP_ADD(self):
            return self.getToken(GreekBaseParser.OP_ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,i)

        def OP_MUL(self):
            return self.getToken(GreekBaseParser.OP_MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,i)

        def OP_DIV(self):
            return self.getToken(GreekBaseParser.OP_DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_LPAREN(self):
            return self.getToken(GreekBaseParser.OP_LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,0)

        def OP_RPAREN(self):
            return self.getToken(GreekBaseParser.OP_RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GreekBaseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GreekBaseParser.ExpressionContext,i)

        def OP_SUB(self):
            return self.getToken(GreekBaseParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GreekBaseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(GreekBaseParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GreekBaseParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                localctx = GreekBaseParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 204
                self.match(GreekBaseParser.OP_LPAREN)
                self.state = 205
                self.expression(0)
                self.state = 206
                self.match(GreekBaseParser.OP_RPAREN)
                pass
            elif token in [52]:
                localctx = GreekBaseParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 208
                self.match(GreekBaseParser.IDENTIFIER)
                pass
            elif token in [48]:
                localctx = GreekBaseParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 209
                self.match(GreekBaseParser.LIT_INT)
                pass
            elif token in [49]:
                localctx = GreekBaseParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 210
                self.match(GreekBaseParser.LIT_FLOAT)
                pass
            elif token in [50]:
                localctx = GreekBaseParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 211
                self.match(GreekBaseParser.LIT_STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 226
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = GreekBaseParser.AddExprContext(self, GreekBaseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 214
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 215
                        self.match(GreekBaseParser.OP_ADD)
                        self.state = 216
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = GreekBaseParser.SubExprContext(self, GreekBaseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 218
                        self.match(GreekBaseParser.OP_SUB)
                        self.state = 219
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = GreekBaseParser.MulExprContext(self, GreekBaseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 220
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 221
                        self.match(GreekBaseParser.OP_MUL)
                        self.state = 222
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = GreekBaseParser.DivExprContext(self, GreekBaseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 223
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 224
                        self.match(GreekBaseParser.OP_DIV)
                        self.state = 225
                        self.expression(7)
                        pass

             
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EQUAL(self):
            return self.getToken(GreekBaseParser.OP_EQUAL, 0)

        def OP_NOT_EQUAL(self):
            return self.getToken(GreekBaseParser.OP_NOT_EQUAL, 0)

        def OP_LESS(self):
            return self.getToken(GreekBaseParser.OP_LESS, 0)

        def OP_LESS_EQ(self):
            return self.getToken(GreekBaseParser.OP_LESS_EQ, 0)

        def OP_GREATER(self):
            return self.getToken(GreekBaseParser.OP_GREATER, 0)

        def OP_GREATER_EQ(self):
            return self.getToken(GreekBaseParser.OP_GREATER_EQ, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_relop

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

        localctx = GreekBaseParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         





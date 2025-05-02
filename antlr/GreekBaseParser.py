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
        4,1,55,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,4,1,4,1,4,1,4,5,4,
        56,8,4,10,4,12,4,59,9,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,3,4,
        68,8,4,1,4,1,4,1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,4,1,4,5,
        4,82,8,4,10,4,12,4,85,9,4,3,4,87,8,4,1,4,3,4,90,8,4,1,5,1,5,1,5,
        1,5,5,5,96,8,5,10,5,12,5,99,9,5,1,5,1,5,1,5,1,5,1,5,5,5,106,8,5,
        10,5,12,5,109,9,5,1,5,3,5,112,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,5,7,123,8,7,10,7,12,7,126,9,7,1,7,1,7,1,8,1,8,1,8,5,8,133,
        8,8,10,8,12,8,136,9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,146,8,
        9,1,10,1,10,1,10,3,10,151,8,10,1,10,1,10,1,10,5,10,156,8,10,10,10,
        12,10,159,9,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,171,8,11,10,11,12,11,174,9,11,3,11,176,8,11,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,184,8,11,10,11,12,11,187,9,11,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,0,0,15,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,0,3,1,0,48,51,2,0,48,50,52,52,1,
        0,25,30,210,0,33,1,0,0,0,2,42,1,0,0,0,4,47,1,0,0,0,6,49,1,0,0,0,
        8,51,1,0,0,0,10,91,1,0,0,0,12,113,1,0,0,0,14,118,1,0,0,0,16,129,
        1,0,0,0,18,145,1,0,0,0,20,147,1,0,0,0,22,164,1,0,0,0,24,192,1,0,
        0,0,26,196,1,0,0,0,28,198,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,
        35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,0,0,
        0,36,37,5,0,0,1,37,1,1,0,0,0,38,43,3,8,4,0,39,43,3,10,5,0,40,43,
        3,12,6,0,41,43,3,20,10,0,42,38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,
        0,42,41,1,0,0,0,43,3,1,0,0,0,44,48,3,8,4,0,45,48,3,10,5,0,46,48,
        3,12,6,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,5,1,0,0,0,
        49,50,7,0,0,0,50,7,1,0,0,0,51,52,5,3,0,0,52,89,3,24,12,0,53,57,5,
        4,0,0,54,56,3,4,2,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,67,1,0,0,0,59,57,1,0,0,0,60,64,5,5,0,0,61,63,3,4,2,
        0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,68,
        1,0,0,0,66,64,1,0,0,0,67,60,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,
        69,70,5,2,0,0,70,71,5,3,0,0,71,90,5,41,0,0,72,76,5,22,0,0,73,75,
        3,4,2,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,
        77,86,1,0,0,0,78,76,1,0,0,0,79,83,5,5,0,0,80,82,3,4,2,0,81,80,1,
        0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,87,1,0,0,0,85,
        83,1,0,0,0,86,79,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,90,5,23,
        0,0,89,53,1,0,0,0,89,72,1,0,0,0,90,9,1,0,0,0,91,92,5,7,0,0,92,111,
        3,24,12,0,93,97,5,6,0,0,94,96,3,4,2,0,95,94,1,0,0,0,96,99,1,0,0,
        0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,
        5,2,0,0,101,102,5,6,0,0,102,112,5,41,0,0,103,107,5,22,0,0,104,106,
        3,4,2,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,
        1,0,0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,112,5,23,0,0,111,93,
        1,0,0,0,111,103,1,0,0,0,112,11,1,0,0,0,113,114,5,52,0,0,114,115,
        5,24,0,0,115,116,3,26,13,0,116,117,5,41,0,0,117,13,1,0,0,0,118,119,
        5,44,0,0,119,124,3,16,8,0,120,121,5,41,0,0,121,123,3,16,8,0,122,
        120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,
        127,1,0,0,0,126,124,1,0,0,0,127,128,5,45,0,0,128,15,1,0,0,0,129,
        134,5,52,0,0,130,131,5,42,0,0,131,133,5,52,0,0,132,130,1,0,0,0,133,
        136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,0,0,0,136,
        134,1,0,0,0,137,138,5,40,0,0,138,139,3,18,9,0,139,140,3,6,3,0,140,
        17,1,0,0,0,141,146,5,9,0,0,142,146,5,10,0,0,143,144,5,9,0,0,144,
        146,5,10,0,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,0,146,
        19,1,0,0,0,147,148,5,12,0,0,148,150,5,52,0,0,149,151,3,14,7,0,150,
        149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,14,0,0,153,
        157,5,1,0,0,154,156,3,4,2,0,155,154,1,0,0,0,156,159,1,0,0,0,157,
        155,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,1,0,0,0,160,
        161,5,2,0,0,161,162,5,12,0,0,162,163,5,41,0,0,163,21,1,0,0,0,164,
        165,5,13,0,0,165,166,5,52,0,0,166,175,5,44,0,0,167,172,5,52,0,0,
        168,169,5,42,0,0,169,171,5,52,0,0,170,168,1,0,0,0,171,174,1,0,0,
        0,172,170,1,0,0,0,172,173,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,
        0,175,167,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,5,45,0,
        0,178,179,5,40,0,0,179,180,5,52,0,0,180,181,5,14,0,0,181,185,5,1,
        0,0,182,184,3,2,1,0,183,182,1,0,0,0,184,187,1,0,0,0,185,183,1,0,
        0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,185,1,0,0,0,188,189,5,2,
        0,0,189,190,5,13,0,0,190,191,5,41,0,0,191,23,1,0,0,0,192,193,3,26,
        13,0,193,194,3,28,14,0,194,195,3,26,13,0,195,25,1,0,0,0,196,197,
        7,1,0,0,197,27,1,0,0,0,198,199,7,2,0,0,199,29,1,0,0,0,21,33,42,47,
        57,64,67,76,83,86,89,97,107,111,124,134,145,150,157,172,175,185
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
                      "OP_LESS_EQ", "OP_GREATER", "OP_GREATER_EQ", "OP_PLUS", 
                      "OP_MINUS", "OP_MUL", "OP_DIV", "OP_MOD", "OP_AND", 
                      "OP_OR", "OP_NOT", "OP_DOT", "OP_COLON", "OP_SEMICOLON", 
                      "OP_COMMA", "OP_ARROW", "OP_LPAREN", "OP_RPAREN", 
                      "OP_LBRACKET", "OP_RBRACKET", "LIT_INT", "LIT_FLOAT", 
                      "LIT_STRING", "LIT_CHAR", "IDENTIFIER", "LINE_COMMENT", 
                      "MULTILINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_nonDeclarativeStatement = 2
    RULE_literal = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_assignment = 6
    RULE_formalParameterPart = 7
    RULE_parameterSpecification = 8
    RULE_modeSpecifier = 9
    RULE_procedureDeclaration = 10
    RULE_functionDeclaration = 11
    RULE_condition = 12
    RULE_expression = 13
    RULE_relop = 14

    ruleNames =  [ "program", "statement", "nonDeclarativeStatement", "literal", 
                   "ifStatement", "loopStatement", "assignment", "formalParameterPart", 
                   "parameterSpecification", "modeSpecifier", "procedureDeclaration", 
                   "functionDeclaration", "condition", "expression", "relop" ]

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
    OP_PLUS=31
    OP_MINUS=32
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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627374728) != 0):
                self.state = 30
                self.statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(GreekBaseParser.EOF)
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


        def getRuleIndex(self):
            return GreekBaseParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GreekBaseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.loopStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.assignment()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonDeclarativeStatement" ):
                return visitor.visitNonDeclarativeStatement(self)
            else:
                return visitor.visitChildren(self)




    def nonDeclarativeStatement(self):

        localctx = GreekBaseParser.NonDeclarativeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nonDeclarativeStatement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.ifStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.loopStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = GreekBaseParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
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
            self.state = 51
            self.match(GreekBaseParser.KW_IF)
            self.state = 52
            self.condition()
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 53
                self.match(GreekBaseParser.KW_THEN)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 54
                    self.nonDeclarativeStatement()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 60
                    self.match(GreekBaseParser.KW_ELSE)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                        self.state = 61
                        self.nonDeclarativeStatement()
                        self.state = 66
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 69
                self.match(GreekBaseParser.KW_END)
                self.state = 70
                self.match(GreekBaseParser.KW_IF)
                self.state = 71
                self.match(GreekBaseParser.OP_SEMICOLON)
                pass
            elif token in [22]:
                self.state = 72
                self.match(GreekBaseParser.KW_LCURL)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 73
                    self.nonDeclarativeStatement()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==5:
                    self.state = 79
                    self.match(GreekBaseParser.KW_ELSE)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                        self.state = 80
                        self.nonDeclarativeStatement()
                        self.state = 85
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 88
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
            self.state = 91
            self.match(GreekBaseParser.KW_WHILE)
            self.state = 92
            self.condition()
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 93
                self.match(GreekBaseParser.KW_LOOP)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 94
                    self.nonDeclarativeStatement()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 100
                self.match(GreekBaseParser.KW_END)
                self.state = 101
                self.match(GreekBaseParser.KW_LOOP)
                self.state = 102
                self.match(GreekBaseParser.OP_SEMICOLON)
                pass
            elif token in [22]:
                self.state = 103
                self.match(GreekBaseParser.KW_LCURL)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                    self.state = 104
                    self.nonDeclarativeStatement()
                    self.state = 109
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 110
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GreekBaseParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 114
            self.match(GreekBaseParser.OP_ASSIGN)
            self.state = 115
            self.expression()
            self.state = 116
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterPart" ):
                return visitor.visitFormalParameterPart(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterPart(self):

        localctx = GreekBaseParser.FormalParameterPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_formalParameterPart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(GreekBaseParser.OP_LPAREN)
            self.state = 119
            self.parameterSpecification()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 120
                self.match(GreekBaseParser.OP_SEMICOLON)
                self.state = 121
                self.parameterSpecification()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterSpecification" ):
                return visitor.visitParameterSpecification(self)
            else:
                return visitor.visitChildren(self)




    def parameterSpecification(self):

        localctx = GreekBaseParser.ParameterSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 130
                self.match(GreekBaseParser.OP_COMMA)
                self.state = 131
                self.match(GreekBaseParser.IDENTIFIER)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self.match(GreekBaseParser.OP_COLON)
            self.state = 138
            self.modeSpecifier()
            self.state = 139
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModeSpecifier" ):
                return visitor.visitModeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def modeSpecifier(self):

        localctx = GreekBaseParser.ModeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_modeSpecifier)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(GreekBaseParser.KW_IN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(GreekBaseParser.KW_OUT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.match(GreekBaseParser.KW_IN)
                self.state = 144
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureDeclaration" ):
                return visitor.visitProcedureDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def procedureDeclaration(self):

        localctx = GreekBaseParser.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GreekBaseParser.KW_PROCEDURE)
            self.state = 148
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 149
                self.formalParameterPart()


            self.state = 152
            self.match(GreekBaseParser.KW_IS)
            self.state = 153
            self.match(GreekBaseParser.KW_BEGIN)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627370632) != 0):
                self.state = 154
                self.nonDeclarativeStatement()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(GreekBaseParser.KW_END)
            self.state = 161
            self.match(GreekBaseParser.KW_PROCEDURE)
            self.state = 162
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = GreekBaseParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GreekBaseParser.KW_FUNCTION)
            self.state = 165
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 166
            self.match(GreekBaseParser.OP_LPAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 167
                self.match(GreekBaseParser.IDENTIFIER)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 168
                    self.match(GreekBaseParser.OP_COMMA)
                    self.state = 169
                    self.match(GreekBaseParser.IDENTIFIER)
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 177
            self.match(GreekBaseParser.OP_RPAREN)
            self.state = 178
            self.match(GreekBaseParser.OP_COLON)
            self.state = 179
            self.match(GreekBaseParser.IDENTIFIER)
            self.state = 180
            self.match(GreekBaseParser.KW_IS)
            self.state = 181
            self.match(GreekBaseParser.KW_BEGIN)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627374728) != 0):
                self.state = 182
                self.statement()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(GreekBaseParser.KW_END)
            self.state = 189
            self.match(GreekBaseParser.KW_FUNCTION)
            self.state = 190
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = GreekBaseParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.expression()
            self.state = 193
            self.relop()
            self.state = 194
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
            return self.getToken(GreekBaseParser.IDENTIFIER, 0)

        def LIT_INT(self):
            return self.getToken(GreekBaseParser.LIT_INT, 0)

        def LIT_FLOAT(self):
            return self.getToken(GreekBaseParser.LIT_FLOAT, 0)

        def LIT_STRING(self):
            return self.getToken(GreekBaseParser.LIT_STRING, 0)

        def getRuleIndex(self):
            return GreekBaseParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = GreekBaseParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6473924464345088) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = GreekBaseParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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






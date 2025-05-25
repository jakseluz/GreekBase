from dataclasses import dataclass
from typing import List


class ASTNode:
    pass

class Statement(ASTNode):
    pass

class NonDeclarativeStatement(Statement):
    pass

@dataclass
class Program(ASTNode):
    statements: List[Statement]

class Expression(ASTNode):
    pass

class Literal(Expression):
    pass

class RelationOperator(ASTNode):
    pass


# LITERALS
@dataclass
class IntLiteral(Literal):
    value: int

@dataclass
class FloatLiteral(Literal):
    value: float

@dataclass
class CharLiteral(Literal):
    value: str

@dataclass
class StringLiteral(Literal):
    value: str


# CONDITION
@dataclass
class Condition(ASTNode):
    left: Expression
    operator: RelationOperator
    right: Expression


# EXPRESSIONS
@dataclass
class MultiplicationOperator(Expression):
    left: Expression
    operator: str                 # multiplication or divison
    right: Expression

@dataclass
class AdditionOperator(Expression):
    left: Expression
    operator: str                 # addition or substraction
    right: Expression

@dataclass
class ParenthesisExpression(Expression):
    value: Expression

@dataclass
class Identifier(Expression):
    value: str


# NON-DECLARATIVE STATEMENTS
@dataclass
class IfStatement(NonDeclarativeStatement):
    condition: Condition
    then : List[NonDeclarativeStatement]
    else_branch: List[NonDeclarativeStatement]

@dataclass
class LoopStatement(NonDeclarativeStatement):
    condition: Condition
    then: List[NonDeclarativeStatement]

@dataclass
class Assignment(NonDeclarativeStatement):
    id: Identifier
    value: Expression

@dataclass
class PrintStatement(NonDeclarativeStatement):
    value: Expression


# RELATION OPERATORS
@dataclass
class EqualityOperator(RelationOperator):
    value: str

@dataclass
class NonEqualityOperator(RelationOperator):
    value: str

@dataclass
class LessThanOperator(RelationOperator):
    value: str

@dataclass
class LessOrEqualThanOperator(RelationOperator):
    value: str

@dataclass
class GreaterThanOperator(RelationOperator):
    value: str

@dataclass
class GreaterOrEqualThanOperator(RelationOperator):
    value: str


# PROCEDURE
@dataclass
class ModeSpecifier(ASTNode):
    value: str

@dataclass
class ParameterSpecification(ASTNode):
    id: List[Identifier]
    mode: ModeSpecifier
    literal: Literal

@dataclass
class FormalParameterPart(ASTNode):
    parameterSpecification: List[ParameterSpecification]

@dataclass
class Procedure(Statement):
    id: Identifier
    formalParameterPart: FormalParameterPart
    body: List[NonDeclarativeStatement]


# variables
@dataclass
class VariableDeclaration(NonDeclarativeStatement):
    varType: Literal
    id: Identifier
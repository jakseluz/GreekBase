from dataclasses import dataclass
from typing import List


@dataclass
class ASTNode:
    line: int
    column: int

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

class VariableType(ASTNode):
    pass

class Atom(ASTNode):
    pass


# LITERALS
@dataclass
class IntLiteral(Literal):
    value: int

@dataclass
class FloatLiteral(Literal):
    value: float

@dataclass
class BoolLiteral(Literal):
    value: bool

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
    left: Atom
    operator: str
    right: Atom

@dataclass
class AdditionOperator(Expression):
    left: MultiplicationOperator
    operator: str
    right: MultiplicationOperator

@dataclass
class ParenthesisExpression(Atom):
    value: Expression

@dataclass
class Identifier(Expression):
    value: str
    type: str


# variables
@dataclass
class VariableDeclaration(NonDeclarativeStatement):
    varType: VariableType
    id: Identifier
    varValue : Literal | None


# functions
@dataclass
class FunctionDeclaration(Statement):
    name: Identifier
    parameters: List[VariableDeclaration]
    return_type: VariableType | None
    statements: List[Statement]

@dataclass
class FunctionCall(Atom):
    name: Identifier
    parameters: List[Expression]


# NON-DECLARATIVE STATEMENTS
@dataclass
class IfStatement(NonDeclarativeStatement):
    condition: Condition
    then_branch : List[NonDeclarativeStatement]
    else_branch: List[NonDeclarativeStatement] | None

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
    value: Identifier | Literal | FunctionCall
    # id: str | None # TODO


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




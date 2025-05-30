#!/bin/bash
# for use on Linux
# creating antlr/generated folder containing ANTLR's generated files
mkdir -p antlr/generated
antlr4 -Dlanguage=Python3 -no-listener -visitor -Xexact-output-dir -o antlr/generated antlr/GreekBaseLexer.g4 -lib antlr/generated  antlr/GreekBaseParser.g4
touch antlr/generated/__init__.py
echo "# antlr/generated/__init__.py
from .GreekBaseLexer import *
from .GreekBaseParser import *
from .GreekBaseParserVisitor import *" > antlr/generated/__init__.py

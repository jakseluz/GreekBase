REM This script generates Python files from ANTLR grammar files for the GreekBase language.


@echo off
mkdir antlr\generated 2>nul
REM Ensure you have ANTLR installed and the path to the jar file is correct.
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 -no-listener -visitor -Xexact-output-dir -o antlr\generated antlr\GreekBaseLexer.g4 antlr\GreekBaseParser.g4
echo from .GreekBaseLexer import * > antlr\generated\__init__.py
echo from .GreekBaseParser import * >> antlr\generated\__init__.py
echo from .GreekBaseParserVisitor import * >> antlr\generated\__init__.py

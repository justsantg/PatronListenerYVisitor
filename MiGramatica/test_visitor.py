from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

input_code = "for (i = 0; i < 3; i = i + 1) { x = x + 2; };"
input_stream = InputStream(input_code)
lexer = MiGramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiGramaticaParser(token_stream)
tree = parser.programa()

visitor = EvalVisitor()
visitor.visit(tree)

print("📌 Valores finales de las variables:", visitor.variables)

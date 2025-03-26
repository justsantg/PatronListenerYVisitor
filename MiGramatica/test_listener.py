from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener

input_stream = InputStream("for (i = 0; i < 3; i = i + 1) { x = x + 2; };")
lexer = MiGramaticaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiGramaticaParser(token_stream)
tree = parser.programa()

listener = MyListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)

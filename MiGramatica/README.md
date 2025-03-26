pip install antlr4-python3-runtime
antlr4 -Dlanguage=Python3 -visitor -listener MiGramatica.g4
python test_listener.py
python test_visitor.py
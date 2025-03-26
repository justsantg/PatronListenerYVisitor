from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar variables

    def visitAssign(self, ctx):
        """ Maneja asignaciones como x = 5 """
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())  

        # 🔥 Asegurar que la expresión devuelva un número válido
        if value is None:
            print(f"⚠️ Error: Asignación de {var} devolvió None, se ajusta a 0")
            value = 0

        self.variables[var] = value
        print(f"✅ Asignación: {var} = {value}")
        return value

    def visitInicializacion(self, ctx):
        """ Maneja la inicialización del for (Ej: i = 0) """
        print(f"📌 Inicializando: {ctx.getText()}")
        return self.visitAssign(ctx)

    def visitForLoop(self, ctx):
        """ Simula la ejecución de un ciclo for """
        self.visit(ctx.inicializacion())  
        print(f"🚀 Estado inicial de variables: {self.variables}")

        while self.visit(ctx.condicion()):  
            for stmt in ctx.sentencia():
                self.visit(stmt)

            self.visit(ctx.actualizacion())  
            print(f"🔄 Estado de variables después de actualización: {self.variables}")

    def visitCondicion(self, ctx):
        """ Evalúa la condición del for (Ej: i < 3) """
        var = ctx.ID().getText()
        op = ctx.op.text
        val = int(ctx.INT().getText())

        if var not in self.variables:
            print(f"⚠️ La variable {var} no estaba inicializada, asignando 0")
            self.variables[var] = 0

        resultado = eval(f"{self.variables[var]} {op} {val}")
        print(f"🔍 Evaluando condición: {var} {op} {val} → {resultado}")
        return resultado

    def visitExpresion(self, ctx):
        """ Evalúa expresiones matemáticas correctamente """
        if ctx.INT():
            valor = int(ctx.INT().getText())
            print(f"🧩 Evaluando número entero: {valor}")
            return valor
        elif ctx.ID():
            var_name = ctx.ID().getText()
            valor = self.variables.get(var_name, 0)
            print(f"🧩 Evaluando variable: {var_name} → {valor}")
            return valor
        elif ctx.op:
            left = self.visit(ctx.expresion(0))
            right = self.visit(ctx.expresion(1))
            resultado = eval(f"{left} {ctx.op.text} {right}")
            print(f"🧮 Evaluando expresión: {left} {ctx.op.text} {right} = {resultado}")
            return resultado
        return 0  

    def visitActualizacion(self, ctx):
        """ Evalúa la actualización del for (Ej: i = i + 1) """
        return self.visitAssign(ctx)

from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print(f"🌀 Detectado un 'for' en línea {ctx.start.line}")

    def exitInicializacion(self, ctx):
        print(f"🔹 Inicialización: {ctx.getText()}")

    def exitCondicion(self, ctx):
        print(f"🔸 Condición: {ctx.getText()}")

    def exitActualizacion(self, ctx):
        print(f"🔺 Actualización: {ctx.getText()}")

    def exitAssign(self, ctx):
        print(f"✅ Asignación detectada: {ctx.getText()}")

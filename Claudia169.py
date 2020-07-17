class Mouse:
    def _init_(self,marca,color, tipo):
        self._marca = marca
        self._color = color
        self._tipo = tipo
    @property
    def marca (self):
        return self._marca

    @property
    def color (self):
        return self._color

    @property
    def color (self):
        return self._tipo

    def imprimir (self):
        print ("Mouse existente")
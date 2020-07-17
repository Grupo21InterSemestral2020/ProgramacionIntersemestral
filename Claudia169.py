class Mouse:
    def _init_(self,marca,color, tipo):
        self._marca = marca
        self._color = color
        self._tipo = tipo

    @property
    def marca (self):

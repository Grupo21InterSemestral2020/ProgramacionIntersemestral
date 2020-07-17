class Mouse:
    cantidadMouse = 0
    def _init_(self,marca="Logitech",color="Negro", tipo="Inalambrico"):
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
        Mouse.cantidadMouse +=1

    def imprimirinfo(self):
        print(f"Marca: {self._marca}, Color: {self._color}, Tipo: {self._tipo}")



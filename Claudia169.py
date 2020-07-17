class Mouse:
    cantidadMouse = 0
    def _init_(self,marca,color, tipo):
        self._marca = marca
        self._color = color
        self._tipo = tipo
    @property
    def marca (self):
        return self._marca

    @marca.setter
    def marca (self,marcaNueva):
        self._marca=marcaNueva

    @property
    def color (self):
        return self._color

    @color.setter
    def color (self):
        self._color=colorVariedad

    @property
    def tipo (self):
        return self._tipo

    @tipo.setter
    def tipo (self):
        self._tipo=tipoVariedad

   
        Mouse.cantidadMouse +=1

    def imprimirinfo(self):
        print(f"Marca: {self._marca}, Color: {self._color}, Tipo: {self._tipo}")

m1 = Mouse("Logitech","Negro","Inalambrico")

print (f"Mouse disponibles: {Mouse.cantidadMouse}")
m1.tipo ="Inalambrico"
m1.color="Negro"



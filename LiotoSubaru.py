class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo

    @property
    def marca (self):
        return self.__marca

    @property
    def color (self):
        return self.__color

    @property
    def tipo (self):
        return self.__tipo

    @marca.setter
    def marca (self,marca1):
        self.__marca = marca1

    @color.setter
    def color (self,color1):
        self.__color = color1

    @tipo.setter
    def tipo (self,tipo1):
        self.__tipo = tipo1

    def informacion(self):
        print(f"Marca: {self.__marca}\n Color: {self.__color}\n Tipo: {self.__tipo}\n\n")

m1 = Mouse("Dell","Rojo","Inalambrico")
m2 = Mouse("Logitech","Gris","Alambrico")

m1.informacion()
m2.informacion()

class mouse:
    def __initi__ (self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo
    @property 
    def marca (self):
        return self._marca

    @property
    def color (self):
        return self._color

    @property 
    def tipo (self):
        return self._tipo



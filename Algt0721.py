class Mouse:
    def __init__(self,marca,color,tipo):
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo 

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,valor):
        self.__marca = valor
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,valor):
        self.__color = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,valor):
        self.__tipo = valor 
    
    def ImpInfo(self):
        print(f'Marca {self.__marca}, Color:{self.__color},Tipo:{self.__tipo}')
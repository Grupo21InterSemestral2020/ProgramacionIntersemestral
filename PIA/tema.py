import os
class Tema:
    def __init__(self,idTema,Nombre):
        self.__idTema = idTema
        self.__Nombre = Nombre
        
    @property
    def idTema(Self):
        return self.__idTema

    @property
    def Nombre(self):
        return self.__Nombre

    @idTema.setter
    def idTema(self,valor):
        self.__idTema = valor
    
    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre = valor
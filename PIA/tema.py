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

    def AgregarTema(self):
        self.archivo = open("./BD/temas.txt","a",encoding="utf8")
        self.__idTema = input("Ingrese el ID:\n")
        with open("./BD/temas.txt","r",encoding="utf8") as temas:
            num = temas.readlines()
            for f in num:
                while self.__idTema in f: 
                    self.__idTema = input("Lo siento, ese ID ya existe, ingrese otro!!:\n")
                temas.close()
        self.__Nombre = input("Ingrese Nombre del Tema:\n")
        self.archivo.write(self.__idTema + "|" + self.__Nombre + "\n")
        self.archivo.close()
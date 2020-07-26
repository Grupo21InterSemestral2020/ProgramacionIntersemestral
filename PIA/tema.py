import os
class Tema:
    def __init__(self,idTema,Nombre):
        self.__idTema = idTema
        self.__Nombre = Nombre
        
    @property
    def idTema(self):
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

    def EliminarTema(self):
        self.archivo = open("./BD/temas.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/temas_temp.txt","w",encoding="utf8")
        self.id_delete = input("ID del Tema a borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/temas.txt")
        os.rename("./BD/temas_temp.txt","./BD/temas.txt")
    
    def ConsultaTema(self):
        self.archivo = open("./BD/temas.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()

    def InfoTema(self):
        self.archivo = open("./BD/temas.txt",encoding="utf8")
        self.id_temasearch = input("Ingresa ID del Tema a buscar su información:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_temasearch == id:
                print(renglon)
        self.archivo.close()
        
    def ModificarTema(self):
        self.archivo = open("./BD/temas.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/temas_temp.txt","w",encoding="utf8")
        self.id_change = input("Actual ID:\n")
        self.__idTema = input("Nuevo ID\n:")
        self.__Nombre = input("Ingrese Nuevo Nombre:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.__idTema + "|" + self.__Nombre + "\n")
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/temas.txt")
        os.rename("./BD/temas_temp.txt","./BD/temas.txt")
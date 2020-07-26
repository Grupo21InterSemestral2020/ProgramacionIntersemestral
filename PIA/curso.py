import os
class Curso:
    def __init__(self,idCurso,Descripcion,Empleado):
        self.__idCurso = idCurso
        self.__Descripcion = Descripcion
        self.__Empleado = Empleado

    @property
    def idCurso(self):
        return self.__idCurso

    @property
    def Descripcion(self):
        return self.__Descripcion

    @property
    def Empleado(self):
        return self.__Empleado

    @idCurso.setter
    def idCurso(self,valor):
        self.__idCurso = valor
    
    @Descripcion.setter
    def Descripcion(self,valor):
        self.__Descripcion = valor

    @Empleado.setter
    def Empleado(self,valor):
        self.__Empleado = valor

    def AgregarCurso(self):
        self.archivo = open("./BD/curso.txt","a",encoding="utf8")
        self.__idCurso = input("Ingrese el ID:\n")
        with open("./BD/curso.txt","r",encoding="utf8") as curso:
            num = curso.readlines()
            for f in num:
                while self.__idCurso in f: 
                    self.__idCurso = input("Lo siento, ese ID ya existe, ingrese otro!!:\n")
                curso.close()
        self.__Descripcion = input("Ingrese Descripcion:\n")
        self.__Empleado = input("Ingrese Id del Empleado:\n")
        self.archivo.write(self.__idCurso + "|" + self.__Descripcion + "|" + self.__Empleado + "\n")
        self.archivo.close()
   
    def EliminarCurso(self):
        self.archivo = open("./BD/curso.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/curso_temp.txt","w",encoding="utf8")
        self.id_delete = input("ID del Empleado a borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/curso.txt")
        os.rename("./BD/curso_temp.txt","./BD/curso.txt")
    
    def ConsultaCurso(self):
        self.archivo = open("./BD/curso.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()


    def InfoCurso(self):
        self.archivo = open("./BD/curso.txt",encoding="utf8")
        self.id_cursosearch = input("Ingresa ID del curso a cursar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_cursoearch == id:
                print(renglon)
        self.archivo.close()
        
    def ModificarCurso(self):
        self.archivo = open("./BD/curso.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/curso_temp.txt","w",encoding="utf8")
        self.id_change = input("Actual ID:\n")
        self.__idCurso = input("Nuevo ID\n:")
        self.__Descripcion = input("Ingrese Nueva Descripcion:\n")
        self.__Empleado = input("Ingrese nueva empleado:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.__idCurso + "|" + self.__Descripcion + "|" + self.__Empleado + "\n")
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/curso.txt")
        os.rename("./BD/curso_temp.txt","./BD/curso.txt")
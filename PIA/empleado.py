import os
class Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__Direccion = Direccion

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @property
    def Nombre(self):
        return self.__Nombre

    @property
    def Direccion(self):
        return self.__Direccion

    @idEmpleado.setter
    def idEmpleado(self,valor):
        self.__idEmpleado = valor
    
    @Nombre.setter
    def Nombre(self,valor):
        self.__Nombre = valor

    @Direccion.setter
    def Direccion(self,valor):
        self.__Direccion = valor

    def AgregarEmpleado(self):
        self.archivo = open("./BD/empleados.txt","a",encoding="utf8")
        self.__idEmpleado = input("Id \n")
        with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
            num = empleados.readlines()
            for f in num:
                while self.__idEmpleado in f: 
                    self.__idEmpleado = input("Lo siento, ese ID ya existe, ingrese otro:\n")
                empleados.close()
        print("Nombre del Empleado:\n")
        self.__Nombre = input("Nombre: \n")
        print("Direccion del Empleado")
        self.__Direccion = input("> ")
        self.archivo.write(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion + "\n")
        self.archivo.close()
   
    def EliminarEmpleado(self):
        self.archivo = open("./BD/empleados.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/empleados_temp.txt","w",encoding="utf8")

        print("ID a borrar")
        self.id_delete = input("ID Del:")

        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)
    
        self.archivo.close()
        self.archivo_temporal.close()

        os.remove("./BD/empleados.txt")
        os.rename("./BD/empleados_temp.txt","./BD/empleados.txt")

E = Empleado(0,0,0)
E.AgregarEmpleado()
E.AgregarEmpleado()
E.EliminarEmpleado()
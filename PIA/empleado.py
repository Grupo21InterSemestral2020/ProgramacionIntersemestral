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
        self.__idEmpleado = input("Ingrese el ID:\n")
        with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
            num = empleados.readlines()
            for f in num:
                while self.__idEmpleado in f: 
                    self.__idEmpleado = input("Lo siento, ese ID ya existe, ingrese otro!!:\n")
                empleados.close()
        self.__Nombre = input("Ingrese Nombre del Empleado:\n")
        self.__Direccion = input("Ingrese Dirección del Empleado:\n")
        self.archivo.write(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion + "\n")
        self.archivo.close()
   
    def EliminarEmpleado(self):
        self.archivo = open("./BD/empleados.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/empleados_temp.txt","w",encoding="utf8")
        self.id_delete = input("ID del Empleado a borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/empleados.txt")
        os.rename("./BD/empleados_temp.txt","./BD/empleados.txt")
    
    def ConsultaEmpleado(self):
        self.archivo = open("./BD/empleados.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()


    def InfoEmpleado(self):
        self.archivo = open("./BD/empleados.txt",encoding="utf8")
        self.id_empleadosearch = input("Ingresa ID del empleado a buscar su información:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_empleadosearch == id:
                print(renglon)
        self.archivo.close()
        
    def ModificarEmpleado(self):
        self.archivo = open("./BD/empleados.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/empleados_temp.txt","w",encoding="utf8")
        self.id_change = input("Actual ID:\n")
        self.__idEmpleado = input("Nuevo ID\n:")
        self.__Nombre = input("Ingrese Nuevo Nombre:\n")
        self.__Direccion = input("Ingrese nueva dirección:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.__idEmpleado + "|" + self.__Nombre + "|" + self.__Direccion + "\n")
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/empleados.txt")
        os.rename("./BD/empleados_temp.txt","./BD/empleados.txt")
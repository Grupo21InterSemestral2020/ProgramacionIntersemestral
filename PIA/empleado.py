class Empleado:
    def __init__(self,idEmpleado,Nombre,Direccion):
        self.__idEmpleado = idEmpleado
        self.__Nombre = Nombre
        self.__Direccion = Direccion

    @property
    def idEmpleado(Self):
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

    def AgregarEmpleado():
        archivo = open("./BD/empleados.txt","a",encoding="utf8")
        idEmpleado = input("Ingresa el ID con el que registraras al Empleado:\n")
        with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
            num = empleados.readlines()
            for f in num:
                while idEmpleado in f: 
                    idEmpleado = input("Lo siento, ese ID ya existe, ingrese otro:\n")
            Nombre = str(input("Ingresa su Nombre:\n"))
            Direccion = str(input("Ingresa su Dirección:\n"))
            archivo.write(f"{idEmpleado} | {Nombre} | {Direccion}\n")
            archivo.close
    def EliminarEmpleado():
        

Empleado.AgregarEmpleado()
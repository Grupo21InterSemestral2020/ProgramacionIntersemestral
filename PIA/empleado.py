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
        empleados = open("./BD/empleados.txt","r",encoding="utf8")
        num = empleados.readlines()
        empleados.close
        idEmpleado = input("Ingresa el ID con el que registraras al Empleado:\n")
        with open("./BD/empleados.txt","a+",encoding="utf8") as empleados:
            for f in num:
                while idEmpleado in f: 
                    idEmpleado = input("Lo siento, ese ID ya existe, ingrese otro:\n")
            Nombre = str(input("Ingresa su Nombre:\n"))
            Direccion = str(input("Ingresa su Dirección:\n"))
            empleados.write(idEmpleado + '|' + Nombre + '|' + Direccion + '\n')
            empleados.close
   
    def EliminarEmpleado():
        empleados = open("./BD/empleados.txt","r",encoding="utf8")
        lines = empleados.readlines()
        print(lines)
        empleados.close()
        empleados = open("./BD/empleados.txt","w+",encoding="utf8")
        idEmpleado = int(input("Ingrese Id de empleado a eliminar: "))
        for line in lines:
            id = line.split("|")[0]
            if line!=id:
                empleados.write(line)
        lines = empleados.readlines()
        print(lines)
        empleados.close()

Empleado.AgregarEmpleado()
Empleado.AgregarEmpleado()
Empleado.EliminarEmpleado()
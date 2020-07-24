import os
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

    def AgregarEmpleado(self):
        self.archivo = open("./BD/empleados.txt","a",encoding="utf8")
        self.__idEmpleado = input("Id \n")
        with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
            num = empleados.readlines()
            for f in num:
<<<<<<< HEAD
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
=======
                while idEmpleado in f: 
                    idEmpleado = input("Lo siento, ese ID ya existe, ingrese otro:\n")
            Nombre = str(input("Ingresa su Nombre:\n"))
            Direccion = str(input("Ingresa su Dirección:\n"))
<<<<<<< HEAD
            archivo.write(f"{idEmpleado} | {Nombre} | {Direccion}\n")
            archivo.close
    
    def EliminarEmpleado():
        empleados = open("./BD/empleados.txt","r",encoding="utf8")
        num = empleados.readlines()
        empleados = open("./BD/empleados.txt","w",encoding="utf8")
        idEmpleado = input("Ingrese el ID a Eliminar: ")
        for f in num:
            id1 = f.split("|")[0]
            id2 = f.split("|")[1]
            if idEmpleado!= id1:
               empleados.write(id2)
        empleados.close()

    def ModificarEmpleado():
        pass

Empleado.AgregarEmpleado()
with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
    print(empleados.readlines())
Empleado.AgregarEmpleado()
with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
    print(empleados.readlines())
#Empleado.EliminarEmpleado()
#with open("./BD/empleados.txt","r",encoding="utf8") as empleados:
#    print(empleados.readlines())

archivo = open("./BD/empleados.txt","r",encoding="utf8")
lines = archivo.readlines()
archivo.close()
archivo = open("./BD/empleados.txt","w",encoding="utf8")
idEmpleado = input("Ingrese Id de empleado a modificar: ")
    
for line in lines:
    id = line.split("|")[0]
    if idEmpleado != id:
        archivo.write(line)
    else:
        print("Ingrese nuevos datos de empleado: ")
        idEmpleado=input("Ingrese id: ")
        Nombre=str(input("Nombre: "))
        Direccion=str(input("Direccion:"))
        archivo.writelines(idEmpleado + "|" + Nombre + "|" + Direccion + "\n")        
        #<3<3<3<<33<3<3<3<3<3<3<3<3       Yaki  y  Johan    <3<3<3<3<3<3<33<3<3<3<3<33
=======
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
>>>>>>> ad213252f7e676a226b99266ee89b995d489de06
>>>>>>> 58f9c2b504f8fc80827c18c1a224660c039168d4

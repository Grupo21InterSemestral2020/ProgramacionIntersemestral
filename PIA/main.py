from curso import *
from empleado import *
from video import *
from tema import *
from curso_tema import *
from curso_tema_video import *
import os

C = Curso(0,0,0)
E = Info_Empleado(0,0,0)
V = Video(0,0,0,0)
T = temas(0,0)
CT = Curso_Tema(0,0,0)
CTV = Curso_Tema_Video(0,0,0)

def menu_principal():
    print("\n")
    print("*"*50)
    opcion = int(input("Elige un archivo\n1.Cursos\n2.Empleados\n3.Videos\n4.Temas\n5.Temas de los Cursos\n6.Videos de los Temas\n7.Salir\n"))
    return opcion

def menu_opciones():
    print("*"*50)
    opcion = int(input("¿Que accion quieres realizar?\n1. Agregar\n2. Borrar\n3. Modificar\n4. Consultar todos los registros\n5. Ver detalles de un solo registro\n"))
    return opcion

opcion1 = menu_principal()
if opcion1 <= 6:
        opcion2 = menu_opciones()

while True:
    if opcion1 == 2:
        if opcion2 == 1:
            E.AgregarEmpleado()
        elif opcion2 == 2:
            E.EliminarEmpleado()
        elif opcion2 == 3:
            E.ModificarEmpleado()
        elif opcion2 == 4:
            E.ConsultaEmpleado()
        elif opcion2 == 5:
            E.InfoEmpleado()

    elif opcion1 == 4:
        if opcion2 == 1:
            T.AgregarTema()
        elif opcion2 == 2:
            T.EliminarTema()
        elif opcion2 == 3:
            T.ModificarTema()
        elif opcion2 == 4:
            T.ConsultaTema()
        elif opcion2 == 5:
            T.InfoTema()

    elif opcion1 == 7:
        quit()

    else:
        print("Opción Invalida, intente nuevamente")

    opcion1 = menu_principal()
    if opcion1 <= 6:
        opcion2 = menu_opciones()
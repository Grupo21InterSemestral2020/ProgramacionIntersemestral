from curso import *
from empleado import *
from video import *
from tema import *
from curso_tema import *
from curso_tema_video import *
import os

C = Curso(0,0,0)
E = Empleado(0,0,0)
V = Video(0,0,0,0)
T = Tema(0,0)
CT = Curso_tema(0,0,0)
CTV = video_tema(0,0,0)

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
    if opcion1 == 1:
        if opcion2 == 1:
            C.AgregarCurso()
        elif opcion2 == 2:
            C.EliminarCurso()
        elif opcion2 == 3:
            C.ModificarCurso()
        elif opcion2 == 4:
            C.ConsultaCurso_()
        elif opcion2 == 5:
            C.InfoCurso()
    
    elif opcion1 == 2:
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
    
    elif opcion1 == 3:
        if opcion2 == 1:
            V.agregarVideo()
        elif opcion2 == 2:
            V.borrarVideo()
        elif opcion2 == 3:
            V.modificarVideo()
        elif opcion2 == 4:
            V.consultaVideos()
        elif opcion2 == 5:
            V.detallesVideo()

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
    
    elif opcion1 == 5:
        if opcion2 == 1:
            CT.AgregarTemaAsignado()
        elif opcion2 == 2:
            CT.EliminarTemaAsignado()
        elif opcion2 == 3:
            CT.ModificarTemaAsignado()
        elif opcion2 == 4:
            CT.ConsultaTemaAsignado()
        elif opcion2 == 5:
            CT.InfoTemaAsignado()
    
    elif opcion1 == 6:
        if opcion2 == 1:
            CTV.AgregarVideoAsignado()
        elif opcion2 == 2:
            CTV.EliminarVideoAsignado()
        elif opcion2 == 3:
            CTV.ModificarVideoAsignado()
        elif opcion2 == 4:
            CTV.ConsultaTemaAsignado()
        elif opcion2 == 5:
            CTV.InfoVideoAsignado()

    elif opcion1 == 7:
        quit()

    else:
        print("Opción Invalida, intente nuevamente")

    opcion1 = menu_principal()
    if opcion1 <= 6:
        opcion2 = menu_opciones()
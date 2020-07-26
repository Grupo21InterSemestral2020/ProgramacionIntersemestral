class Curso_tema:
    def __init__(self,idCursoTema,idCurso,idTema):
        self.__idCursoTema = idCursoTema
        self.__idCurso = idCurso
        self.__idTema = idTema

    @property
    def idCursoTema (self):
        return self.__idCursoTema

    @idCursoTema.setter 
    def idCursoTema (self,valorIdCursoT):
        self.__idCursoTema = valorIdCursoT

    @property
    def idCurso (self):
        return self.__idCurso

    @idCurso.setter
    def idCurso (self,valorIdCurso):
        self.__idCurso = valorIdCurso

    @property
    def idTema (self):
        return self.__idTema

    @idTema.setter
    def idTema (self,valorIdTema):
        self.__idTema = valorIdTema


    def AgregarTemaAsignado(self):
        self.archivo = open("./BD/curso_tema.txt","a",encoding="utf8")
        self.__idCursoTema = input("Ingrese el ID:\n")
        with open("./BD/curso_tema.txt","r",encoding="utf8") as curso:
            num = curso.readlines()
            for f in num:
                while self.__idCursoTema in f: 
                    self.__idCursoTema = input("Lo siento, ese ID ya existe, ingrese otro!!:\n")
                curso.close()
        self.__idCurso = input("Ingrese algún Id curso:\n")
        self.__idTema = input("Ingrese un Id Tema:\n")
        self.archivo.write(self.__idCursoTema + "|" + self.__idCurso + "|" + self.__idTema + "\n")
        self.archivo.close()


    def EliminarTemaAsignado(self):
        self.archivo = open("./BD/curso_tema.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/curso_tema.txt","w",encoding="utf8")
        self.id_delete = input("ID del Tema a borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
    
    def ConsultaTemaAsignado(self):
        self.archivo = open("./BD/curso_tema.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()

    def InfoTemaAsignado(self):
        self.archivo = open("./BD/curso_tema.txt",encoding="utf8")
        self.id_cursoTemasearch = input("Ingresa ID del Curso tema para buscar su información:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_cursoTemasearch == id:
                print(renglon)
        self.archivo.close()
        
    def ModificarTemaAsignado(self):
        self.archivo = open("./BD/curso_tema.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/cursoTema_temp.txt","w",encoding="utf8")
        self.id_change = input("Actual ID:\n")
        self.__idCursoTema = input("Nuevo ID Curso Tema\n:")
        self.__idCurso = input("Ingrese Nuevo ID Curso:\n")
        self.__idTema = input ("Ingresa Nuevo ID Tema")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.__idTema + "|" + self.__idCurso + "|" + self.__idCursoTema +"\n")
        self.archivo.close()
        self.archivo_temporal.close()

CT = Curso_tema(0,0,0)
CT.AgregarTemaAsignado()
CT.ModificarTemaAsignado()
CT.ConsultaTemaAsignado()
CT.EliminarTemaAsignado()
CT.InfoTemaAsignado()

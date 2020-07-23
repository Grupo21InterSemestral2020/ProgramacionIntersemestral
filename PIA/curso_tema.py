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
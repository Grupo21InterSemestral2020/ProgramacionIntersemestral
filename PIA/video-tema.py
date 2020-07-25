class video_tema:
    def __init__(self,idCursoTv, idVideo,idTema, idCurso):
        self.__idCursoTv = idCursoTv
        self.__idVideo = idCurso
        self.__idTema = idTema
    @property
    def idCursoTv (self):
        return self.__idCursoTv
    @idCursoTv.setter
    def idCursoTvs (self, valoridCursoTv):
        self.__idCursoTv = valoridCursoTv

    @property
    def idVideo (self):
        return self.__idVideo
    @idVideo.setter
    def idVideo (self, valoridVideo):
        self.__idVideo = valoridVideo
    
    @property
    def idTema (self):
        return self.__idTema
    @idTema.setter
    def idTema (self, valoridTema):
        self.__idTema = valoridTema

    @property
    def idcurso (self):
        return self.__idCurso
    @idCurso.setter
    def idCurso (self, valoridCurso):
        self.__idCurso = idCurso




class video_tema:
    def __init__(self,idCursoTv, idVideo,idCursoTema,):
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
    def idCursoTema (self):
        return self.__idCursoTema
    @idCursoTema.setter
    def idCursoTema (self, valoridCursoTema):
        self.__idCursoTema = valoridCursoTema

    



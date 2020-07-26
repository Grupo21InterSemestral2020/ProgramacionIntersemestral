class video_tema:
    def __init__(self,idCursoTv, idVideo,idCursoTema,):
        self.__idCursoTv = idCursoTv
        self.__idVideo = idCurso
        self.__idTema = idTema
    @property
    def idCursoTv (self):
        return self.__idCursoTv
    @idCursoTv.setter
    def idCursoTvs (self, valor):
        self.__idCursoTv = valor

    @property
    def idVideo (self):
        return self.__idVideo
    @idVideo.setter
    def idVideo (self, valor):
        self.__idVideo = valor
    
    @property
    def idCursoTema (self):
        return self.__idCursoTema
    @idCursoTema.setter
    def idCursoTema (self, valor):
        self.__idCursoTema = valor

      def AgregarVideoAsignado(self):
        self.archivo = open("./BD/curso_tema_videos.txt","a",encoding="utf8")
        self.__idCursoTv = input("Ingrese el ID:\n")
        with open("./BD/curso_tema_videos.txt","r",encoding="utf8") as tema:
            num = tema.readlines()
            for f in num:
                while self.__idCursoTv in f: 
                    self.__idCursoTv = input("Este ID ya existe, ingrese otro:\n")
                curso.close()



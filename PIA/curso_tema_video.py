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
        self.__idVideo = input("Ingrese un Id Video:\n")
        self.__idCursoTema = input("Ingrese un Id CursoTema:\n")
        self.archivo.write(self.__idCursoTv + "|" + self.__idVideo + "|" + self.__idCursoTema + "\n")
        self.archivo.close()

    def EliminarVideoAsignado(self):
        self.archivo = open("./BD/curso_tema_videos.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/video_temp.txt","w",encoding="utf8")
        self.id_delete = input("ID del Video a borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
    
    def ConsultaTemaAsignado(self):
        self.archivo = open("./BD/VideoAsignado.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()


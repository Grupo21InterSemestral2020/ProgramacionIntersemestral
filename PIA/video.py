class Video:

def __init__(self, idVideo, nombre, url, fechapublicacion):
    self.__idVideo = idVideo
    self.__nombre = nombre
    self.__url = url
    self.__fechapublicacion = fechapublicacion

    @property
    def idVideo(self):
        return self.__idVideo

    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = idVideo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = nombre

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, valor):
        self.__url = url

    @property
    def fechapublicacion(self):
        return self.__fechapublicacion

    @idVideo.setter
    def fechapublicacion(self, valor):
        self.__fechapublicacion = __fechapublicacion

    def agregarVideo(self):
            self.archivo = open("./BD/video.txt","a",encoding="utf8")
            self.__idVideo = input("Ingrese el ID del video que desea insertar:\n")
            with open("./BD/video.txt","r",encoding="utf8") as video:
                num = video.readlines()
                for f in num:
                    while self.__idVideo in f: 
                        self.__idVideo = input("Lo sentimos, ese ID ya existe, ingrese otro:\n")
                    video.close()
        self.__nombre = input("Ingrese nombre del video:\n")
        self.__url = input("Ingrese el url del video:\n")
        self.__fechapublicacion = input("Ingrese la fecha en que se publicó el video:\n")
        self.archivo.write(self.__idVideo + "|" + self.__nombre + "|" + self.__url + '|' + self.__fechapublicacion + "\n")
        self.archivo.close()
   
    def borrarVideo(self):
        self.archivo = open("./BD/video.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/video_temp.txt","w",encoding="utf8")
        self.id_delete = input("Inserte el ID del Video que desea borrar:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_delete != id:
                self.archivo_temporal.write(renglon)    
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/video.txt")
        os.rename("./BD/video_temp.txt","./BD/video.txt")
    
    def consultaVideos(self):
        self.archivo = open("./BD/video.txt",encoding="utf8")
        print(self.archivo.read())
        self.archivo.close()

    def detallesVideo(self):
        self.archivo = open("./BD/video.txt",encoding="utf8")
        self.id_videosearch = input("Ingrese el ID del video del cual desea tener información:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_videosearch == id:
                print(renglon)
        self.archivo.close()
        
    def modificarVideo(self):
        self.archivo = open("./BD/video.txt","r",encoding="utf8")
        self.archivo_temporal = open("./BD/video_temp.txt","w",encoding="utf8")
        self.id_change = input("Inserte el ID Actual:\n")
        self.__idVideo = input("Inserte el ID nuevo\n:")
        self.__nombre = input("Inserte el nuevo nombre del video:\n")
        self.__url = input("Ingrese la nueva url del video:\n")
        self.__fechapublicacion = input("Ingrese la fecha de la publicacion del video:\n")
        for renglon in self.archivo:
            id = renglon.split("|")[0]
            if self.id_change != id:
                self.archivo_temporal.write(renglon)
            elif self.id_change == id:
                self.archivo_temporal.write(self.__idVideo + "|" + self.__nombre + "|" + self.__url + '|' + self.__fechapublicacion "\n")
        self.archivo.close()
        self.archivo_temporal.close()
        os.remove("./BD/video.txt")
        os.rename("./BD/video_temp.txt","./BD/video.txt")

E = Video(0,0,0)
E.agregarVideo()
E.agregarVideo()
E.modificarVideo()
E.consultaVideos()
E.borrarVideo()
E.detallesVideo()
                    

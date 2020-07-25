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

    @static.method
        def agregarvideo():
            while True:
                while True:
                    try
                        idVideo=int(input("Ingrese ID del Video: "))
                        break
                    except:
                        
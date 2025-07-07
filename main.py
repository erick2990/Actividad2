class cliente():

    def __init__(self, nombre, telefono, correo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo

    #Metodos Setter and getters
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre #Esto sirve por si desea cambiarse el nombre
    def get_telefono(self):
        return self.__nombre
    def set_telefono(self, numero_nuevo):
        self.__telefono = numero_nuevo
    def get_correo(self):
        return self.__correo
    def set_correo(self, nuevo_correo):
        self.__correo = nuevo_correo



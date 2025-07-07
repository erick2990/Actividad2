class Cliente:

    def __init__(self, nombre, phone, email, list_mascot):
        self.__nombre = nombre
        self.__phone = phone
        self.__email = email
        self.__list_mascot = list_mascot

    #Metodos Setter and getters
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre #Esto sirve por si desea cambiar el nombre
    def get_phone(self):
        return self.__phone
    def set_phone(self, numero_nuevo):
        self.__phone = numero_nuevo
    def get_email(self):
        return self.__email
    def set_email(self, nuevo_correo):
        self.__email = nuevo_correo
    def get_mascots(self):
        return self.__list_mascot
    def set_mascots(self, nueva_masc):
        self.__list_mascot.append(nueva_masc) #seagrega la nueva


class Mascot:

    def __init__(self, nombre, edad, especie):
        self.__name = nombre
        self.__age = edad
        self.__especie = especie

    def get_name(self):
        return self.__name
    def set_name(self, nuevo):
        self.__name = nuevo

    def get_age(self):
        return self.__age
    def set_age(self, nueva):
        self.__age = nueva

    def get_especie(self):
        return self.__especie



class Dog(Mascot):

    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "PERRO")
        self.__raza = raza


class Cat(Mascot):

    def __init__(self, nombre, edad , color):
        super().__init__(nombre, edad, "GATO")
        self.__color = color



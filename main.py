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


class Veterinaria:
    listaCliente = [] #en esta lista se guardan todos los clientes que posee la veterinaria
    ListaCitas = [] #aqui se guarda las citas de los clientes junto con sus mascotas


class CitaMedica:

    def __init__(self, cliente, mascota):
        self.cliente = cliente
        self.mascota = mascota





def registro_cliente():
    print('Registrando clientes')

def registro_mascot():
    print('Registrando mascota nueva')

def program_date():
    print('Programar Cita')

def history():
    print('Historial de citas')

def view_animals():
    print('Viendo animales')


fin=True

while fin:

    try:
        print('\r\t\t===Bienvenido a la veterinaria===')
        print('1. Registrar nuevo cliente \r\n2.Registrar nueva mascota \r\n3.Agendar Cita médica')
        print('4.Ver historial de citas \r\n5.Ver clientes y mascotas \r\n0.Salir')
        op = int(input())
        match op:
            case 0:
                print('Gracias por usar el sistema')
                fin=False
            case 1:
                registro_cliente()
            case 2:
                registro_mascot()
            case 3:
                program_date()
            case 4:
                history()
            case 5:
                view_animals()
            case _:
                print("Error no existe la opcion ingresada intentelo de nuevo")

    except ValueError:
        print("Entrada no valida por favor vuelve a intentarlo")







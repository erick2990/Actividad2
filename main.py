class Cliente:


    def __init__(self, nombre, phone, email):
        self.__nombre = nombre
        self.__phone = phone
        self.__email = email
        self.lista_mascota = [] #se inicializa una lista para este objeto en el que se guardaran las mascotas


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

    def asociar_Mascot(self, mascota):
        self.lista_mascota.append(mascota) #se añade a la lista que se inicializo



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

    lista_cliente = []
    lista_citas = []

class CitaMedica:

    def __init__(self, cliente, mascota):
        self.cliente = cliente
        self.mascota = mascota


def registrar_cliente():
    fin_Ingreso = True
    print('Registro de cliente')
    while fin_Ingreso:
        try:
            nombre_tmp = input('Ingrese el nombre del cliente: ')
            numero_tmp = int(input('Ingrese su numero de telefono: '))
            correo_tmp = input('Ingrese su correo electronico: ')
            cliente_tmp = Cliente(nombre_tmp, numero_tmp, correo_tmp) #Se envian los parametros y se instancia
            #comprobacion si existe o no
            if cliente_tmp not in dia.lista_cliente:
                dia.lista_cliente.append(cliente_tmp) #se añade el cliente
                print('Cliente añadido con exito')
                fin_Ingreso = False

            else:
                print('ESTA PERSONA YA EXISTE POR FAVOR VERIFIQUE LOS DATOS')

        except ValueError:
            print('ERROR - Ingreso incorrecto intente de nuevo')



def registrar_mascot():
    print('Regisrar mascota')

def agen_date():
    print('Agendar cita')

def history():
    print('Historial de citas')
def vie_custom():
    print('Viendo clientes y sus mascotas')



fin = True
#Se instancia un objeto de tipo veterinaria para poder iniciar una lista de clientes y de citas
dia = Veterinaria() #se inicializa el dia para la veterinaria

while fin:

    try:
        print('\r\t===Clinica Veterinaria===\r\n1.Registrar nuevo cliente \r\n2.Registrar nueva mascota \r\n3.Agendar cita medica')
        print('4.Ver historial de citas \r\n5.Ver clientes y mascotas \r\n0. Salir')
        op = int(input())
        match op:
            case 0:
                print('Gracias por usar el programa')
                fin = False
            case 1:
                registrar_cliente()
            case 2:
                registrar_mascot()
            case 3:
                agen_date()
            case 4:
                history()
            case 5:
                vie_custom()
            case _:
                print('ERROR - Opcion incorrecta vuelva a intentarlo')


    except ValueError:
        print("ERROR ENTRADA INVALIDA POR FAVOR INGRESE NUEVAMENTE SU OPCION")


class Cliente:

    def __init__(self, nombre, phone, email):
        self.__nombre = nombre
        self.__phone = phone
        self.__email = email
        self.mascotas = [] #Esto sirve para instanciar unna lista en el objeto

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
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota) #se añade esta mascota al lisrado de animales


    def mostrar_info(self):
        if len(self.mascotas) >0:
            print(f'Hola soy {self.get_nombre()} y tengo a mi cargo las siguientes mascotas: ')
            for cargo in self.mascotas:
                print(cargo.get_name())
        else:
            print(f'Hola soy {self.get_nombre()} y aun no tengo mascotas a mi cargo')

    def mostrar_mascotas(self):
        numero =1
        for masco in self.mascotas:
            print(f'{numero}. {masco.get_name()}')
            numero+=1
    def mostrar_nombre(self):
        print(f'{self.get_nombre()}')




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

    def presentar_cita(self):
        print(f'Propietario: {self.cliente.get_nombre()} Mascota: {self.mascota.get_name()}')


dia = Veterinaria() #se inicializa el dia para la veterinaria



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

    fin_registro = True
    while fin_registro:
        try:
            nombre_mas = input('Ingrese el nombre de su mascota: ')
            edad_mas = int(input('Ingrese la edad de su mascota: '))
            tipo_Mas = int(input('Que tipo de animal tiene 1. Perro 2. Gato 3. Exotico \r\n'))
            match tipo_Mas:
                case 1:
                    raza_mas = input('Ingrese la raza del perro: ')
                    masc_tmp = Dog(nombre_mas, edad_mas, raza_mas)

                case 2:
                    color_tmp = input('Ingres el color del gato: ')
                    masc_tmp = Cat(nombre_mas, edad_mas, color_tmp)

                case 3:
                    especie = input('Ingrese la especie del animal: ')
                    masc_tmp = Mascot(nombre_mas, edad_mas, especie)

                case _:
                    print("Opcion incorrecta por favor verifique su respuesta")

            if len(dia.lista_cliente)>0:
                cont = 1
                correcto = True

                for tmp in dia.lista_cliente:
                    print(f'{cont} {tmp.get_nombre()}')
                    cont+=1

                while correcto:
                    num_cliente = int(input('Ingrese el numero del cliente para asociarlo a la mascota (0 para cancelar): '))-1
                    if num_cliente >= 0 and num_cliente < len(dia.lista_cliente):
                        seleccionado = dia.lista_cliente[num_cliente]
                        seleccionado.agregar_mascota(masc_tmp)
                        print(f'Cliente {num_cliente+1} asociado con exito... ')
                        correcto = False
                        fin_registro =False

                    elif num_cliente<0:
                        print('Regresando...')
                        correcto =False
                        fin_registro =False

                    else:
                        print(f'Cliene {num_cliente} no existe intente nuevamente...')

            else:
                print('No existen clientes aún registrados por favor vuelva a intentarlo o registra clientes primero')
                fin_registro =False



        except ValueError:
            print('Error valor incorrecto')




def agen_date():
    print('Agendar cita')
    if len(dia.lista_citas)>=0:
        indic =1
        asignar =True

        while asignar:
            try:
                print('Si el nombre de su mascota y dueño no aparece en la lista por favor registrese para agendar cita')
                for tmp in dia.lista_cliente:
                    print(f'{indic} Propietario: {tmp.get_nombre()} Animales: ')
                    tmp.mostrar_mascotas()
                    indic += 1
                propietario = int(input('Ingrese el numero segun el propietario: '))-1
                citado = dia.lista_cliente[propietario]
                print(f'Seleccione que mascota del cliente {citado.get_nombre()} tendra la cita: ')
                citado.mostrar_mascotas()
                numero_mascota = int(input())-1
                if numero_mascota>=0 and numero_mascota<len(citado.mascotas):
                    paciente = citado.mascotas[numero_mascota] #se añade desde la lista del propietario
                    cita_tmp = CitaMedica(citado, paciente)
                    dia.lista_citas.append(cita_tmp) #se añade a la lista de citas para este dia
                    print('La cita se agendo con exito')
                    asignar =False

                else:
                    print('Error usted selecciono un numero de masctoa que no existe')

            except ValueError:
                print('Error valor incorrecto')


    else:
        print('No hay citas registradas aún')



def history():
    print('Historial de citas')
    if len(dia.lista_citas)>0:
        for tmp in dia.lista_citas:
            tmp.presentar_cita()
    else:
        print('Aún no hay citas registradas')


def vie_custom():
    print('Viendo clientes y sus mascotas')
    if len(dia.lista_cliente)>0:
        for tmp in dia.lista_cliente:
            tmp.mostrar_info()

    else:
        print('Aún no hay clientes ni mascotas')





fin = True
#Se instancia un objeto de tipo veterinaria para poder iniciar una lista de clientes y de citas


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


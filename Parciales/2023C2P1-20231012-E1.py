"""
La agencia de viajes Te llevo a donde quieras SRL está pasando por problemas organizativos con sus 
clientes, por lo cual solicitó la ayuda de los estudiantes de Algoritmos y Programación I para crear 
un sistema de gestión que, mediante el uso de la consola y un menú de opciones, permita al personal 
de ventas de la agencia:
    a. Cargar toda la información correspondiente a cada una de las ventas de viajes que
       realicen en las oficinas de atención al público, solicitando al usuario:
           i.   DNI (del comprador)
           ii.  Nombre y apellido (del comprador)
           iii. Destino turístico

                Para la selección del destino turístico, el sistema debe:
                    1. mostrar los paquetes disponibles para ese destino
                    2. permitir al usuario seleccionar un paquete

                Esta información debe guardarse, ya que un mismo destino turístico puede tener
                más de un paquete.
            
           iv.  Cantidad de pasajeros
           v.   Valor a pagar

                valor a pagar = valor del paquete * cantidad de pasajeros

    b. Cargar paquetes turísticos, solicitando al usuario:
           i.   Nombre del paquete
           ii.  Destino
           iii. Cantidad de días
           iv.  Valor

           Ejemplo: Brasil mágico, Brasil, 7, 450000

    c. Ingresar un destino y listar todas las reservas/ventas que se realizaron hasta el momento

    d. Imprimir el nombre del paquete más vendido y los usuarios que lo reservaron

    e. Imprimir la información del pasajero que más reservas realizó

    f. Listar todas las ventas cuyos montos totales sean mayores al promedio, la información a listar 
       debe incluir el número de dni del comprador
"""
###############################################################
########## INICIO LÓGICA REUTILIZADA DE OTROS MENUES ##########
###############################################################

def solicitar_ingreso(mensaje: str) -> str:
    entrada: str = input(f'\n{mensaje}: ')

    return entrada


def es_numero_entero(entrada: str) -> bool:
    es_numero_valido: bool = False

    if entrada.isnumeric():
        es_numero_valido = True
    else:
        print('\n¡Sólo se pueden ingresar numeros enteros!')

    return es_numero_valido


def se_encuentra_entre_valores(numero: int, numero_minimo: int, numero_maximo: str) -> bool:
    esta_dentro_del_rango: bool = False

    if numero >= numero_minimo and numero <= numero_maximo:
        esta_dentro_del_rango = True

    else:
        print(f'\n¡El número entero ingresado debe estar entre {numero_minimo} y {numero_maximo}!')

    return esta_dentro_del_rango


def son_solo_espacios(entrada: str) -> bool:
    son_espacios: bool = True

    if entrada.isspace():
        print('\n¡No se pueden ingresar solamente espacios!')
    else:
        son_espacios = False

    return son_espacios


def es_numero_entero_valido(entrada: str) -> bool:
    es_numero_valido: bool = False

    if entrada[0] == '-':
        es_numero_valido = es_numero_entero(entrada[1::])

    else:
        es_numero_valido = es_numero_entero(entrada)      

    return es_numero_valido


def validar_numero_entero(entrada: str, numero_minimo: int, numero_maximo: int, mensaje: str) -> int:
    numero: int = int()
    es_numero_valido: bool = False

    while not es_numero_valido:

        if (not son_solo_espacios(entrada) and es_numero_entero_valido(entrada) and 
                se_encuentra_entre_valores(int(entrada), numero_minimo, numero_maximo)):
            
            numero = int(entrada)
            es_numero_valido = True

        else:
            entrada = solicitar_ingreso(mensaje)

    return numero


def ingresar_opcion_de_usuario(mensaje_de_menu: str, opciones: list) -> int:
    print(f'\n######## {mensaje_de_menu} ########\n')
    print('Opciones válidas: \n')

    for x in range(len(opciones)):
        print(x + 1, '-', opciones[x])

    mensaje: str = 'Ingrese una opción'
    entrada: str = solicitar_ingreso(mensaje)
    opcion: int = validar_numero_entero(entrada, 1, len(opciones), mensaje)

    return opcion

##############################################################
########### FIN LÓGICA REUTILIZADA DE OTROS MENUES ###########
##############################################################

def cargar_venta(ventas: dict, paquetes_turisticos: dict) -> None:
    destinos: str = ', '.join(list(paquetes_turisticos.keys()))

    dni: str = input('Ingrese el dni del comprador: ')
    nombre: str = input('Ingrese el nombre del comprador: ').title()
    apellido: str = input('Ingrese el apellido del comprador: ').title()

    print(f'\nLos destinos disponibles son: {destinos}')
    
    destino: str = input('Ingrese el destino: ')

    while destino not in paquetes_turisticos:
        print(f'\nLos destinos disponibles son: {destinos}')

        destino = input('Ingrese un destino válido, por favor: ').title()

    nombres_de_paquetes: list = list()

    for paquete_turistico in paquetes_turisticos[destino]:
        nombres_de_paquetes.append(paquete_turistico['nombre_del_paquete'])

    print('Los paquetes disponibles son: ')

    for paquete_turistico in paquetes_turisticos:
        print(paquete_turistico)

    nombre_del_paquete: str = input('Ingrese el nombre del paquete: ').title()

    while nombre_del_paquete not in paquetes_turisticos:
        print('Los paquetes disponibles son: ')

        for paquete_turistico in paquetes_turisticos:
            print(paquete_turistico)

        nombre_del_paquete: str = input('Ingrese el nombre de un paquete válido, por favor: ').title()


    cantidad_de_pasajeros: int = int(input('Ingrese la cantidad de pasajeros: '))
    valor_a_pagar: float = paquetes_turisticos[destino]['valor'] * cantidad_de_pasajeros

    if dni in ventas:
        ventas[dni]['informacion_de_ventas'].append(
            {
                'destino_turistico': {
                    'destino': destino,
                    'nombre_del_paquete': nombre_del_paquete
                },
                'cantidad_de_pasajeros': cantidad_de_pasajeros,
                'valor_a_pagar': valor_a_pagar
            }
        )
        
    else:
        ventas[dni]['informacion_de_ventas'] = [
            {
                'destino_turistico': {
                    'destino': destino,
                    'nombre_del_paquete': nombre_del_paquete
                },
                'cantidad_de_pasajeros': cantidad_de_pasajeros,
                'valor_a_pagar': valor_a_pagar
            }
        ]


def cargar_paquete_turistico(paquetes_turisticos: dict) -> None:
    nombre_del_paquete: str = input('Ingrese el nombre del paquete: ').title()
    destino: str = input('Ingrese el destino: ').title()
    cantidad_de_dias: int = int(input('Ingrese la cantidad de dias: '))
    valor: float = float(input('Ingrese el valor del paquete: '))

    if destino not in paquetes_turisticos:
        paquetes_turisticos[destino] = list()

    else:
        paquetes_turisticos[destino].append(
            {
                'nombre_del_paquete': nombre_del_paquete,
                'cantidad_de_dias': cantidad_de_dias,
                'valor': valor
            }
        )


def listar_ventas_por_destino(ventas: dict) -> None:
    destinos: list = list()
    destino: str = input('\nIngrese un destino para filtrar: ').title()

    for dni in ventas:
        cliente: dict = ventas[dni]

        for venta in cliente['informacion_de_ventas']:
            destino_turistico: dict = venta['destino_turistico']

            if destino_turistico['destino'] not in destinos:
                destinos.append(destino_turistico['destino'])


    if destino not in destinos:
        print('\n¡Se ingreso un destino para el cual no se realizó la venta de ningún paquete turístico!\n')
    
    else:
        for dni in ventas:
            cliente: dict = ventas[dni]

            for venta in cliente['informacion_de_ventas']:
                destino_turistico: dict = venta['destino_turistico']

                if destino_turistico['destino'] == destino:
                    print('Destino: {0}, Paquete turístico: {1}, DNI: {2}'
                        .format(
                            destino_turistico['destino'],
                            destino_turistico['nombre_del_paquete'],
                            dni
                        )
                    )


def mostrar_paquete_mas_vendido(ventas: dict) -> None:
    usuarios_por_paquete: dict = dict()

    for dni in ventas:
        cliente: dict = ventas[dni]

        for venta in cliente['informacion_de_ventas']:
            destino_turistico: dict = venta['destino_turistico']

            if destino_turistico['nombre_del_paquete'] not in usuarios_por_paquete:
                usuarios_por_paquete[destino_turistico['nombre_del_paquete']] = {
                    'cantidad_de_ventas': 1,
                    'usuarios': [dni]
                }
            else:
                usuarios_por_paquete[destino_turistico['nombre_del_paquete']]['cantidad_de_ventas'] += 1
                usuarios_por_paquete[destino_turistico['nombre_del_paquete']]['usuarios'].append(dni)

    if ventas:
        flag_primer_paquete: bool = False
        cantidad_de_ventas_maxima: int = 0
        nombre_de_paquete_con_mas_reservas: str = str()
        usuarios_de_paquete_con_mas_reservas: list = list()

        for nombre_del_paquete in usuarios_por_paquete:
            paquete: dict = usuarios_por_paquete[nombre_del_paquete]

            if not flag_primer_paquete:
                cantidad_de_ventas_maxima = paquete['cantidad_de_ventas']
                nombre_de_paquete_con_mas_reservas = nombre_del_paquete
                usuarios_de_paquete_con_mas_reservas = paquete['usuarios']
                flag_primer_paquete = True

            elif paquete['cantidad_de_ventas'] > cantidad_de_ventas_maxima:
                cantidad_de_ventas_maxima = paquete['cantidad_de_ventas']
                nombre_de_paquete_con_mas_reservas = nombre_del_paquete
                usuarios_de_paquete_con_mas_reservas = paquete['usuarios']

        print('El paquete más vendido fue "{0}", y los usuarios con DNI {1} lo reservaron'
            .format(
                nombre_de_paquete_con_mas_reservas,
                ", ".join(usuarios_de_paquete_con_mas_reservas)
            )
        )

    else:
        print('\n¡Aún no se han cargado ventas!\n')


def mostrar_pasajero_con_mas_reservas(ventas: dict) -> None:
    flag_primer_pasajero: bool = False
    cantidad_de_reservas_maxima: int = 0
    dni_con_mas_reservas: str = str()
    pasajero_con_mas_reservas: dict = dict()

    for dni in ventas:
        cliente: dict = ventas[dni]

        if not flag_primer_pasajero:
            cantidad_de_reservas_maxima = len(cliente['informacion_de_ventas'])
            dni_con_mas_reservas = dni
            pasajero_con_mas_reservas = cliente
            flag_primer_pasajero = True

        elif len(cliente['informacion_de_ventas']) > cantidad_de_reservas_maxima:
            cantidad_de_reservas_maxima = len(cliente['informacion_de_ventas'])
            dni_con_mas_reservas = dni
            pasajero_con_mas_reservas = cliente

    # Si el diccionario no está vacío
    if ventas:
        print('\nEl pasajero {0} {1} con DNI {2}, es quien realizó más reservas, con una cantidad de {3} reservas\n'
            .format(
                pasajero_con_mas_reservas['nombre'],
                pasajero_con_mas_reservas['apellido'],
                dni_con_mas_reservas,
                len(pasajero_con_mas_reservas['informacion_de_ventas'])
            )
        )

    else:
        print('\n¡Aún no se han cargado ventas!\n')


def listar_ventas_mayores_al_promedio(ventas: dict) -> None:
    venta_acumulada: float = 0.0
    cantidad_de_ventas: int = 0
    promedio_de_ventas: float = 0.0

    for dni in ventas:
        cliente: dict = ventas[dni]

        for venta in cliente['informacion_de_ventas']:
            venta_acumulada += venta['valor_a_pagar']
            cantidad_de_ventas += 1

    if (cantidad_de_ventas != 0):
        promedio_de_ventas = round(venta_acumulada / cantidad_de_ventas, 2)

    else:
        print('\n¡Aún no se han cargado ventas!\n')

    for dni in ventas:
        cliente: dict = ventas[dni]

        for venta in cliente['informacion_de_ventas']:
            if venta['valor_a_pagar'] > promedio_de_ventas:
                destino_turistico: dict = venta['destino_turistico']

                print('La venta del cliente con DNI {0}, con destino a {1} del paquete "{2}", supera el promedio de ventas de ${3}'
                    .format(    
                        dni,
                        destino_turistico['destino'],
                        destino_turistico['nombre_del_paquete'],
                        promedio_de_ventas
                    )
                )


def main() -> None:
    opciones: list = [
        'Cargar información correspondiente de venta de viaje',
        'Cargar paquete turístico',
        'Listar reservas/ventas por destino',
        'Mostrar paquete más vendido y usuarios que lo reservaron',
        'Mostrar pasajero que más reservas realizó',
        'Listar ventas mayores al promedio',
        'Salir'
    ]

    ventas: list = {
        '39219469': {
            'nombre': 'Leonel',
            'apellido': 'Chaves',
            'informacion_de_ventas': [
                {
                    'destino_turistico': {
                        'destino': 'Argentina',
                        'nombre_del_paquete': 'Bariloche te sorprende'
                    },
                    'cantidad_de_pasajeros': 1,
                    'valor_a_pagar': 485000.00
                },
                {
                    'destino_turistico': {
                        'destino': 'Brasil',
                        'nombre_del_paquete': 'Brasil mágico'
                    },
                    'cantidad_de_pasajeros': 2,
                    'valor_a_pagar': 900000.00
                },
                {
                    'destino_turistico': {
                        'destino': 'Argentina',
                        'nombre_del_paquete': 'Salta más linda que nunca'
                    },
                    'cantidad_de_pasajeros': 4,
                    'valor_a_pagar': 840000.00
                }
            ]
        },
        '41251451': {
            'nombre': 'Tomas',
            'apellido': 'Villegas',
            'informacion_de_ventas': [
                {
                    'destino_turistico': {
                        'destino': 'Chile',
                        'nombre_del_paquete': 'Chi Chi Chi Chi le'
                    },
                    'cantidad_de_pasajeros': 1,
                    'valor_a_pagar': 1210000.00
                }
            ]
        },
        '39451215': {
            'nombre': 'Martin',
            'apellido': 'Sosa',
            'informacion_de_ventas': [
                {
                    'destino_turistico': {
                        'destino': 'Brasil',
                        'nombre_del_paquete': 'Copacabana a full'
                    },
                    'cantidad_de_pasajeros': 1,
                    'valor_a_pagar': 825000.00
                },
                {
                    'destino_turistico': {
                        'destino': 'Argentina',
                        'nombre_del_paquete': 'Salta más linda que nunca'
                    },
                    'cantidad_de_pasajeros': 2,
                    'valor_a_pagar': 420000.00
                }
            ]
        }
    }

    paquetes_turisticos: dict = {
        'Brasil': [
            {
                'nombre_del_paquete': 'Brasil mágico',
                'cantidad_de_dias': 7,
                'valor': 450000.00
            },
            {
                'nombre_del_paquete': 'Copacabana a full',
                'cantidad_de_dias': 14,
                'valor': 825000.00
            }
        ],
        'Argentina': [
            {
                'nombre_del_paquete': 'Salta más linda que nunca',
                'cantidad_de_dias': 5,
                'valor': 210000.00
            },
            {
                'nombre_del_paquete': 'Bariloche te sorprende',
                'cantidad_de_dias': 10,
                'valor': 485000.00
            }
        ],
        'Chile': [
            {
                'nombre_del_paquete': 'Chi Chi Chi Chi le',
                'cantidad_de_dias': 6,
                'valor': 1210000.00
            }
        ]
    }

    opcion: int = ingresar_opcion_de_usuario('MENU PRINCIPAL', opciones)

    while opcion != len(opciones):    
        if opcion == 1:
            cargar_venta(ventas, paquetes_turisticos)

        elif opcion == 2:
            cargar_paquete_turistico(paquetes_turisticos)

        elif opcion == 3:
            listar_ventas_por_destino(ventas)

        elif opcion == 4:
            mostrar_paquete_mas_vendido(ventas)

        elif opcion == 5:
            mostrar_pasajero_con_mas_reservas(ventas)

        elif opcion == 6:
            listar_ventas_mayores_al_promedio(ventas)

        opcion = ingresar_opcion_de_usuario('MENU PRINCIPAL', opciones)

    print('\n¡Finalizó el programa!')


main()
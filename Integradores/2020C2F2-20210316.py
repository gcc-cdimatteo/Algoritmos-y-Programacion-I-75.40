'''
La cámara de comercio digital nos encarga un análisis de las plataformas de streaming y el uso que le dan los usuarios en la Argentina.
La información que nos bridan se encuentra en dos archivos. El primero conteniendo información general de cada plataforma y el segundo con el detalle de usuarios y atributos asociados a cada uno de ellos.

plataformas.csv

Plataforma, costo mensual, años de actividad
Ej de líneas de este archivo:
Netflix, 400, 8
Spotify, 275, 6

usuarios.csv

Nombre, Plataforma, Puntuación, Meses suscrito, TipoDispositivo1, Horas1, Tipo Dispositivo2, Horas2, … , TipoDispositivo N, horas N
Ej de líneas de este archivo:
guidocosta, Netflix, 9, 18, Mobile, 73, PC, 42, TV, 179
tomasvillegas, Spotify, 8.5, 12, Mobile, 123, PC, 49

El programa deberá tener un menú poder cumplir lo siguiente:
1. Procesar información de entrada
2. Determinar la plataforma que mayores ingresos generó en toda la historia
3. Determinar el usuario que mayor cantidad de plataformas puntuó y cuanto dinero lleva gastado en plataformas.
4. Ranking de plataformas por puntuación promedio
5. Determinar la plataforma mas utilizada, y luego indicar como es la distribución porcentual sobre los dispositivos que se utiliza ordenada del mas utilizado al menos utilizado
Aclaración: Recuerde que es un programa, con lo cual deberá tener funciones y programa principal.
'''

import re
import copy


OPCIONES = [
    "Procesar información de entrada",
    "Determinar plataforma con mayor ingreso",
    "Determinar usuario, que mayor cantidad de plataformas puntuó y dinero gastado",
    "Ranking de plataformas por puntuación promedio",
    "Determinar plataforma más utilizada, y distribución porcentual sobre los dispositivos",
    "Salir"
]

PLATAFORMA_ENCABEZADOS = ["Plataforma", "Costo mensual", "Años de actividad"]

USUARIO_ENCABEZADOS = ["Nombre", "Plataforma", "Puntuación", "Meses suscrito", "Dispositivos"]

DISPOSITIVO_ENCABEZADOS = ["Dispositivo", "Horas"]

# PLATAFORMAS = [
#     "Amazon Prime Video", "HBO", "Netflix", 
#     "Apple TV", "Flow", "Disney+", "Spotify"
# ]

DISPOSITIVOS = ["Mobile", "TV", "PC"]


def validar_numero(numero  # type: str
                   ):

    # PRE: 'numero', debe ser una variable de tipo str
    # POST: Devuelve un int o float, que representa al número pasado por 
    #       parámetro, al cual se le ha eliminado los caracteres alfabeticos

    numero_formateado = ""
    valor = 0

    numero_formateado = re.sub("[a-zA-Z]+", "", numero)

    try:
        valor = int(numero_formateado)

    except ValueError:
        valor = float(numero_formateado)

    return valor


def validar_opcion(opcion,  # type: str
                   opciones  # type: list[str]
                   ):

    # PRE: 'opcion', debe ser una variable de tipo str
    #      'opciones', debe ser una variable de tipo list
    # POST: Devuelve un boolean, que representa a si la opcion pasada 
    #       por parámetro, es un número y si se encuentra dentro del 
    #       rango de las posibles opciones a elegir

    option_number = 0
    flag_valid_option = False

    if opcion.isnumeric():
        option_number = int(opcion)

        if option_number > 0 and option_number <= len(opciones):
            flag_valid_option = True

        else:
            print(f"\n¡Sólo puedes ingresar una opción entre el 1 y el {len(opciones)}!")

    else:
        print(f"\n¡Las opciones son numeros enteros, sin decimales!")

    return flag_valid_option


def validar_opcion_ingresada():

    # POST: Devuelve un int, que representa a la entrada hecha por el  
    #       usuario, de una opcion, a la cual se la valida  

    opcion_ingresada = ""
    numero = 0
    flag_opcion_valida = False

    opcion_ingresada = input("\nIngrese una opción: ")

    while not flag_opcion_valida:
        try:
            numero = validar_numero(opcion_ingresada)

            flag_opcion_valida = validar_opcion(opcion_ingresada, OPCIONES) 

        except ValueError:
            print("\n¡Sólo se pueden ingresar numeros!")

    return numero


def obtener_entrada_usuario(opciones  # type: list[str]
                            ):

    # PRE: 'opciones', debe ser una variable de tipo list
    # POST: Devuelve un int, que representa a la entrada hecha por el  
    #       usuario, de una opcion, a la cual se la valida

    opcion = 0

    print("\nOpciones válidas: \n")

    for x in range(len(opciones)):
        print(x + 1, "-", opciones[x])

    opcion = validar_opcion_ingresada()

    return opcion


def leer_archivo(ruta_archivo  # type: str
              ):

    # PRE: 'ruta_archivo', debe ser una variable de tipo str
    # POST: Devuelve una lista, que representa a las lineas leidas del archivo  
    #       que fue abierto y leido posteriormente

    data = []

    try:
        f = open(ruta_archivo, "r", encoding="utf-8")
    except IOError:
        print("\nNo se pudo leer el archivo: ", ruta_archivo)
    
    with f:
        data = f.read().splitlines()

    return data


def parsear_data_a_plataforma(data  # type: str
                              ):
    
    # PRE: 'data', debe ser una variable de tipo str
    # POST: Devuelve un dict, que representa a la información pasada por 
    #       parámetro y que ha sido parseada al modelo 'plataforma'

    # plataforma = { 
    #   'Plataforma': str, 
    #   'Costo mensual': int,
    #   'Años de actividad': int
    # }

    data_formateada = []
    plataforma = {}

    data_formateada = re.split("\,\s*|\,", data)

    for x in range(len(PLATAFORMA_ENCABEZADOS)):

        if (PLATAFORMA_ENCABEZADOS[x] == "Costo mensual" or PLATAFORMA_ENCABEZADOS[x] == "Años de actividad"):
            plataforma[PLATAFORMA_ENCABEZADOS[x]] = validar_numero(data_formateada[x])

        else:
            plataforma[PLATAFORMA_ENCABEZADOS[x]] = data_formateada[x]        

    return plataforma


def parsear_data_a_dispositivos(data  # type: list[str]
                                ):

    # PRE: 'data', debe ser una variable de tipo list
    # POST: Devuelve una lista de dicts, que representa a la información 
    #       pasada por parámetro y que ha sido parseada al modelo 'dispositivo'

    # dispositivo = { 'Dispositivo': str, 'Horas': int }

    dispositivos = []
    cant_dispos = 0

    cant_dispos = len(data) // 2

    for x in range(cant_dispos):
        dispositivo = {}

        dispositivo[DISPOSITIVO_ENCABEZADOS[0]] = data[x * 2]
        dispositivo[DISPOSITIVO_ENCABEZADOS[1]] = validar_numero(data[x * 2 + 1])

        dispositivos.append(dispositivo)

    return dispositivos


def parsear_data_a_usuario(data  # type: str
                           ):
    
    # PRE: 'data', debe ser una variable de tipo str
    # POST: Devuelve un dict, que representa a la información pasada por 
    #       por parámetro y que ha sido parseada al modelo 'usuario'

    # usuario = { 
    #   'Nombre': str, 
    #   'Plataforma': str,
    #   'Puntuación': int | float,
    #   'Meses suscrito': int,
    #   'Dispositivos': list[dispositivo]
    # }

    data_formateada = []
    usuario = {}

    data_formateada = re.split("\,\s*|\,", data)

    for x in range(len(USUARIO_ENCABEZADOS)):

        if(USUARIO_ENCABEZADOS[x] == "Puntuación" or USUARIO_ENCABEZADOS[x] == "Meses suscrito"):
            usuario[USUARIO_ENCABEZADOS[x]] = validar_numero(data_formateada[x])

        elif x == 4:
            #data_formateada.pop(x - 1)

            usuario[USUARIO_ENCABEZADOS[x]] = parsear_data_a_dispositivos(data_formateada[x:len(data_formateada) + 1])

        else:
            usuario[USUARIO_ENCABEZADOS[x]] = data_formateada[x] 

    return usuario


def procesar_informacion():

    # POST: Devuelve dos listas de dicts, que representa a la 
    #       información procesada de los archivos 'plataformas.csv' y  
    #       'usuarios.csv'

    plataformas_data = []
    usuarios_data = []
    plataformas = []
    usuarios = []

    plataformas_data = leer_archivo("plataformas.csv")
    usuarios_data = leer_archivo("usuarios.csv")

    for x in range(len(plataformas_data)):

        plataformas.append(
            parsear_data_a_plataforma(plataformas_data[x])
        )

    for x in range(len(usuarios_data)):

        usuarios.append(
            parsear_data_a_usuario(usuarios_data[x])
        )

    return plataformas, usuarios


def filtrar_valores_unicos(data,  # type: list[dict]
                           llave  # type: str
                           ):
    
    # PRE: 'data', debe ser una variable de tipo list
    #      'llave', debe ser una variable de tipo str
    # POST: Devuelve una lista de str, que representa a la información 
    #       pasada por parámetro y que ha sido filtrada de modo que 
    #       queden únicamente los 'values' de dicha 'llave'

    data_filtrada = []

    data_filtrada = list({v[llave]:v for v in data})

    return data_filtrada


def imprimir_plataforma_mayor_ingreso(plataformas,  # type: list[dict]
                                      usuarios  # type: list[dict]
                                      ):

    copia_plataformas = []
    plataforma_mayor_ingreso = {}

    copia_plataformas = copy.deepcopy(plataformas)

    for plataforma in copia_plataformas:
        total_ingreso = 0

        for usuario in usuarios:

            if(plataforma.get("Plataforma") == usuario.get("Plataforma")):
                total_ingreso += plataforma.get("Costo mensual") * usuario.get("Meses suscrito")

        plataforma["Total ingreso"] = total_ingreso

    plataforma_mayor_ingreso = max(copia_plataformas, key=lambda x:x["Total ingreso"])

    print("\nLa plataforma '{0}', es la que más ha recaudado, por un monto de ${1} "
        .format(
            plataforma_mayor_ingreso.get("Plataforma"),
            plataforma_mayor_ingreso.get("Total ingreso")
        )
    )


def imprimir_usuario_mas_plataformas(plataformas,  # type: list[dict]
                                     usuarios  # type: list[dict]
                                     ):

    usuarios_resumen = []
    usuario_mayor_plataformas = {}

    lista_usuarios = filtrar_valores_unicos(usuarios, "Nombre")

    usuarios_resumen = [{"Nombre": lista_usuarios[x]} for x in range(len(lista_usuarios))]

    for usuario_resumen in usuarios_resumen:
        cant_plataformas = 0
        tot_dinero_gastado = 0

        for usuario in usuarios:

            if(usuario_resumen.get("Nombre") == usuario.get("Nombre")):
                for plataforma in plataformas:

                    if(usuario.get("Plataforma") == plataforma.get("Plataforma")):
                        cant_plataformas += 1
                        tot_dinero_gastado += plataforma.get("Costo mensual") * usuario.get("Meses suscrito")

        usuario_resumen["Cantidad de plataformas"] = cant_plataformas
        usuario_resumen["Total dinero gastado"] = tot_dinero_gastado

    usuario_mayor_plataformas = max(usuarios_resumen, key=lambda x:x["Cantidad de plataformas"])

    print("\nEl usuario '{0}', es quien mayor cantidad de plataformas puntuó, y ha gastado un total de ${1}"
        .format(
            usuario_mayor_plataformas.get("Nombre"),
            usuario_mayor_plataformas.get("Total dinero gastado")
        )
    )


def imprimir_puntuacion_promedio(plataformas,  # type: list[dict]
                                 usuarios  # type: list[dict]
                                 ):

    plataformas_resumen = []
    plataformas_ordenadas = []

    lista_plataformas = filtrar_valores_unicos(plataformas, "Plataforma")

    plataformas_resumen = [{"Plataforma": lista_plataformas[x]} for x in range(len(lista_plataformas))]

    for plataforma_resumen in plataformas_resumen:
        cant_usuarios = 0
        puntuacion_total = 0

        for usuario in usuarios:

            if(plataforma_resumen.get("Plataforma") == usuario.get("Plataforma")):
                cant_usuarios += 1
                puntuacion_total += usuario.get("Puntuación")

        plataforma_resumen["Cantidad de usuarios"] = cant_usuarios
        plataforma_resumen["Puntuación total"] = puntuacion_total
        plataforma_resumen["Puntuación promedio"] = round(puntuacion_total / cant_usuarios)

    plataformas_ordenadas = sorted(plataformas_resumen, key=lambda k: k["Puntuación promedio"])
    plataformas_ordenadas.reverse()

    for plataforma_ordenada in plataformas_ordenadas:
        print("\nLa plataforma '{0}', tiene una puntuación promedio de {1}"
            .format(
                plataforma_ordenada.get("Plataforma"),
                plataforma_ordenada.get("Puntuación promedio")
            )
        )


def imprimir_plataforma_mas_utilizada(plataformas,  # type: list[dict]
                                      usuarios  # type: list[dict]
                                      ):

    plataformas_resumen = []
    plataforma_mas_utilizada = []
    dispositivo_horas_ordenadas = []

    lista_plataformas = filtrar_valores_unicos(plataformas, "Plataforma")

    plataformas_resumen = [{"Plataforma": lista_plataformas[x]} for x in range(len(lista_plataformas))]

    for plataforma_resumen in plataformas_resumen:
        cant_usuarios = 0
        cant_horas_mobile = 0
        cant_horas_tv = 0
        cant_horas_pc = 0

        for usuario in usuarios:

            if plataforma_resumen.get("Plataforma") == usuario.get("Plataforma"):
                cant_usuarios += 1

                for dispositivo in usuario.get("Dispositivos"):

                    if dispositivo.get("Dispositivo") == "Mobile":
                        cant_horas_mobile += dispositivo.get("Horas")

                    elif dispositivo.get("Dispositivo") == "TV":
                        cant_horas_tv += dispositivo.get("Horas")

                    elif dispositivo.get("Dispositivo") == "PC":
                        cant_horas_pc += dispositivo.get("Horas")                        

        plataforma_resumen["Cantidad de usuarios"] = cant_usuarios
        plataforma_resumen["Total dispositivos horas"] = [
            {"Dispositivo": "Mobile", "Horas": cant_horas_mobile},
            {"Dispositivo": "TV", "Horas": cant_horas_tv},
            {"Dispositivo": "PC", "Horas": cant_horas_pc}
        ]
        plataforma_resumen["Total horas"] = cant_horas_mobile + cant_horas_tv + cant_horas_pc

    plataforma_mas_utilizada = max(plataformas_resumen, key=lambda x:x["Cantidad de usuarios"])

    dispositivo_horas_ordenadas = sorted(
        plataforma_mas_utilizada.get("Total dispositivos horas"), 
        key=lambda k: k["Horas"]
    )

    dispositivo_horas_ordenadas.reverse()

    print(f"\n{plataforma_mas_utilizada.get('Plataforma')} es la plataforma más utilizada")

    for dispositivo_horas in dispositivo_horas_ordenadas:
        print("\nDipositivo '{0}', distribución porcentual = {1}%"
            .format(
                dispositivo_horas.get("Dispositivo"),
                round(
                    dispositivo_horas.get("Horas") * 100 / plataforma_mas_utilizada.get("Total horas"),
                    2
                )
            )
        )


def main():
    plataformas = []
    usuarios = []

    opcion = 0
    flag_es_valido = False

    opcion = obtener_entrada_usuario(OPCIONES)

    while opcion != 6:

        if opcion == 1:
            plataformas, usuarios = procesar_informacion()

            print("\n¡Archivos procesados!")

            flag_es_valido = True

        elif(opcion == 2 and flag_es_valido):
            imprimir_plataforma_mayor_ingreso(plataformas, usuarios)

        elif(opcion == 3 and flag_es_valido):
            imprimir_usuario_mas_plataformas(plataformas, usuarios)

        elif(opcion == 4 and flag_es_valido):
            imprimir_puntuacion_promedio(plataformas, usuarios)

        elif(opcion == 5 and flag_es_valido):
            imprimir_plataforma_mas_utilizada(plataformas, usuarios)

        else:
            print("\n¡Debes procesar información primero, antes de elegir esa opción!")

        opcion = obtener_entrada_usuario(OPCIONES)

    print("\nPrograma finalizado")


if __name__ == "__main__":
    main()
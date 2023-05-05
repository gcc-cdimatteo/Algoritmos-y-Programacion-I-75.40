def valor_invalido(valor, valores_validos) -> bool:
    return valor not in valores_validos

def numero_invalido(numero: str) -> bool:
    return numero.isnumeric()

## Podria usarse para refactorizar imprimir_porcentaje_tipo_vehiculo y imprimir_porcentaje_tipo_asistencias
def porcentaje_tipo(asistencias: dict, pos: int) -> dict:
    tipos_totales = {}
    
    for asistencia in asistencias:
        tipo = asistencias[asistencia][pos]
        if tipo not in tipos_totales: 
            tipos_totales[tipo] = 1
        else:
            tipos_totales[tipo] += 1
    
    return tipos_totales

def imprimir_porcentaje_tipo_vehiculo(asistencias: dict) -> None:
    tipo_vehiculos_totales = {}
    
    for asistencia in asistencias:
        tipo_vehiculo = asistencias[asistencia][2]
        if tipo_vehiculo not in tipo_vehiculos_totales: 
            tipo_vehiculos_totales[tipo_vehiculo] = 1
        else:
            tipo_vehiculos_totales[tipo_vehiculo] += 1
    
    for tipo_vehiculo in tipo_vehiculos_totales:
        print(f"El porcentaje de los vehiculos asistidos del tipo {tipo_vehiculo} es {100*tipo_vehiculo/len(asistencias)}%")

def imprimir_porcentaje_tipo_asistencias(asistencias: dict) -> None:
    tipo_asistencias_totales = {}
    
    for asistencia in asistencias:
        tipo_asistencia = asistencias[asistencia][5]
        if tipo_asistencia not in tipo_asistencias_totales: 
            tipo_asistencias_totales[tipo_asistencia] = 1
        else:
            tipo_asistencias_totales[tipo_asistencia] += 1
    
    for tipo_asistencia in tipo_asistencias_totales:
        print(f"El porcentaje de asistencias del tipo {tipo_asistencia} es {100*tipo_asistencia/len(asistencias)}%")

def imprimir_movil_mas_solicitado(asistencias: dict) -> None:
    solicitudes = {}
    
    for asistencia in asistencias:
        numero_movil = asistencias[asistencia][8]
        if numero_movil not in solicitudes:
            solicitudes[numero_movil] = 1
        else:
            solicitudes[numero_movil] += 1
    
    max_solicitud = -1
    
    for solicitud in solicitudes:
        if solicitudes[solicitud] > max_solicitud: max_solicitud = solicitudes[solicitud]
    
    for solicitud in solicitudes:
        if solicitudes[solicitud] == max_solicitud: print(f"El movil {solicitud} presto {solicitudes[solicitud]} servicios")

def imprimir_promedio_tiempo_estimado(asistencias: dict) -> None:
    total = 0
    for asistencia in asistencias:
        total += asistencias[asistencia][6]
    
    print(f"El promedio del tiempo estimado de los servicios es {total/len(asistencias)}")

def imprimir_total_servicios_movil(asistencias: dict, moviles: dict) -> None:
    numero_movil = input("Ingrese el numero de movil para el cual se imprimira el total facturado: ")
    while numero_invalido(numero_movil) or valor_invalido(int(numero_movil), list(moviles.keys())):
        numero_movil = input(f"El numero de movil {numero_movil} es invalido. Por favor, ingrese un numero de movil valido: ")
    numero_movil = int(numero_movil)

    dia = input("Ingrese el dia para el cual se imprimira el total facturado del movil {numero_movil}: ")
    while numero_invalido(dia):
        dia = input(f"El dia {dia} es invalido. Por favor, ingrese un dia valido: ")
    dia = int(dia)
    
    mes = input("Ingrese el mes para el cual se imprimira el total facturado del movil {numero_movil}: ")
    while numero_invalido(mes):
        mes = input(f"El mes {mes} es invalido. Por favor, ingrese un mes valido: ")
    mes = int(mes)
    
    anio = input("Ingrese el anio para el cual se imprimira el total facturado del movil {numero_movil}: ")
    while numero_invalido(anio):
        anio = input(f"El anio {anio} es invalido. Por favor, ingrese un anio valido: ")
    anio = int(anio)
    
    fecha = (dia, mes, anio)

    total = 0
    
    for asistencia in asistencias:
        if asistencias[asistencia][0] != fecha or asistencias[asistencia][8] != numero_movil or asistencias[asistencia][9] == 'en curso': continue
        print(asistencias[asistencia])
        total += asistencias[asistencia][10]
    
    print(f"El total de lo facturado para el movil {numero_movil} en la fecha {fecha} es: {total}")

def agregar_movil(moviles: dict) -> None:
    numero_movil = input("Ingrese el numero de movil que desea ingresar al sistema: ")
    while numero_invalido(numero_movil) or not valor_invalido(int(numero_movil), list(moviles.keys())):
        numero_movil = input(f"El numero de movil {numero_movil} es invalido. Por favor, ingrese un numero de movil valido: ")
    numero_movil = int(numero_movil)

    tipo_asistencia_valida = ['mecanica', 'remolque']
    tipo_asistencia = input("Ingrese el tipo de asistencia que realizara el movil: ")
    while valor_invalido(tipo_asistencia, tipo_asistencia_valida):
        print(f"El tipo de asistencia {tipo_asistencia} es invalida. Los tipos validos son: {tipo_asistencia_valida}")
        tipo_asistencia = input("Por favor, ingrese un tipo de asistencia valida: ")
    
    moviles[numero_movil] = tipo_asistencia

def actualizar_estado(asistencias: dict, numero_dominio: int, estado: str) -> None:
    for asistencia in asistencias:
        if numero_dominio != asistencias[asistencia][1]: continue
        asistencias[asistencia][9] = estado

def numero_dominio_invalido(asistencias: dict, numero_dominio: int) -> bool:
    for asistencia in asistencias:
        if numero_dominio == asistencias[asistencia][1]: return False
    return True

def cerrar_asistencia(asistencias: dict) -> None:
    # {id_asistencia: [fecha, numero_dominio, tipo_vehiculo, direccion_origen, direccion_destino, tipo_asistencia, tiempo_estimado, prioridad, numero_movil, estado, cobro]}
    numero_dominio = input("Ingrese el numero de dominio para el cual quiere finalizar/cancelar un servicio: ")
    while numero_invalido(numero_dominio) or numero_dominio_invalido(asistencias, int(numero_dominio)):
        numero_dominio = input(f"El numero de dominio {numero_dominio} es invalido. Por favor, ingrese un numero de dominio valido: ")
    numero_dominio = int(numero_dominio)

    estado_valido = ['finalizado', 'cancelado']
    estado = input(f"Ingrese el estado que quiere ingresar para el dominio {numero_dominio} ({estado_valido}): ")
    while valor_invalido(estado, estado_valido):
        print(f"El estado ingresado {estado} es invalido. Los estados validos son {estado_valido}.")
        estado = input("Por favor, ingrese un estado valido: ")
    
    actualizar_estado(asistencias, numero_dominio, estado)

def cargar_asistencia(asistencias: dict, moviles: dict) -> None:
    # {id_asistencia: [fecha, numero_dominio, tipo_vehiculo, direccion_origen, direccion_destino, tipo_asistencia, tiempo_estimado, prioridad, numero_movil, estado, cobro]}
    id_asistencia = len(asistencias) + 1
    
    dia = input("Ingrese el dia de solicitud de la asistencia: ")
    while numero_invalido(dia):
        dia = input(f"El dia {dia} es invalido. Por favor, ingrese un dia valido: ")
    dia = int(dia)
    
    mes = input("Ingrese el mes de solicitud de la asistencia: ")
    while numero_invalido(mes):
        mes = input(f"El mes {mes} es invalido. Por favor, ingrese un mes valido: ")
    mes = int(mes)
    
    anio = input("Ingrese el anio de solicitud de la asistencia: ")
    while numero_invalido(anio):
        anio = input(f"El anio {anio} es invalido. Por favor, ingrese un anio valido: ")
    anio = int(anio)
    
    fecha = (dia, mes, anio)

    numero_dominio = input("Ingrese el numero de dominio del vehiculo que requiere asistencia: ")
    while numero_invalido(numero_dominio):
        numero_dominio = input(f"El numero de dominio {numero_dominio} es invalido. Por favor, ingrese un numero de dominio valido: ")
    numero_dominio = int(numero_dominio)

    tipo_vehiculo_valido = ['auto', 'moto', 'camioneta', 'camion']
    tipo_vehiculo = input("Ingrese el tipo de vehiculo que requiere asistencia: ")
    while valor_invalido(tipo_vehiculo, tipo_vehiculo_valido):
        print(f"El tipo de vehiulo {tipo_vehiculo} es invalido. Los tipos validos son: {tipo_vehiculo_valido}")
        tipo_vehiculo = input("Por favor, ingrese un tipo de vehiculo valido: ")
    
    direccion_origen = input("Ingrese la direccion de origen de la asistencia: ")
    direccion_destino = input("Ingrese la direccion de destino de la asistencia: ")

    tipo_asistencia_valida = ['mecanica', 'remolque']
    tipo_asistencia = input("Ingrese el tipo de asistencia que requiere el vehiculo: ")
    while valor_invalido(tipo_asistencia, tipo_asistencia_valida):
        print(f"El tipo de asistencia {tipo_asistencia} es invalida. Los tipos validos son: {tipo_asistencia_valida}")
        tipo_asistencia = input("Por favor, ingrese un tipo de asistencia valida: ")
    
    tiempo_estimado = input("Ingrese el tiempo estimado del servicio medido en horas: ")
    while numero_invalido(tiempo_estimado):
        tiempo_estimado = input(f"El tiempo estimado {tiempo_estimado} es invalido. Por favor, ingrese un tiempo estimado valido medido en horas: ")
    tiempo_estimado = int(tiempo_estimado)
    
    prioridad_valida = ['alta', 'media', 'normal']
    prioridad = input("Ingrese la prioridad de la asistencia: ")
    while valor_invalido(prioridad, prioridad_valida):
        print(f"La prioridad {prioridad} es invalida. Las prioridades son: {prioridad_valida}")
        prioridad = input("Por favor, ingrese una prioridad valida: ")
    
    numero_movil = input("Ingrese el numero de movil que realizara la asistencia: ")
    while numero_invalido(numero_movil) or valor_invalido(int(numero_movil), list(moviles.keys())):
        numero_movil = input(f"El numero de movil {numero_movil} es invalido. Por favor, ingrese un numero de movil valido: ")
    numero_movil = int(numero_movil)

    estado_valido = ['finalizado', 'en curso', 'cancelado']
    estado = input("Ingrese el estado del servicio: ")
    while valor_invalido(estado, estado_valido):
        print(f"El estado {estado} es invalido. Los estados son: {estado_valido}")
        estado = input("Por favor, ingrese un estado valido: ")

    cobro = input("Ingrese el valor a cobrar por la asistencia: ")
    while numero_invalido(cobro):
        cobro = input(f"El valor a cobrar {cobro} es invalido. Por favor, ingrese un valor a cobrar valido: ")
    cobro = float(cobro)

    asistencias[id_asistencia] = [fecha, numero_dominio, tipo_vehiculo, direccion_origen, direccion_destino, tipo_asistencia, tiempo_estimado, prioridad, numero_movil, estado, cobro]

def imprimir_opciones() -> None:
    print("-"*10)
    print("Menu de Opciones:")
    print("a. Cargar asistencia recibida")
    print("b. Finalizar/Cancelar un servicio")
    print("c. Agregar un móvil nuevo a la flota")
    print("d. Listar el total de servicios prestados y el total facturado para una fecha para un movil")
    print("e. Obtener el promedio del tiempo estimado total")
    print("f. Obtener el movil que mas servicios presto")
    print("g. Obtener el porcentaje de tipo de asistencia total")
    print("h. Obtener el porcentaje de los tipos de vehiculos asistidos")
    print("i. Salir")
    print("-"*10)

def seleccionar_opcion() -> str:
    imprimir_opciones()

    opt = input("Ingrese una opcion: ")

    while valor_invalido(opt, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']):
        opt = input(f"La opcion {opt} es invalida. Por favor, seleccione una opcion valida: ")

    return opt

def main() -> None:
    print("Bienvenido al Software Oficial de No Te Dejamos Tirado S.A.!")

    asistencias = {} # {id_asistencia: [fecha, numero_dominio, tipo_vehiculo, direccion_origen, direccion_destino, tipo_asistencia, tiempo_estimando_servicio, prioridad, numero_movil, estado_servicio, valor_servicio]}
    
    moviles = {} # {1: 'mecanica', 2: 'remolque'}
    
    opt = seleccionar_opcion()

    while opt != 'i':
        if opt == 'a':
            cargar_asistencia(asistencias, moviles)
        elif opt == 'b':
            cerrar_asistencia(asistencias)
        elif opt == 'c':
            agregar_movil(moviles)
        elif opt == 'd':
            imprimir_total_servicios_movil(asistencias, moviles)
        elif opt == 'e':
            imprimir_promedio_tiempo_estimado(asistencias)
        elif opt == 'f':
            imprimir_movil_mas_solicitado(asistencias)
        elif opt == 'g':
            imprimir_porcentaje_tipo_asistencias(asistencias)
        elif opt == 'h':
            imprimir_porcentaje_tipo_vehiculo(asistencias)
        
        opt = seleccionar_opcion()
    
    return

main()
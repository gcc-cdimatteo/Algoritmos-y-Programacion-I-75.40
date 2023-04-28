def imprimir_pedido(pedidos: dict, id_pedido: int) -> None:
    print(f"-- Pedido {id_pedido}: ")
    print(f" - Nombre del Usuario: {pedidos[id_pedido][0]}")
    print(f" - Fecha de alta: {pedidos[id_pedido][1]}")
    print(f" - Direccion: {pedidos[id_pedido][2]}")
    print(f" - Localidad: {pedidos[id_pedido][3]}")

def id_pedido_invalido(id_pedido, pedidos_keys) -> bool:
    return id_pedido not in pedidos_keys

def imprimir_datos_pedido(pedidos: dict) -> None:
    id_pedido = input("Ingrese el numero de pedido para el cual se quiere buscar la informacion relacionada: ")

    while id_pedido_invalido(id_pedido, pedidos.keys()):
        id_pedido = input(f"El codigo de pedido [{id_pedido}] es invalido. Por favor, ingrese un codigo de pedido valido: ")

    id_pedido = int(id_pedido)

    imprimir_pedido(pedidos, id_pedido)    

def obtener_importe_total(pedidos: dict, tarifas: dict, localidad: str = "") -> float:
    total = 0
    
    for id_pedido in pedidos:
        localidad_pedido = pedidos[id_pedido][3]
        if localidad != "" and localidad_pedido != localidad: continue
        total += tarifas[localidad]
    
    return total

def imprimir_metricas_envios(pedidos: dict, tarifas: dict) -> None:
    print("-- Metricas:")
    
    total_CABA = obtener_importe_total(pedidos, tarifas, 'CABA')
    total_Provincia = obtener_importe_total(pedidos, tarifas, 'Provincia')
    total = obtener_importe_total(pedidos, tarifas) # obtener_importe_total(pedidos, tarifas) == total_CABA + total_Provincia

    print(f"Total en pesos de los envios realizados en CABA: {total_CABA}")
    print(f"Porcentaje de los envios realizados en CABA: {total_CABA / total}")
    print(f"Total en pesos de los envios realizados en Provincia: {total_Provincia}")
    print(f"Porcentaje de los envios realizados en Provincia: {total_Provincia / total}")

def imprimir_listado_envios_usuario_localidad(usuario: str, localidad: str, pedidos: dict, tarifas: dict) -> None:
    print(f"-- Listado de Envios realizados para el usuario {usuario} en {localidad}:")

    total = 0

    for id_pedido in pedidos:
        if pedidos[id_pedido][3] == localidad and pedidos[id_pedido][0] == usuario:
            print(f"Pedido [{id_pedido}] - Realizado el {pedidos[id_pedido][1]} para la direccion {pedidos[id_pedido][2]}")
            total += tarifas[localidad]

    print(f"El importe total valorizado para el usuario {usuario} es: {total}")

def usuario_invalido(usuario: str, pedidos: dict) -> bool:
    for id_pedido in pedidos:
        if usuario == pedidos[id_pedido][0]: return True
    return False

def imprimir_listado_envios_usuario(pedidos: dict, tarifas: dict) -> None:
    usuario = input("Ingrese el nombre del usuario para el cual quiere buscar los pedidos realizados: ")

    while usuario_invalido(usuario, pedidos):
        usuario = input(f"El usuario [{usuario}] es invalido. Por favor, ingrese un nombre de usuario valido: ")
    
    imprimir_listado_envios_usuario_localidad(usuario, 'CABA', pedidos, tarifas)
    imprimir_listado_envios_usuario_localidad(usuario, 'Provincia', pedidos, tarifas)

def tarifa_invalida(tarifa) -> bool:
    return not tarifa.isnumeric()

def cambiar_tarifa_localidad(tarifas: dict, localidad: str) -> None:
    tarifa = input(f"Ingrese una tarifa sin IVA para {localidad}: ")

    while tarifa_invalida(tarifa):
        tarifa = input("La tarifa [{tarifa}] es invalida. Por favor, ingrese una tarifa valida: ")
    
    tarifas[localidad] = int(tarifa)*1.21

def cambiar_tarifas(tarifas: dict) -> None:
    if input("Quiere cambiar la tarifa para CABA? (s/N): ") == 's':
        cambiar_tarifa_localidad(tarifas, 'CABA')

    if input("Quiere cambiar la tarifa para Provincia? (s/N): ") == 's':
        cambiar_tarifa_localidad(tarifas, 'Provincia')

def localidad_invalida(localidad) -> bool:
    return localidad not in ['CABA', 'Provincia']

def cargar_pedido_nuevo(pedidos: dict) -> None:
    id_pedido = len(pedidos.keys()) + 1

    nombre_usuario = input("Ingrese el nombre del usuario que genero el pedido: ").lower()

    dia = int(input("Ingrese el dia de alta del pedido: "))
    mes = int(input("Ingrese el mes de alta del pedido: "))
    anio = int(input("Ingrese el año de alta del pedido: "))
    
    fecha = (dia, mes, anio)

    direccion = input("Ingrese la direccion de origen del pedido: ")

    localidad = input("Ingrese la localidad de origen del pedido (CABA/Provincia): ")
    while localidad_invalida(localidad):
        localidad = input(f"La localidad [{localidad}] es invalida. Por favor, ingrese una localidad valida: ")
    
    pedidos[id_pedido] = (nombre_usuario, fecha, direccion, localidad)

    imprimir_pedido(pedidos, id_pedido)

def imprimir_opciones() -> None:
    print("-"*10)
    print("Menu de Opciones:")
    print("a. Cargar un pedido nuevo")
    print("b. Cambiar las tarifas")
    print("c. Obtener el listado de la informacion de envios de un usuario por localidad")
    print("d. Mostrar las metricas de los envios realizados por localidad")
    print("e. Buscar los datos de un envio")
    print("f. Salir")
    print("-"*10)

def opcion_invalida(opt: str) -> bool:
    return opt not in ['a', 'b', 'c', 'd', 'e', 'f']

def seleccionar_opcion() -> str:
    imprimir_opciones()

    opt = input("Ingrese una opcion: ")

    while opcion_invalida(opt):
        opt = input(f"La opcion [{opt}] es invalida. Por favor, seleccione una opcion valida: ")

    return opt

def main() -> None:
    print("Bienvenido al Software Oficial de Moto Veloz!")

    pedidos = {} # {id_pedido: (nombre_usuario, fecha, direccion, localidad)}
    
    tarifas = {'CABA': 490*1.21, 'Provincia': 750*1.21}
    
    opt = seleccionar_opcion()

    while opt != 'f':
        if opt == 'a':
            cargar_pedido_nuevo(pedidos)
        elif opt == 'b':
            cambiar_tarifas(tarifas)
        elif opt == 'c':
            imprimir_listado_envios_usuario(pedidos, tarifas)
        elif opt == 'd':
            imprimir_metricas_envios(pedidos, tarifas)
        elif opt == 'e':
            imprimir_datos_pedido(pedidos)
        
        opt = seleccionar_opcion()
    
    return

main()
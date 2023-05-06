CUIL = 0
NOMBRE = 1
APELLIDO = 2
H_ENTRADA = 3
H_SALIDA = 4


def parsear_cadena(cadena: str) -> list:
    """
    Pre: Recibe una cadena con los datos de los empleados
    Post: Devuelve una lista con los datos de los empleados
    """
    datos = cadena.split("||")
    datos_de_los_empleados = []
    for dato_del_empleado in datos:
        dato_del_empleado = dato_del_empleado.split(",")
        datos_de_los_empleados.append(dato_del_empleado)
    return datos_de_los_empleados

def cantidad_de_salidas(cadena: str) -> list:
    datos_de_los_empleados = parsear_cadena(cadena)

    salidas = dict()

    for dato_del_empleado in datos_de_los_empleados:
        if dato_del_empleado[CUIL] in salidas:
            salidas[dato_del_empleado[CUIL]] = salidas[dato_del_empleado[CUIL]] + 1
        else:
            salidas[dato_del_empleado[CUIL]] = 1

    return list(salidas.items())

def no_cumple_horario_alternativo(cadena: str) -> None:
    datos_de_los_empleados = parsear_cadena(cadena)

    for dato_del_empleado in datos_de_los_empleados:
        horario_entrada = int(dato_del_empleado[H_ENTRADA])
        horario_salida = int(dato_del_empleado[H_SALIDA])
        horas_trabajadas = (horario_salida - horario_entrada) // 100
        if(horas_trabajadas < 8):
            print(f"El trabajador {dato_del_empleado[NOMBRE]},{dato_del_empleado[APELLIDO]} con cuil {dato_del_empleado[CUIL]} trabajó solamente {horas_trabajadas} horas")

def no_cumple_horario(cadena: str) -> None:
    datos_de_los_empleados = parsear_cadena(cadena)

    horas_trabajadas = dict()
    for dato_del_empleado in datos_de_los_empleados:
        horario_entrada = int(dato_del_empleado[H_ENTRADA])
        horario_salida = int(dato_del_empleado[H_SALIDA])
        horas_de_trabajo = (horario_salida - horario_entrada) // 100
        minutos_trabajos = (horario_salida - horario_entrada) % 100
        if dato_del_empleado[CUIL] in horas_trabajadas:
            (horas, minutos) = horas_trabajadas[dato_del_empleado[CUIL]]
            horas_trabajadas[dato_del_empleado[CUIL]] = (horas + horas_de_trabajo, minutos + minutos_trabajos)
        else:
            horas_trabajadas[dato_del_empleado[CUIL]] = (horas_de_trabajo, minutos_trabajos)

    for dato_del_empleado in datos_de_los_empleados:
        (horas, minutos) = horas_trabajadas[dato_del_empleado[CUIL]]
        horas_sobrantes = minutos // 60
        horas_totales = horas + horas_sobrantes
        if(horas_totales < 8):
            print(f"El trabajador {dato_del_empleado[NOMBRE]},{dato_del_empleado[APELLIDO]} con cuil {dato_del_empleado[CUIL]} trabajó solamente {horas_totales} horas")

def datos_x_cuil(cadena: str, cuil: str) -> list:
    datos_de_los_empleados = parsear_cadena(cadena)
    datos = []

    for dato_del_empleado in datos_de_los_empleados:
        if dato_del_empleado[CUIL] == cuil:
            datos.append(dato_del_empleado)

    return datos


cadena = "1,T,V,1000,1200||2,L,C,900,1300||3,C,D,1200,2000||1,T,V,1300,2000||3,C,D,1200,2000||1,T,V,1000,1550"
# print(cantidad_de_salidas(cadena))
no_cumple_horario(cadena)
print(datos_x_cuil(cadena, '1'))
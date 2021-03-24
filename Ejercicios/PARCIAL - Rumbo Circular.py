'''
"@RumboCircular" es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además
de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad
general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de
un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- Crear un menú que permita el acceso a los siguientes puntos.
b- Modificación de cursos. Se podrá modificar la siguiente infomación de los cursos. Nombre, cantidad de días,
costo.
c- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
d- Cargado de asistentes a los cursos definidos.
e- Mostrar el listado de todos los cursos y sus respectivos asistentes. Ordenados por nombre de curso en forma
ascendente.
'''

def validar_opcion_modificacion(mensaje_input, mensaje_error, tope_inferior, tope_superior):
    '''
    Pre: Recibe mensajes de input y error, el tope inferior y el superior.
    Post:Retorna la opcion validada por el usuario
    '''
    respuesta = input(mensaje_input)
    while(not respuesta.isnumeric() or int(respuesta) > tope_superior or int(respuesta) < tope_inferior):
        print(mensaje_error)
        respuesta = input(mensaje_input)
    return int(respuesta)
def mostrar_cursos(cursos):
    '''
    Pre: Recibe los cursos actuales en el sistema
    Post: Muestra por pantalla los cursos y si tiene ayudantes, muestra los ayudantes
    '''
    print("Se mostrarán los cursos actuales")
    for curso in sorted(cursos):
        if(len(curso) == 3):
            print(f"El curso {curso[0]} dura {curso[1]} dias y cuesta {curso[2]}, no hay asistentes definidos por el momento\n\n")
        else:
            print(f"El curso {curso[0]} dura {curso[1]} dias y cuesta {curso[2]}")
            print(f"Los ayudantes del curso {curso[0]} son {curso[3::]}\n\n")
def cargar_asistentes(cursos):
    '''
    Pre: Agrego un asistente a los cursos
    Post: Un asistente fue agregado al curso
    '''
    print("\n¿A qué curso quiere agregar un asistente?")
    print(f"\n 1.{cursos[0][0]} \n 2.{cursos[1][0]} \n 3. {cursos[2][0]}")
    opcion = validar_opcion_modificacion('Ingrese la opcion del nombre del curso: ', 'Curso invalido', 1, 3)
    if(opcion == 1):
        asistente_curso = input(f"Ingrese el nombre del asistente para agregarlo al curso {cursos[0][0]}\n")
        cursos[0].append(asistente_curso)
    elif(opcion == 2):
        asistente_curso = input(f"Ingrese el nombre del asistente para agregarlo al curso {cursos[1][0]}\n")
        cursos[1].append(asistente_curso)
    elif(opcion == 3):
        asistente_curso = input(f"Ingrese el nombre del asistente para agregarlo al curso {cursos[2][0]}\n")
        cursos[2].append(asistente_curso)
def listar_cursos(cursos):
    for curso in cursos:
        if(curso[2] > 1150):
            print(f"\n\n El curso {curso[0]} tiene un coste mayor a 1150 pesos\n\n")
def pregunta_modificacion(cursos):
    '''
    Pre: Recibe los cursos y su informacion, luego elige que modificar de cada curso
    Post: Retorna que modificar de cada curso en una lista 
    '''
    print("¿Qué desea modificar de los cursos? \n 1.El nombre \n 2.Cantidad de días \n 3.Costo \n")
    indice_uno = validar_opcion_modificacion('Ingrese el dato a modificar: ', 'Dato invalido', 1,3)-1 #Le resto uno porque se devuelve un indice 
    print(f"¿De qué curso? \n 1.{cursos[0][0]} \n 2.{cursos[1][0]} \n 3. {cursos[2][0]} ")
    indice_dos = validar_opcion_modificacion('Ingrese el nombre del curso: ', 'Curso invalido', 1,3)-1 #Le resto uno porque se devuelve un indice
    if(indice_uno == 0):
        print(f"Usted va modificar el nombre del curso {cursos[indice_dos][0]}")
        nombre = input("Ingrese el nombre nuevo del curso: \n")
        cursos[indice_dos][indice_uno] = nombre
    elif(indice_uno == 1):
        print(f"Usted va modificar la cantidad de días del curso {cursos[indice_dos][0]}")
        dias = validar_opcion_modificacion('Ingrese la cantidad de dias:', 'Dias invalidos', 1, 365) #Asumo un anio maximo de duracion
        cursos[indice_dos][indice_uno] = dias
    elif(indice_uno == 2):
        print(f"Usted va modificar el costo del curso {cursos[indice_dos][0]}")
        costo = validar_opcion_modificacion('Ingrese el nuevo costo del curso: ', 'Costo invalido ', 1, 10000)#Asumo que ningun curso va tener precios absurdos
        cursos[indice_dos][indice_uno] = costo
#Indice_uno representa el indice de la sublista del curso
#Indice_dos representa el indice del curso
def opciones(opcion, cursos):
    '''
    Pre: Recibe la opcion del menu y una lista con los cursos sin asistentes al principio
    '''
    if(opcion == 1):
        pregunta_modificacion(cursos)
    elif(opcion == 2):
        listar_cursos(cursos) #Que cuesten mas de 1150$
    elif(opcion == 3):
        cargar_asistentes(cursos)
    elif(opcion == 4):
        mostrar_cursos(cursos)
def main():
    terminar_programa = False
    cursos = [["Aprende  a hacer tu propio compost",1 ,950],["Los niños y el medioambiente(para padres e hijes)",2,990],["Tu huerta orgánica",4,2500]]
    while(terminar_programa == False):
        print('''Bienvenido  al sistema de registros de cursos de RumboCircular, ¿Que desea hacer? 
        1.Modicar uno de los tres cursos 
        2.Mostrar los cursos con un coste mayor a 1150 
        3.Seleccionar asistentes para un curso 
        4.Mostrar el listado de cursos y asistentes 
        5.Cerrar el programa ''')
        opcion = validar_opcion_modificacion('Ingrese una opcion: ', 'Ingreso invalido', 1, 5)
        if(opcion != 5):
            opciones(opcion, cursos)
        else:
            terminar_programa = True
main()
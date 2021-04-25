'''
Cree un programa que permita al usuario elegir entre las siguientes opciones:
1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
3 - Cantidad de alumnos totales y promedio general.
4 - Quitar a un  alumno.
5 - Salir
'''

opciones = ["Agregar un alumno", "Consultar aprobados", "Cantidad de alumnos totales y promedio general", "Quitar a un alumno", "Salir"]
nombres = []
padrones = []
notas = []
flag_salir = False
flag_opcion = False
opcion = ""

print("\nOpciones válidas: \n")

for x in range(len(opciones)):
    print(x + 1, "-", opciones[x])

opcion = input("\nIngrese la opción que desea realizar: ")

while(not flag_salir):
    nombre = ""
    padron = 0
    nota = 0

    # Validación de opción válida
    while(not flag_opcion):
        
        if(opcion.isdecimal()): 
            if(int(opcion) > 0 and int(opcion) <= len(opciones)):
                flag_opcion = True
            else:
                print("\n====== ADVERTENCIA ======\n")
                print("Las opciones válidas se númeran desde el 1 hasta el", len(opciones))
                print("\n====== ADVERTENCIA ======\n")
                
        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Recuerde ingresar el número de la opción")
            print("\n====== ADVERTENCIA ======\n")

        # Se mostrará el mensaje y las opciones, solo si no ingresa una opción válida
        if(not flag_opcion): 
            print("\nOpciones válidas: \n")

            for x in range(len(opciones)):
                print(x + 1, "-", opciones[x])

            opcion = input("\nIngrese la opción que desea realizar: ")

    # TODO: Falta validación para que se ingrese un nombre válido, número de padrón válido y nota válida
    if(opcion == "1"):
        nombre = input("Ingrese el nombre del alumno: ")
        padron = int(input("Ingrese el N° de padrón del alumno: "))
        nota = int(input("Ingrese la nota del alumno: "))

        nombres.append(nombre)
        padrones.append(padron)
        notas.append(nota)

        print("\n¡Se ha ingresado exitosamente un/a alumno/a nuevo/a!\n")

    elif(opcion == "2" or opcion == "3" or opcion == "4"):
        # Es solo declarativo, con poner solo una expresión booleana, es suficiente
        if(nombres == [] or padrones == [] or notas == []): 
            print("\n====== ADVERTENCIA ======\n")
            print("Aún no se ha ingresado ningún alumno")
            print("\n====== ADVERTENCIA ======\n")

        elif(opcion == "2"):
            for alumno in range(len(nombres)):
                if(notas[alumno] >= 4):
                    print("\nEl alumno {0}, con N° de padrón {1}, ha aprobado con una nota de {2}"
                        .format(
                            nombres[alumno],
                            padrones[alumno],
                            notas[alumno]
                        )
                    )

        elif(opcion == "3"):
            # Se puede obtener la longitud de la lista ya sea de nombres, padrones o notas, es indistinto
            cant_alumnos = len(nombres)
            acumulador_notas = 0
            promedio_notas = 0

            for nota in range(len(notas)):
                acumulador_notas += notas[nota]

            promedio_notas = acumulador_notas / cant_alumnos

            print("\nHay una cantidad de {0} alumno/s, y el promedio general es: {1}"
                .format(
                    cant_alumnos,
                    promedio_notas
                )
            )

        elif(opcion == "4"):
            alumno_eliminar = ""
            # TODO: Falta validación para que se ingrese un número de padrón válido
            # TODO: Se optó por camino feliz, pero también se podrían eliminar alumnos por nota y/o nombre
            alumno_eliminar = int(input("Ingrese el N° de padrón, del alumno a eliminar: "))

            if(alumno_eliminar in padrones):
                indice = padrones.index(alumno_eliminar)

                nombres.pop(indice)
                padrones.pop(indice)
                notas.pop(indice)

                print("\nAlumno/a eliminado/a\n")

            else:
                print("\n====== ADVERTENCIA ======\n")
                print("El N° de padrón ingresado, no corresponde a ningún alumno")
                print("\n====== ADVERTENCIA ======\n")                

    # Se mostrará el mensaje y las opciones, sólo si no elige la opción de salir
    if(opcion == "5"): 
        flag_salir = True

    else:
        print("\nOpciones válidas: \n")

        for x in range(len(opciones)):
            print(x + 1, "-", opciones[x])

        opcion = input("\nIngrese otra opción que desee realizar: ")
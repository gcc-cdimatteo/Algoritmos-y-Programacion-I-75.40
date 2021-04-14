'''
Dados los padrones y notas de las 5 cátedras del parcial de Computación, realice un programa que indique:
a) Padrón de la primera persona que aprobó de cada curso
b) Cuantas personas (por curso) obtuvieron esa misma nota que obtuvo el primero que aprobó (de su curso).
c) Porcentaje de reprobados general de todas las cátedras.
d) Promedio de cada cátedra.
Observaciones:
    · La cantidad de alumnos por curso es indeterminada inicialmente, debe consultarse al usuario si desea seguir ingresando información o no.
    · Se considera aprobado cualquier nota mayor o igual a 4
'''

totalAlumnos = 0
totalDesaprobados = 0

for catedraNro in range(1,6):
    ingreso = True
    print("-----" + "Catedra " + str(catedraNro) + "-----")
    aprobados = 0
    desaprobados = 0
    cantPrimerNotaAprobada = 0
    totalNotas = 0
    while ingreso:
        padron = input("Ingrese el Numero de Padron del Alumno: ")
        nota = float(input("Ingrese la nota del alumno " + str(padron) + ": "))
        totalNotas += nota
        if nota >= 4:
            aprobados += 1
            if aprobados == 1:
                primerNotaAprobada = nota
                print("El primer aprobado de la catedra " + str(catedraNro) + " es: " + padron)
            else:
                if primerNotaAprobada == nota: cantPrimerNotaAprobada += 1
        else:
            desaprobados += 1
        if input("Desea seguir ingresando información? s/n: ").lower() != "s": ingreso = False
    totalDesaprobados += desaprobados
    totalAlumnos += desaprobados+aprobados
    print("La cantidad de alumnos que obtuvieron la misma nota que obtuvo el primero aprobado es: " + str(cantPrimerNotaAprobada))
    print("El promedio general de la catedra " + str(catedraNro) + " es: " + str(totalNotas/(aprobados+desaprobados)))

print("El procentaje general de alumnos desaprobados es: " + str(totalDesaprobados*100/totalAlumnos))

print("Adios!")

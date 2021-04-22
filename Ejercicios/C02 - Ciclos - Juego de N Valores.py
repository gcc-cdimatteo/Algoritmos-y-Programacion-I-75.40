'''
Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
Considerar un condiciòn de corte para el n.
Calculando el promedio de cada juego, el máximo de cada juego y el mínimo de todos los juegos.
'''

valor = int(input("Ingrese por favor el primer valor"))
#inicializo la variable mínimo para todos los valores de todos los juegos
minimo = valor
if (valor <0):
    print("se terminó el programa, no ingresó ningún valor")
else:
    #iterar los juegos de 0 a 7
    for juego in range(8):
        #inicializo las variables para cada uno de los juegos!, máximo, contador, y acumulador
        maximo = valor
        contador = 0
        acumulador = 0
        #iterar los valores de cada uno de los juegos
        while(valor>=0):
            if (maximo < valor):
                maximo = valor
            if (minimo > valor):
                minimo = valor
            acumulador = acumulador + valor #tmb acumulador += valor
            contador += 1
            print("El máximo para el juego", juego+1,"es: ", maximo)
            valor = int(input("Ingrese por favor un valor o -1 para salir"))
        promedio = acumulador/contador
        print("El promedio del juego ", juego+1, "es: ", promedio)
        valor = input("Ingrese un nuevo valor o -1 pasa salir")
    #fuera del while y fuera del for, vamos a mostrar el valor mínimo correspondiente a TODOS los valores ingresados.
    print("El valor mínimo de todos los valores ingresados es: ", minimo)
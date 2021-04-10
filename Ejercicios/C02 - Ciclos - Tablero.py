'''
Crear un programa que permita generar un tablero de nxm en el cual la diagonal se muestre con "#" mientras que el resto de las casillas deben mostrar "*".
Pedir al usuario que ingrese una coordenada (fila y columna).
Si el casillero tiene un "*" cambiarlo a "#".
Si  tiene un "#" mostrar un mensaje que diga "la diagonal es del alfil"
Si elige el mismo casillero más de una vez mostrar un mensaje que diga "¿¿¿Pero que esta haciendo???"
'''

# Pido dimensiones del tablero
n = int(input("Ingrese una dimension de filas para el tablero: "))
m = int(input("Ingrese una dimension de columnas para el tablero: "))

# Construyo el tablero
tablero = []
for i in range(n):
    tablero.append([])
    for j in range(m):
        if i == j: tablero[i].append("#")
        else: tablero[i].append("*")

# Imprimo el tablero
for i in range(n):
    print("[ ", end="")
    for j in range(m):
        print(tablero[i][j], end=" ")
    print("] ", end="")
    print()


'''
Crear un programa que permita generar un tablero de nxm en el cual la diagonal se muestre con "#" mientras que el resto de las casillas deben mostrar "*".
Pedir al usuario que ingrese una coordenada (fila y columna).
Si el casillero tiene un "*" cambiarlo a "#".
Si  tiene un "#" mostrar un mensaje que diga "la diagonal es del alfil"
Si elige el mismo casillero que el turno anterior mostrar un mensaje que diga "¿¿¿Pero que esta haciendo???"
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

print("Ingrese una coordenada:")
x = int(input("Posicion de la fila: "))-1
y = int(input("Posicion de la columna: "))-1
old_x = 0
old_y = 0

while x > 0 and x < n and y > 0 and y < m: # Si es coordenada valida
    if (old_x != 0 and old_y != 0) and (x == old_x and y == old_y): # Si es coordenada anterior
        print("¿¿¿Pero que esta haciendo???")
    else: # Si no es coordenada anterior
        if tablero[x][y] == "*":
            tablero[x][y] = "#"
            # Imprimo el tablero
            for i in range(n):
                print("[ ", end="")
                for j in range(m):
                    print(tablero[i][j], end=" ")
                print("] ", end="")
                print()
        else:
            print("la diagonal es del alfil")        
    # Guardo coordenada actual
    old_x = x
    old_y = y
    print("Ingrese una coordenada:")
    x = int(input("Posicion de la fila: "))-1
    y = int(input("Posicion de la columna: "))-1


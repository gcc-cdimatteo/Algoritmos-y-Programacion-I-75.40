'''
Realizar un programa que permita jugar a adivinar un número entero. 
El participante A elige el número a adivinar, y luego hace jugar al participante B, el cual deberá intentar adivinarlo arriesgando números. 
El programa debe guiar al participante B indicándole, en cada intento, si el número arriesgado es mayor o menor al definido por el participante A.
El juego debe concluir al acertar el número o superar los 20 intentos. 
Al acertar el número debe indicar la cantidad de intentos que fueron utilizados para lograrlo. 
En caso de no haber conseguido el objetivo, debe indicarle que ha superado los 20 intentos.
'''

num_secreto = int(input("Ingrese un número para que el próximo jugador adivine: "))

num_adivinado = num_secreto + 1 # Elijo cualquier numero distinto al que se debe adivinar
intentos = 0

while num_secreto != num_adivinado or intentos <= 20:
    num_adivinado = int(input("Ingrese el número que cree que digitó el jugador anterior: "))
    intentos += 1

if intentos <= 20:
    print("Correcto! :) El número que ingresó A fue: ", num_secreto)
    print("Para lograrlo, se utilizaron ", intentos, " intentos")
else:
    print("Qué mal! Ya pasaste los 40 intentos! :( Volvé a intentar en un rato cuando estés más despejado :)")
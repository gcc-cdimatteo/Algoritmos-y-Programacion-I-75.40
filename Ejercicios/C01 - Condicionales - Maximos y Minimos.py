'''
Escribe un prorgrama en Python que solicite al usuario 5 números enteros. 
Luego imprimir el máximo y el mínimo de los valores ingresados. 
El programa deberá permitir el ingreso de valores iguales.
'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
num5 = int(input("Ingrese el quinto numero: "))

# Inicializo el maximo y el minimo
max = num1
min = num1

# Busco el maximo real
if max < num2: max = num2
if max < num3: max = num3
if max < num4: max = num4
if max < num5: max = num5
# En otro caso -> num1 era el maximo

# Analogamente busco el minimo real
if min > num2: min = num2
if min > num3: min = num3
if min > num4: min = num4
if min > num5: min = num5

print(f"El maximo numero ingresado es: {max}")
print(f"El minimo numero ingresado es: {min}")
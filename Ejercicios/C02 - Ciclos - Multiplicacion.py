'''
Dado un número X y otro número Y, multiplicar X * Y sin utilizar el operandor '*'.
X e Y son números enteros.
'''

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

multiplicacion = 0
es_positivo = abs(y) == y
for i in range(abs(y)):
    if es_positivo:
        multiplicacion += x
    else:
        multiplicacion -= x

print(multiplicacion)

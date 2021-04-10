'''
Escribe un programa en Python que solicite 5 números enteros al usuario. 
El mismo debe indicar si entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS DISTINTOS”.
'''

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
num5 = int(input("Ingrese el quinto numero: "))

# Chequeo si num2, num3, num4 o num5 coinciden con el valor de num1
if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5:
    print("HAY DUPLICADOS")
# Analogamente, opero para el resto de los numeros
elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5:
    print("HAY DUPLICADOS")
elif num3 == num1 or num3 == num2 or num3 == num4 or num3 == num5:
    print("HAY DUPLICADOS")
elif num4 == num1 or num4 == num2 or num4 == num3 or num4 == num5:
    print("HAY DUPLICADOS")
elif num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    print("HAY DUPLICADOS")
else:
    print("SON TODOS DISTINTOS")
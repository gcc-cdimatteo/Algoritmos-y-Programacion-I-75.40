'''
Se deberá crear un programa que permita:
Ingresar una palabra y una letra a buscar.
Se deberá buscar la letra en esa palabra; en caso de que esté, se imprimirá: "LA ENCONTRÉ", caso contrario: "PSS, NO 'STABA".
'''

palabra = ""
letra = ""

palabra = input("Ingrese una palabra: ").lower()
letra = input("\nIngrese la letra a buscar: ").lower()

if letra in palabra:
    print("\n¡LA ENCONTRÉ!")
else:
    print("\n¡PSS, NO ESTABA!")
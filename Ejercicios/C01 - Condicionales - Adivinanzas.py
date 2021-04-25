'''
Crear un programa que permita este funcionamiento de juego:
Un usuario1 va a ingresar una palabra y un usuario2 va a tener tres intentos para adivinar cuántas letras contiene esa palabra.
En caso de que el usuario2 adivine la cantidad; se printeará: "Muy bien!"
En caso de que el usuario2 adivine la cantidad DOS VECES; se printeará: "AH, PERO SOS BUENÍSIMOOOOO"
En caso de que el usuario2 no adivine la cantidad ninguna vez; se printeará: "Vuelva prontos; esta vez no se pudo"

AYUDA: Para saber la cantidad de caracteres que contiene una string se puede usar len(), que devuelve un número.
Ejemplo de cómo usar len():
largo = len("palabra")
print(largo)
el output será:
>>> 7
'''

palabra = ""
longitud_palabra = 0
intento01 = 0
intento02 = 0
intento03 = 0

palabra = input("Usuario1, ingresar una palabra: ")
longitud_palabra = len(palabra)

print("\nUsuario2, tendrá 3 intentos para adivinar la longitud de la palabra que ingresó el usuario1\n")

intento01 = int(input("1er intento: "))
intento02 = int(input("2do intento: "))
intento03 = int(input("3er intento: "))

if ((intento01 == longitud_palabra and intento02 == longitud_palabra) or 
    (intento01 == longitud_palabra and intento03 == longitud_palabra) or 
    (intento02 == longitud_palabra and intento03 == longitud_palabra)):

    print("\nAH, PERO SOS BUENÍSIMOOOOO\n")

elif (intento01 == longitud_palabra or intento02 == longitud_palabra or 
      intento03 == longitud_palabra):

    print("\n¡Muy bien!")

else:
    print("Vuelva prontos; esta vez no se pudo")
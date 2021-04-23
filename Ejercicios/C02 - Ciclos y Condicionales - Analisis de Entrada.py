'''
Realice un programa que permita el ingreso de N caracteres ingresados por teclado. 
El programa deberá indicar cuántos caracteres son número, cuántos letras y cuántos caracteres especiales.
Al finalizar deberá sacar la suma de todos los números que se hayan ingresado.
'''

entrada = "si"
caracter = ""
cant_numeros = 0
cant_letras = 0
cant_caracteres_especiales = 0

while(entrada != "no"):
    caracter = input("\nIngrese un carácter: ")

    if(caracter.isalpha()):
        if(caracter.isdigit()):
            cant_numeros += 1

        else:
            cant_letras += 1

    else:
        cant_caracteres_especiales += 1

    entrada = input("\n¿Desea seguir ingresando caracteres <si/no>?: ").lower()

print(f"\nSe ingresaron {cant_numeros} caracteres que son numeros")
print(f"\nSe ingresaron {cant_letras} caracteres que son letras")
print(f"\nSe ingresaron {cant_caracteres_especiales} caracteres que son especiales")
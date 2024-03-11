"""
Se pide crear una función que reciba como parámetro un string. La misma debe devolver una tupla de enteros, 
donde el primer valor es la cantidad de palabras de menor longitud y el segundo valor es la cantidad de 
palabras de mayor longitud. Remover del análisis los caracteres especiales “.”, “,”, “;”, “:”.

Ejemplo:
>>> “Las personas mayores nunca son capaces de comprender las cosas por sí mismas, y es muy aburrido para los niños tener que darles una y otra vez explicaciones.”

>>> (2, 1)

Hay dos palabras de largo 1 (“y”, “y”)
Hay una palabra de largo 13 (“explicaciones”)
"""

def calcular_minima_y_maxima_cantidad_de_palabras_en_longitud(texto: str) -> tuple[int, int]:
    caracteres_especiales: list = ['.', ',', ';', ':']

    for caracter in caracteres_especiales:
        texto = texto.replace(caracter, '')

    palabras: list = texto.split()

    # Uso como pivote, el primer elemento de la lista de palabras, para el máximo y mínimo
    minima_palabra: str = palabras[0]
    maxima_palabra: str = palabras[0]
    cantidad_de_palabras_minimas: int = 0
    cantidad_de_palabras_maximas: int = 0

    for palabra in palabras:
        if len(minima_palabra) > len(palabra):
            minima_palabra = palabra
            cantidad_de_palabras_minimas = 1

        elif len(minima_palabra) == len(palabra):
            cantidad_de_palabras_minimas += 1

        if len(maxima_palabra) < len(palabra):
            maxima_palabra = palabra
            cantidad_de_palabras_maximas = 1

        elif len(maxima_palabra) == len(palabra):
            cantidad_de_palabras_maximas += 1

    print(f'Palabra de mínima longitud: "{minima_palabra}"')
    print(f'Palabra de máxima longitud: "{maxima_palabra}"')

    return cantidad_de_palabras_minimas, cantidad_de_palabras_maximas


def main() -> None:
    texto: str = 'Las personas mayores nunca son capaces de comprender las cosas por sí mismas, y es muy aburrido para los niños tener que darles una y otra vez explicaciones.'
    
    resultado: tuple = calcular_minima_y_maxima_cantidad_de_palabras_en_longitud(texto)

    print(resultado)


main()
'''
Analizando textos…. La consultora "Nunca le erramos" quiere analizar los textos que la gente postea en las redes sociales sobre reviews y saber si los textos son de carácter positivo o negativos. Para esto la Consultora nos facilita un endpoint que devuelve una lista cuyos elementos son cadenas de texto. 
El endpoint se llama List<String> TextFromReview( string SocialMedia)
#Input: SocialMedia parámetro de entrada con el nombre de la red social
#Output: Lista de cadenas con los textos correspondientes a esa red Social 
Se pide realizar un programa que analice los textos de Facebook.
Ejemplo de uso del endpoint:
CadenasTexto = []
CadenasTexto = TextFromReview("Facebook")
print(CadenaTexto)  => ("Los productos ACME son muy malos, jamás compres uno!", "Excelente Vendedor, recomendable", "100% seguro", "No lo recomiendo", "10 puntos").
Un texto se determinará positivo o negativo, dependiendo de la cantidad total de palabras positivas o negativas que tenga. 
Palabras positivas:
(Bueno, seguro, Excelente, Bien, Recomendable, Sí, Mejor, Positivo, 10, 100%).
Palabras negativas:
(Malo, inseguro, Horrible, Feo, No, Peor, 0%, Negativo, Nunca)
Se pide saber cuáles son los textos positivos y negativos que determina el programa y la cantidad de los mismos.
'''

import re

POSITIVE_WORDS = [
    "Bueno", "seguro", "Excelente", "Bien", "Recomendable", 
    "Sí", "Mejor", "Positivo", "10", "100%"
]

NEGATIVE_WORDS = [
    "Malo", "inseguro", "Horrible", "Feo", 
    "No", "Peor", "0%", "Negativo", "Nunca"
]


def are_containing_numbers(status_word,  # type: str
                           text_word  # type: str
                           ):

    matched_status_word = []
    matched_text_word = []
    are_containing_numbers = False

    matched_status_word = re.findall("\S*\d+\S*", status_word)
    matched_text_word = re.findall("\S*\d+\S*", text_word)

    are_containing_numbers = len(matched_status_word) == 1 and len(matched_text_word) == 1

    return are_containing_numbers


def count_type_words(text,  # type: str
                     words_type  # type: list[str]
                     ):

    counter = 0
    text_words = []
    matched_words = []

    text_words = re.split("\s+|,\s*", text)

    for word_type in words_type:

        for text_word in text_words:

            if not are_containing_numbers(word_type, text_word):
                matched_words = re.findall(f"^{word_type.lower()}", text_word.lower())
                counter += len(matched_words)

            else:
                matched_words = re.findall(f"^{word_type.lower()}$", text_word.lower())
                counter += len(matched_words)

    return counter


def print_type_text(status_text,  # type: str
                    number_positive_words,  # type: int
                    number_negative_words  # type: int
                    ):

    print(status_text)
    print(f"Cantidad de palabras positivas  :  {number_positive_words}")
    print(f"Cantidad de palabras negativas  :  {number_negative_words}")    


def evaluate_text(text,  # type: str
                  number_positive_words,  # type: int
                  number_negative_words  # type: int
                  ):

    status_text = ""

    if number_positive_words == number_negative_words:
        status_text = f"\nEl texto: '{text}' no es positivo ni negativo"

        print_type_text(status_text, number_positive_words, number_negative_words)

    elif number_positive_words > number_negative_words:
        status_text = f"\nEl texto: '{text}' es positivo"
        
        print_type_text(status_text, number_positive_words, number_negative_words)

    else:
        status_text = f"\nEl texto: '{text}' es negativo"
        
        print_type_text(status_text, number_positive_words, number_negative_words)


def main():
    CADENA_TEXTO = [
        "Los productos ACME son muy malos, jamás compres uno!", 
        "Excelente Vendedor, recomendable", 
        "100% seguro", 
        "No lo recomiendo", 
        "10 puntos"
    ]

    number_positive_words = 0
    number_negative_words = 0

    for text in CADENA_TEXTO:
        number_positive_words += count_type_words(text, POSITIVE_WORDS)
        number_negative_words += count_type_words(text, NEGATIVE_WORDS)

        evaluate_text(text, number_positive_words, number_negative_words)

        number_positive_words = 0
        number_negative_words = 0        
    

if __name__ == "__main__":
    main()
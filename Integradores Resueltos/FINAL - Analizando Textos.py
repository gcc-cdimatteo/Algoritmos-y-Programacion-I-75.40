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

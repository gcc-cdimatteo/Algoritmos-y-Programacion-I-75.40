def obtener_palabras_mayores(parrafo: str, largo: int) -> list:
    palabras = parrafo.split(" ")

    palabras_mayores = []

    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra).upper()
        if len(palabra_limpia) == largo: palabras_mayores.append(palabra_limpia)
    
    return palabras_mayores

def sacar_palabras_prohibidas(parrafo: str, palabras_prohibidas: list) -> str:
    for palabra in palabras_prohibidas:
        parrafo = parrafo.replace(palabra, "*"*4)
    
    return parrafo

def imprimir_ocurrencias(ocurrencias: dict) -> None:
    for palabra in ocurrencias:
        print(f" - {palabra} tiene {ocurrencias[palabra]} ocurrencia(s)")

def limpiar_palabra(palabra: str) -> str:
    caracteres_invalidos = []
    for i in range(len(palabra)):
        if not palabra[i].isalnum(): caracteres_invalidos.append(palabra[i])

    for c in caracteres_invalidos:
        palabra = palabra.replace(c, "")

    return palabra

def contar_ocurrencias(parrafo: str) -> dict:
    palabras = parrafo.split(" ")

    for i in range(len(palabras)):
        palabras[i] = limpiar_palabra(palabras[i]).upper()

    ocurrencias = {}

    for palabra in palabras:
        if palabra in ocurrencias: ocurrencias[palabra] += 1
        else: ocurrencias[palabra] = 1
    
    return ocurrencias

def main():
    parrafo = "Hay quienes me buscan toda una vida, pero no nos encontramos, y quienes reciben mi beso y me rechazan, desagradecidos, desdichados. A veces, parece que prefiero a los inteligentes, a los bellos, a los altos, pero bendigo a todos lo que tienen el coraje de intentarlo. En general, cuando actúo, soy de mano suave, dulce, de miel, pero si me desprecian, me convierto en una bestia difícil de vencer. Porque aunque mis golpes, todos dan siempre en el blanco, cuando mato, lo hago muy, muy despacio..."

    palabras_prohibidas = ["suave", "miel", "mato"]

    print(f"-- Cantidad de Ocurrencias por Palabra: ")    
    imprimir_ocurrencias(contar_ocurrencias(parrafo))
    print()
    print(f"-- Parrafo sin Palabras Prohibidas: ")
    print(sacar_palabras_prohibidas(parrafo, palabras_prohibidas))
    print()
    print(f"-- Palabras de largo mayor a 5: ")
    print(obtener_palabras_mayores(parrafo, 5))


main()
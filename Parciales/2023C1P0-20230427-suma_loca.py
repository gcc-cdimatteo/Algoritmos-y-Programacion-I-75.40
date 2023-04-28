import random

def generar_lista() -> list:
    return random.sample(range(10, 30), 5)

def suma_loca(lista: list) -> list:
    suma = []

    for i in range(len(lista)):
        total = 0
        for j in range(len(lista)):
            if i == j: continue
            total += lista[j]
        suma.append(total)
    
    return suma


def main():
    print(suma_loca([2, 8, 4, 1]))
    
    # generando listas nuevas...
    print(suma_loca(generar_lista()))

main()
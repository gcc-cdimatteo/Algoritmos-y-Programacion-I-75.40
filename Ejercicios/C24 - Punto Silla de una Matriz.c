// Se dice que una matriz tiene su punto silla si alguna posición de la matriz es el menos valor de su fila, y a la vez el mayor de su columna. 
// Escribir un programa que tenga como entrada una matriz de números reales y calcular su posición de un punto silla si es que existe.

#include <stdio.h>
#include <stdlib.h>
#define MAX_COL 2
#define MAX_FIL 2

typedef struct coordenada {
    int x;
    int y;
    } coordenada_t;

coordenada_t silla(int matriz[][]) {
    coordenada_t coordenada_silla;
    coordenada_silla.x = -1;
    coordenada_silla.y = -1;
    for (size_t i = 0; i < MAX_FIL; i++) {
        for (size_t j = 0; j < MAX_COL; j++) {
        //completar logica
        }
    }
    return coordenada_silla;
}

int main() {
    int matriz[MAX_FIL][MAX_COL] = {{1,2},{1,2}};
    coordenada_t silla = silla(matriz);
    if(silla.x == -1 && silla.y == -1) {
        printf("No hay punto silla\n");
    } else {
        printf("El punto silla se encuentra en la coordenada: (%i, %i)\n", silla.x, silla.y);
    }
    return 0;
}
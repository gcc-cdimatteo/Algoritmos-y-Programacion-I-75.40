/*
Implementar una función en C que permita hallar el valor máximo y mínimo de un vector de enteros, sabiendo que la firma de la función es la siguiente:
void hallar_max_min(int array[], int n, int* max, int* min);

Se debe ejemplificar su uso desde una invocación a la misma en el programa principal.
*/

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 10

void hallar_max_min(int array[], int n, int* max, int* min) {
    *max = array[0];
    *min = array[0];

    for(size_t i = 0; i < n; i++) {

        if(array[i] < *min) {
            *min = array[i];
        }

        if(array[i] > *max) {
            *max= array[i];
        } 
    }
}

int main() {
    int max = 0;
    int min = 0;

    int numeros[MAX_SIZE] = {1, 57, -10, 0, 11, 34, -3, -21, 77, -8};

    hallar_max_min(numeros, MAX_SIZE, &max, &min);

    printf("\nEl máximo número es %d, y el mínimo número es %d.\n", max, min);

    return 0;
}
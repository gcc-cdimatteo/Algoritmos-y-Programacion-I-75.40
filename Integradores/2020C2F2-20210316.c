/*
Dado un string, programe una función que invierta el string y lo imprima. Además, en caso de haber una e deberá ser reemplazada por una a.
Ej.: void invertiString(char palabra []);
madera
>>> aradam
No se permite el uso de la función strrev.
*/

#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

void invertirString(char palabra[]) {

    /*
    PRE: 'palabra', debe ser una variable de tipo array de chars
    POST: Invierte las posiciones de la palabra contenida en el  
          array de chars
    */

    int tamanio = strlen(palabra);

    size_t j = tamanio;

    for (size_t i = 0; i < tamanio / 2; i++) {
        char caracter = palabra[i];

        if (palabra[i] == 'e') {
            caracter = 'a';
        }

        if (palabra[tamanio - i - 1] == 'e') {
            palabra[tamanio - i - 1] = 'a';
        }

        palabra[i] = palabra[tamanio - i - 1];

        palabra[tamanio - i - 1] = caracter;
    }
}

int main() {
    char palabra[MAX_SIZE];

    strncpy(palabra, "madera", MAX_SIZE);

    printf("\nVariable 'palabra' antes del cambio: %s\n", palabra);

    invertirString(palabra);

    printf("\nVariable 'palabra' después del cambio: %s\n", palabra);

    return 0;
}
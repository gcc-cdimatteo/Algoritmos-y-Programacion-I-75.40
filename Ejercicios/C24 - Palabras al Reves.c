// Escribir un programa que lea una palabra (1 <= len <= 100 ), y la imprima al revés.
// Input y output manejados desde main, cómputo desde otra función
// Ej: olbaid -> diablo.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char* p1 = "hola";
    char aux [20];
    int j = 0;
    for (int i = strlen(p1)-1; i >= 0; i--) {
        aux[j] = p1[i];
        j++;
    }
    aux[j] = '\0';
    printf("%s\n", aux);
    return 0;
}
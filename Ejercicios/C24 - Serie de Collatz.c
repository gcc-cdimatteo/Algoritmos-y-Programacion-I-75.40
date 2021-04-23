// Considere un algoritmo que toma como input un entero n > 0. Si n es par se divide por 2, si es impar se multiplica por 3 y se le suma 1. 
// El algoritmo se repite hasta que n sea 1.
// Ej: n = 3 ->  3→10→5→16→8→4→2→1

#include <stdio.h>

int ingresarNumero() {
    int numero = 0;

    printf("\nIngrese un número entero: ");
    scanf(" %d", &numero);

    return numero;
}

void calcular(int numero) {
    if(numero > 0) {
        if(numero == 1) {
            printf("\n¡Llegué al final!\n");
        }
        else if(numero % 2 == 0) {
            numero /= 2;

            printf("\n%d\n", numero);

            calcular(numero);
        }
        else{
            numero = numero * 3 + 1;

            printf("\n%d\n", numero);

            calcular(numero);
        }
    }
    else {
        printf("\nSólo se pueden ingresar numeros enteros mayores a 0\n");
    }
}

int main() {
    int numero = 0;

    numero = ingresarNumero();

    calcular(numero);

    return 0;
}
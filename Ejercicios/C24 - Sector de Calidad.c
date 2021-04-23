// Se pide desarrollar un programa en lenguaje C, que cumpla con este enunciado:
// En el sector de calidad de nuestra industria se realizan mediciones de la concentración de un contaminante en ciertas muestras. Los valores que se registran son enteros.
// El sector nos pide que escribamos un programa que permita ingresar los valores de las mediciones (máximo 50) y le informe:
// 1) Cantidad total de mediciones ingresadas.
// 2) Los valores de las mediciones que son mayores al valor generado por la fórmula:
// Valor = (máximo - mínimo) / 2
// Para esto nos brindan la función "asignar_max_min" que debemos utilizar para hallar el máximo y el mínimo.
// Recibe un vector de enteros con su respectivo tope y asigna a max y min el valor máximo y mínimo del vector.
// void asignar_max_min(int vec[MAX],int tope, int *max, int *min);

#include <stdio.h>
#include <string.h>

#define MAX_MEASUREMENTS 50
#define MAX_STRING_SIZE 40

int ingresar_datos(int *mediciones) {
    int c;
    char ingreso[MAX_STRING_SIZE];

    int cant_mediciones = 0;

    do {
        printf("\nIngrese la %d° medición: ", cant_mediciones + 1);
        scanf(" %d", &*(mediciones + cant_mediciones));

        cant_mediciones += 1;

        /*
            Se encarga de obtener los saltos de línea que hayan quedado
            almacenados en el stdin, y avanzar hasta que no quede ninguno
        */
        while ((c = getchar()) != '\n' && c != EOF) { }

        printf("\n¿Desea seguir ingresando datos <s/n>?: ");
        fgets(ingreso, MAX_STRING_SIZE + 1, stdin);

        ingreso[strlen(ingreso) - 1] = '\0';

    } while(strcmp("n", ingreso) != 0 && cant_mediciones < MAX_MEASUREMENTS);

    return cant_mediciones;
}

void asigna_max_min(int mediciones[MAX_MEASUREMENTS], int cant_mediciones, int *max_medicion, int *min_medicion) {
    *max_medicion = mediciones[0];
    *min_medicion = mediciones[0];

    for(size_t i = 0; i < cant_mediciones; i++) {

        if(mediciones[i] < *min_medicion) {
            *min_medicion = mediciones[i];
        }

        if(mediciones[i] > *max_medicion) {
            *max_medicion = mediciones[i];
        }        
    }    
}

void imprimir(int cant_mediciones, double valor_formula, int mediciones[MAX_MEASUREMENTS]) {
    printf("\nSe ha ingresado un total de %d mediciones\n", cant_mediciones);
    printf("\nValor de la formula: %lf\n", valor_formula);

    for(size_t i = 0; i < cant_mediciones; i++) {

        if(mediciones[i] > valor_formula) {
            printf("\nMedición %zu, valor: %d", i + 1, mediciones[i]);
        }
    }

    printf("\n");
}

int main(void) {
    int mediciones[MAX_MEASUREMENTS];

    int cant_mediciones = 0;
    int max_medicion = 0;
    int min_medicion = 0;
    double valorFomula = 0;

    cant_mediciones = ingresar_datos(mediciones);
    asigna_max_min(mediciones, cant_mediciones, &max_medicion, &min_medicion);

    valorFomula = (double)(max_medicion - min_medicion) / 2;

    imprimir(cant_mediciones, valorFomula, mediciones);

    return 0;
}
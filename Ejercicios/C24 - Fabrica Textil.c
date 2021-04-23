// Se pide hacer un programa en lenguaje C, que permita:
// a- Crear una función para la registración de rollos de tela a una fábrica textil, cada rollo posee un nro de rollo y un peso en kg.
//  Se pide:
//      - Calcular el peso promedio de los rollos que han ingresado a la fábrica.
//      - Determinar nro de rollo cuyo peso sea el mayor de entre todos los rollos ingresados.
// b- Sabiendo que la encimadora de tela utiliza rollos mayores a 12kg, crear una función que sea llamada por la del pto a, que valide el peso del rollo y en caso que el mismo sea menor a 12kg imprima un mensaje “Error fuera de norma”

#include <stdio.h>
#include <string.h>

#define MAX_ROLLS 100
#define MAX_STRING_SIZE 40

typedef struct rollo {
    int nro;
    double peso;
} rollo_t;

void validarPeso(double peso) {
    if(peso < 12) { 
        printf("\nError fuera de norma\n");
    }
}

int ingresarDatos(rollo_t *rollos) {
    int c;
    char ingreso[MAX_STRING_SIZE];

    int cantRollos = 0;

    do {
        printf("\nIngrese el número del %d° rollo: ", cantRollos + 1);
        scanf(" %d", &(rollos + cantRollos)->nro);
        
        printf("Ingrese el peso del %d° rollo: ", cantRollos + 1);
        scanf(" %lf", &(rollos + cantRollos)->peso);

        validarPeso((rollos + cantRollos)->peso);

        cantRollos += 1;

        /*
            Se encarga de obtener los saltos de línea que hayan quedado
            almacenados en el stdin, y avanzar hasta que no quede ninguno
        */
        while ((c = getchar()) != '\n' && c != EOF) { }

        printf("\n¿Desea seguir ingresando datos <s/n>?: ");
        fgets(ingreso, MAX_STRING_SIZE + 1, stdin);

        ingreso[strlen(ingreso) - 1] = '\0';

    } while(strcmp("n", ingreso) != 0);

    return cantRollos;
}

double calcularPesoPromedio(rollo_t rollos[MAX_ROLLS], int cantRollos) {
    double totalPeso = 0;
    double pesoPromedio = 0;

    for(size_t i = 0; i < cantRollos; i++) {
        totalPeso += rollos[i].peso;
    }

    pesoPromedio = totalPeso / cantRollos;

    return pesoPromedio;
}

int rolloMayorPeso(rollo_t rollos[MAX_ROLLS], int cantRollos) {
    int nroRolloMayorPeso = rollos[0].nro;
    double mayorPeso = rollos[0].peso;

    for(size_t i = 0; i < cantRollos; i++) {
        if(rollos[i].peso > mayorPeso) {
            mayorPeso = rollos[i].peso;
            nroRolloMayorPeso = rollos[i].nro;
        }
    }

    return nroRolloMayorPeso;
}

int main(void) {
    rollo_t rollos[MAX_ROLLS];

    int cantRollos = 0;
    int nroRolloMayorPeso = 0;
    double pesoPromedio = 0;

    cantRollos = ingresarDatos(rollos);
    pesoPromedio = calcularPesoPromedio(rollos, cantRollos);
    nroRolloMayorPeso = rolloMayorPeso(rollos, cantRollos);

    printf("\nEl peso promedio de los rollos es de %lfkg \n", pesoPromedio);
    printf("\nEl rollo de mayor peso es el número %d \n", nroRolloMayorPeso);

    return 0;
}
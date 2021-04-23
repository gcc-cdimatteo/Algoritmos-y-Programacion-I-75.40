// El ingeniero Guido desea realizar un análisis estratégico del juego "Among us" y para el mismo requiere realizar un programa en el
// lenguaje de programación C que le permita realizar las siguientes acciones:
// i) Cargar las veces que fue impostor y la cantidad de personas que logro asesinar en cada ocasión.
// ii) Cargar las veces que fue tripulante y la cantidad de veces que murió (siendo tripulante o impostor)
// Para mejorar su juego desea que el programa informe en orden:
// 1) Resultado del siguiente calculo: Asesinados totales / ( Nº de veces de tripulante - Nº de veces que murió).
// 2) Mostrar el siguiente mensaje con la información de ingreso correspondiente:
// Impostor:
// Juego 1 - 5 asesinados
// Juego 2 - 1 asesinados
// Juego 3 - 2 asesinados
// ...
// Requisitos:
// 1) Respetar las buenas practicas de programación.
// 2) Utilizar mas de 2 funciones y/o procedimientos.

#include <stdio.h>

#define MAX_KILLS 100

typedef struct jugador {
    int cantVecesImpostor;
    int cantVecesTripulante;
    int cantMuertes;
    int cantAsesinatos[MAX_KILLS];
} jugador_t;

void ingresarDatos(jugador_t *jugador) {

    printf("Ingrese la cantidad de veces que fue impostor: ");
    scanf(" %d", &jugador->cantVecesImpostor);

    for(size_t i = 0; i < jugador->cantVecesImpostor; i++) {
        printf("\nIngrese la cantidad de tripulantes que asesino, la %zu° vez que fue impostor: ", i + 1);
        scanf(" %d", &jugador->cantAsesinatos[i]);
    }    

    printf("\nIngrese la cantidad de veces que fue tripulante: ");
    scanf(" %d", &jugador->cantVecesTripulante);

    printf("\nIngrese la cantidad de veces que murió en total (Siendo inocente o impostor): ");
    scanf(" %d", &jugador->cantMuertes);    
}

int calcularTotalAsesinatos(int *cantAsesinatos, int cantVecesImpostor) {
    int totalAsesinatos = 0;

    for(size_t i = 0; i < cantVecesImpostor; i++) {
        totalAsesinatos += *(cantAsesinatos + i);
    }

    return totalAsesinatos;
}

void imprimirCalculo(int totalAsesinatos, jugador_t jugador) {
    double calculo = totalAsesinatos / (double)(jugador.cantVecesTripulante - jugador.cantMuertes);

    printf("\nAsesinados totales / ( Nº de veces de tripulante - Nº de veces que murió) = %lf \n", calculo);
}

void imprimirInfoImpostor(int cantAsesinatos[MAX_KILLS], int cantVecesImpostor) {
    printf("\nImpostor: \n");

    for(size_t i = 0; i < cantVecesImpostor; i++) {
        printf("Juego %zu -", i + 1);
        printf(" %d asesinados\n", cantAsesinatos[i]);
    } 
}

int main(void) {
    jugador_t jugador;
    int totalAsesinatos = 0;
    double calculo = 0;

    ingresarDatos(&jugador);
    totalAsesinatos = calcularTotalAsesinatos(jugador.cantAsesinatos, jugador.cantVecesImpostor);

    imprimirCalculo(totalAsesinatos, jugador);
    imprimirInfoImpostor(jugador.cantAsesinatos, jugador.cantVecesImpostor);

    return 0;
}
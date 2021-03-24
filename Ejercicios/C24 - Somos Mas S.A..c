// Se pide hacer un programa en lenguaje C, que permita:
// a-	Crear una función que solicite el ingreso del legajo y el sueldo de los N empleados de la empresa “Somos Más S.A”, imprimiendo por pantalla cuál es el sueldo mínimo, todos los legajos que cobren más de 80500 pesos. Dicha función deberá devolver un entero con la cantidad de personas cobran por encima de 80500 pesos.
// b-	Crear un procedimiento que reciba el dato de la función del punto a por parámetro y escriba por pantalla:
// >>>  En Somos Más S.A. los empleados que cobran más de 80500 pesos son: ………

#include "stdio.h"
#define CANTIDAD_MAXIMA  100
#define SUELDO_MOSTRAR 80500

int mostrar_sueldos(int cantidad_empleados, int legajos[CANTIDAD_MAXIMA], int sueldos[CANTIDAD_MAXIMA]){
    printf("Lista de empleados con un sueldo mayor a %i",SUELDO_MOSTRAR);
    int contador = 0;
    for (int i=0; i< cantidad_empleados; i++){
        if (sueldos[i] > SUELDO_MOSTRAR){
            printf("%i\n", legajos[i]);
            contador++;
        }
    }
    return contador;
}

int main() {
    int contador = 0;
    int cantidad_empleados; //contiene basura
    int sueldos[CANTIDAD_MAXIMA];
    int legajos[CANTIDAD_MAXIMA];
    int legajo_actual;
    int sueldo_actual;
    printf("Ingrese la cantidad de empleados: ");
    scanf("%i", &cantidad_empleados);
    while (contador <= CANTIDAD_MAXIMA && (contador <= cantidad_empleados)){
        contador++;
        //contador = 1
        printf("Ingerse el sueldo del empleado N°%i: ",contador);
        scanf("%i", &sueldo_actual);
        printf("Ingerse el legajo empleado N°%i: ",contador);
        scanf("%i", &legajo_actual);
        legajos[contador-1] = legajo_actual;
        sueldos[contador-1] = sueldo_actual;
    }
    mostrar_sueldos(cantidad_empleados, legajos, sueldos);
    return 0;
}
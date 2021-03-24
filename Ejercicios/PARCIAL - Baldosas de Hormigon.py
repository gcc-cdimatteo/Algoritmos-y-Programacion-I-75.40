'''
En un pintoresco jardín hay un camino demarcado por baldosas de hormigón convenientemente espaciadas.
Se desea pintarlas de vivos colores habiendo elegido rojo (R), azul (A) y verde (V). Aprovechando que la cantidad es múltiplo de 3 se desea pintar igual cantidad con cada uno de los colores elegidos. Además dos baldosas consecutivas no pueden tener el mismo color.
Uno de los pintores se ha adelantado y sin consultar pintó una de las baldosas. Antes de proseguir con la tarea se quiere disponer de una planificación que respete las reglas indicadas y el color de la baldosa ya pintada.
Puedes colaborar escribiendo una función que haga una propuesta coherente de colores.
Dicha función recibe una cadena conteniendo una hilera formada por caracteres asterisco (*) y una letra A, R, V, correspondiente a la baldosa ya pintada. El lago de la hilera debe ser múltiplo de 3 y menor a 256. Cada asterisco representa una baldosa a ser pintada y esa única letra a la baldosa ya pintada indicando además su color. Mientras que la función devuelve una cadena que representa una hilera del mismo largo que la leída pero conteniendo exclusivamente letras indicando colores de baldosa.
La función debe validar la condición de entrada.
Ejemplo:
    Estado del camino antes:
    *R
    Una posible propuesta de pintado:
    VRVARA
'''

'''
El restaurante Santa Catalina del Centro porteño desea implementar un sistema de autoservicio. Para lo cual nos pide hacer un sistema que contemple las siguientes funcionalidades:
a.      Cargar menú del restaurant: donde cada plato tiene 3 atributos: Nombre, tipo (E: Entrada, P: Principal, O: Postre) y valor
b.      Listar los platos y cargar pedido. Mostrar listado ordenado según Entradas, principales y postres. Luego de mostrar el listado debe permitir cargar el pedido, agregando platos a pedido del comensal, pueden ser varios platos en un mismo pedido y diferentes cantidades de cada uno. Al finalizar la carga del pedido se debe mostrar el importe total a abonar. El programa deberá permitir cargar diversos pedidos con sus respectivos pagos.
c.      Finalmente, el programa deberá emitir los siguientes reportes:
    1.      Indicar que volumen de $ se facturó de un determinado plato a elección del usuario
    2.      Indicar cual es el plato más pedido de cada tipo
    3.      Indicar los pedidos donde se hayan pedido 2 entradas o mas.
'''

subopciones = ["Informar volumen de $ que se facturó de un determinado plato", "Informar plato más pedido de cada tipo", "Informar pedidos con 2 entradas o mas"]
opciones = ["Cargar menú del restaurant", "Listar los platos y cargar pedido", "Emitir reportes", "Salir"]
tipos = [["E", "Entrada"], ["P", "Principal"], ["O", "Postre"]]
# Mockeo de platos
# ["Puré", "E", 150.1], ["Ensalada", "E", 110.5], ["Papas fritas", "E", 200.25], ["Milanesa", "P", 140], ["Bife de chorizo", "P", 190.80], ["Helado", "O", 90.5]
platos = []
# Mockeo de pedidos
# [[2, 2, 2, 2, 2, 3, 3, 3], 1421.25], [[5], 90.5], [[1, 2, 3, 4], 641.55], [[0, 4], 340.9], [[1, 2, 2, 3, 4], 841.8], [[0, 0], 300.2]
pedidos = []

flag_salir = False

opcion = ""


print("\nOpciones válidas: \n")

for x in range(len(opciones)):
    print(x + 1, "-", opciones[x])

opcion = input("\nIngrese la opción que desea realizar: ")

while(not flag_salir):
    tipo_posicion = []
    nombre = ""
    tipo = ""
    valor = 0
    flag_opcion = False
    
    # Validación de opción válida
    while(not flag_opcion):

        if(opcion.isdecimal()): 
            if(int(opcion) > 0 and int(opcion) <= len(opciones)):
                flag_opcion = True

            else:
                print("\n====== ADVERTENCIA ======\n")
                print("Las opciones válidas se númeran desde el 1 hasta el", len(opciones))
                print("\n====== ADVERTENCIA ======\n")

        else:
            print("\n====== ADVERTENCIA ======\n")
            print("Recuerde ingresar el número de la opción")
            print("\n====== ADVERTENCIA ======\n")

        # Se mostrará el mensaje y las opciones, solo si no ingresa una opción válida
        if(not flag_opcion): 
            print("\nOpciones válidas: \n")

            for x in range(len(opciones)):
                print(x + 1, "-", opciones[x])

            opcion = input("\nIngrese la opción que desea realizar: ")

    if(opcion == "1"):
        decision = ""
        flag_parar_carga = False

        while(not flag_parar_carga):
            plato = []
            flag_tipo = False
            flag_valor = False

            # TODO: ¿Es necesario validación del nombre del plato ingresado?
            nombre = input("\nIngrese el nombre del plato: ")

            print("\nLos tipos válidos de platos son: ")
            for x in range(len(tipos)):
                print(" - ".join(tipos[x]))

            tipo = input("\nIngrese el tipo del plato: ").upper()

            # Validación de tipo ingresado, sólo admite las letras de las opciones
            while(not flag_tipo):

                if(tipo.isalpha()):
                    # [i[0] for i in tipos] --> Devuelve una lista, acorde a la columna deseada, en este caso, la primera
                    #                           que es donde se encuentran las letras de los tipos
                    if(tipo in [fila[0] for fila in tipos]):
                        for y in range(len(tipos)):
                            for x in range(len(tipos[y])):
                                if(tipos[y][x] == tipo):
                                    tipo_posicion.append(y)
                                    tipo_posicion.append(x + 1) # Se suma 1, para recuperar la descripción del tipo

                        flag_tipo = True

                    else:
                        print("\n====== ADVERTENCIA ======\n")
                        print("Recuerde ingresar la letra de la opción")
                        print("\n====== ADVERTENCIA ======\n")

                else:
                    print("\n====== ADVERTENCIA ======\n")
                    print("Recuerde no ingresar números")
                    print("\n====== ADVERTENCIA ======\n")

                # Se mostrará el mensaje y las opciones, solo si no ingresa una un tipo válido
                if(not flag_tipo):
                    print("\nLos tipos válidos de platos son: ")
                    for x in range(len(tipos)):
                        print(" - ".join(tipos[x]))

                    tipo = input("\nIngrese el tipo del plato: ").upper()
            
            valor = input("\nIngrese el valor del plato: ")

            # Validación de valor ingresado, admite centavos con ',' ó '.'
            while(not flag_valor):
                if(valor.replace(',', '', 1).isdigit() or valor.replace('.', '', 1).isdigit()):
                    valor = float(valor.replace(',', '.'))

                    if(valor > 0):
                        flag_valor = True

                    else:
                        print("\n====== ADVERTENCIA ======\n")
                        print("Recuerde ingresar un valor mayor a 0")
                        print("\n====== ADVERTENCIA ======\n")

                else:
                    print("\n====== ADVERTENCIA ======\n")
                    print("Recuerde ingresar números únicamente, pueden tener coma/punto")
                    print("\n====== ADVERTENCIA ======\n")                

                # Se mostrará el mensaje, solo si no ingresa una valor válido
                if(not flag_valor):
                    valor = input("\nIngrese el valor del plato: ")        

            plato.append(nombre)
            plato.append(tipo)
            plato.append(valor)

            platos.append(plato)

            print("\n¡Se ha ingresado exitosamente el plato \"{0}\", el cual es un/a \"{1}\", por un valor de ${2}\n"
                .format(
                    nombre.capitalize(),
                    tipos[tipo_posicion[0]][tipo_posicion[1]],
                    round(valor, 2)
                )
            )

            decision = input("\n¿Desea seguir ingresando platos?: ").upper()

            # TODO: ¿Es necesario crear otro flag y otro bucle "while", hasta que se ingrese una decision válida?
            if(decision not in ["SI", "S", "YES", "Y"]): flag_parar_carga = True

    elif(opcion == "2"):
        # Está condición valida si la lista platos, está vacía
        if(not platos):
            print("\n====== ADVERTENCIA ======\n")
            print("Aún no se ha ingresado ningún plato al menú")
            print("\n====== ADVERTENCIA ======\n")

        else:
            pedido = []
            indice_platos = []
            flag_parar_carga = False
            importe_total = 0
            opcion_plato = ""
            decision = ""

            while(not flag_parar_carga):
                flag_opcion_plato = False

                print("\nMenú: \n")

                for plato in range(len(platos)):
                    tipo = ""
                    tipo_posicion = []

                    tipo = platos[plato][1] # En la subposicion 1, está el tipo en los platos

                    for y in range(len(tipos)):
                        for x in range(len(tipos[y])):
                            if(tipos[y][x] == tipo):
                                tipo_posicion.append(y)
                                tipo_posicion.append(x + 1) # Se suma 1, para recuperar la descripción del tipo

                    print("{0} - {1}, es un plato de tipo {2}, con un valor de ${3}"
                        .format(
                            plato + 1,
                            platos[plato][0],
                            tipos[tipo_posicion[0]][tipo_posicion[1]],
                            platos[plato][2]
                        )
                    )

                print("\nCarga de pedido\n")
                opcion_plato = input("Ingrese el plato que desea pedir: ")                

                # Validación de opción de plato válida
                while(not flag_opcion_plato):
                    if(opcion_plato.isdecimal()): 
                        opcion_plato = int(opcion_plato)

                        if(opcion_plato > 0 and opcion_plato <= len(platos)):
                            opcion_plato -= 1
                            flag_opcion_plato = True
                        else:
                            print("\n====== ADVERTENCIA ======\n")
                            print("Las opciones válidas se númeran desde el 1 hasta el", len(platos))
                            print("\n====== ADVERTENCIA ======\n")
                    else:
                        print("\n====== ADVERTENCIA ======\n")
                        print("Recuerde ingresar el número de la opción del plato")
                        print("\n====== ADVERTENCIA ======\n")

                    # Se mostrará el mensaje y el menú con los platos, solo si no ingresa una opción de plato válida
                    if(not flag_opcion_plato): 
                        print("\nMenú: \n")

                        for plato in range(len(platos)):
                            tipo = ""
                            tipo_posicion = []

                            tipo = platos[plato][1] # En la subposicion 1, está el tipo en los platos

                            for y in range(len(tipos)):
                                for x in range(len(tipos[y])):
                                    if(tipos[y][x] == tipo):
                                        tipo_posicion.append(y)
                                        tipo_posicion.append(x + 1) # Se suma 1, para recuperar la descripción del tipo

                            print("{0} - {1}, es un plato de tipo {2}, con un valor de ${3}"
                                .format(
                                    plato + 1,
                                    platos[plato][0],
                                    tipos[tipo_posicion[0]][tipo_posicion[1]],
                                    platos[plato][2]
                                )
                            )

                        print("\nCarga de pedido")
                        opcion_plato = input("Ingrese el plato que desea pedir: ")
                
                indice_platos.append(opcion_plato)
                importe_total += platos[opcion_plato][2]

                decision = input("¿Desea seguir agregando platos a su pedido?: ").upper()

                # TODO: ¿Es necesario crear otro flag y otro bucle "while", hasta que se ingrese una decision válida?
                if(decision not in ["SI", "S", "YES", "Y"]): flag_parar_carga = True                

            pedido.append(indice_platos)
            pedido.append(importe_total)

            pedidos.append(pedido)

    elif(opcion == "3"):
        flag_subopcion = False
        subopcion = ""

        print("\nSubopciones válidas: \n")

        for x in range(len(subopciones)):
            print(x + 1, "-", subopciones[x])

        subopcion = input("\nIngrese la subopción que desea realizar: ")

        # Validación de subopción válida
        while(not flag_subopcion):
            if(subopcion.isdecimal()): 
                if(int(subopcion) > 0 and int(subopcion) <= len(subopciones)):
                    flag_subopcion = True
                else:
                    print("\n====== ADVERTENCIA ======\n")
                    print("Las opciones válidas se númeran desde el 1 hasta el", len(subopciones))
                    print("\n====== ADVERTENCIA ======\n")
            else:
                print("\n====== ADVERTENCIA ======\n")
                print("Recuerde ingresar el número de la subopción")
                print("\n====== ADVERTENCIA ======\n")

            # Se mostrará el mensaje y las opciones, solo si no ingresa una opción válida
            if(not flag_subopcion): 
                print("\nSubopciones válidas: \n")

                for x in range(len(subopciones)):
                    print(x + 1, "-", subopciones[x])

                subopcion = input("\nIngrese la subopción que desea realizar: ")

        if(subopcion == "1" or subopcion == "2"):
            if(not pedidos):
                print("\n====== ADVERTENCIA ======\n")
                print("Aún no se ha ingresado ningún pedido")
                print("\n====== ADVERTENCIA ======\n")
            elif(subopcion == "1"):
                flag_opcion_plato = False
                opcion_plato = ""
                acumulador_plato = 0

                for plato in range(len(platos)):
                    tipo = ""
                    tipo_posicion = []

                    tipo = platos[plato][1] # En la subposicion 1, está el tipo en los platos

                    print()

                    for y in range(len(tipos)):
                        for x in range(len(tipos[y])):
                            if(tipos[y][x] == tipo):
                                tipo_posicion.append(y)
                                tipo_posicion.append(x + 1) # Se suma 1, para recuperar la descripción del tipo

                    print("{0} - {1}"
                        .format(
                            plato + 1,
                            platos[plato][0],
                        )
                    )

                opcion_plato = input("\nIngrese la opción del plato, del cual quiere emitir el reporte: ")

                # Validación de opción de plato válida
                while(not flag_opcion_plato):
                    if(opcion_plato.isdecimal()): 
                        opcion_plato = int(opcion_plato)

                        if(opcion_plato > 0 and opcion_plato <= len(platos)):
                            opcion_plato -= 1
                            flag_opcion_plato = True
                        else:
                            print("\n====== ADVERTENCIA ======\n")
                            print("Las opciones válidas se númeran desde el 1 hasta el", len(platos))
                            print("\n====== ADVERTENCIA ======\n")
                    else:
                        print("\n====== ADVERTENCIA ======\n")
                        print("Recuerde ingresar el número de la opción del plato")
                        print("\n====== ADVERTENCIA ======\n")

                    # Se mostrará el mensaje y el menú con los platos, solo si no ingresa una opción de plato válida
                    if(not flag_opcion_plato): 
                        for plato in range(len(platos)):
                            tipo = ""
                            tipo_posicion = []

                            tipo = platos[plato][1] # En la subposicion 1, está el tipo en los platos

                            for y in range(len(tipos)):
                                for x in range(len(tipos[y])):
                                    if(tipos[y][x] == tipo):
                                        tipo_posicion.append(y)
                                        tipo_posicion.append(x + 1) # Se suma 1, para recuperar la descripción del tipo

                            print("{0} - {1}"
                                .format(
                                    plato + 1,
                                    platos[plato][0],
                                )
                            )

                        opcion_plato = input("\nIngrese la opción del plato, del cual quiere emitir el reporte: ")     

                for pedido in range(len(pedidos)):
                    # Solo itero la lista con indices, dentro de cada pedido
                    for indices in range(len(pedidos[pedido]) - 1):
                        for indice in range(len(pedidos[pedido][indices])):
                            if(indice == opcion_plato):
                                acumulador_plato += platos[opcion_plato][2]

                print("\nSe facturó ${0} del plato \"{1}\""
                    .format(
                        acumulador_plato,
                        platos[opcion_plato][0]
                    )
                )

            elif(subopcion == "2"):
                indices_platos_por_tipo = []
                indices_platos_por_tipo_unico = []
                cantPlatos = [] # Guarda relación con indices_platos_por_tipo_unico

                 # Busco el código del tipo, en cada tipo
                for itemTipo in range(len(tipos)):
                    indices = []

                    for codigo in range(len(tipos[itemTipo]) - 1):
                        for plato in range(len(platos)):
                            if tipos[itemTipo][codigo] == platos[plato][1]:
                                indices.append(plato)
                    
                    indices_platos_por_tipo.append(indices)

                # Itera la lista indices_platos_por_tipo, y obtiene los valores únicos de cada lista contenida
                for x in range(len(indices_platos_por_tipo)):
                    indice_platos = []
                    
                    for indice in indices_platos_por_tipo[x]:
                        if indice not in indice_platos:
                            indice_platos.append(indice)
                        
                    indices_platos_por_tipo_unico.append(indice_platos)

                # Itera cada uno de los tipos y pedidos, y va acumulando las coincidencias con el indices_platos_por_tipo_unico
                for x in range(len(indices_platos_por_tipo_unico)):
                    cant_platos_tipo = []

                    for y in range(len(indices_platos_por_tipo_unico[x])):
                        contador = 0

                        for pedido in range(len(pedidos)):
                            for indices in range(len(pedidos[pedido]) - 1):
                                contador += pedidos[pedido][indices].count(indices_platos_por_tipo_unico[x][y])

                        cant_platos_tipo.append(contador)

                    cantPlatos.append(cant_platos_tipo)

                print()

                for x in range(len(cantPlatos)):
                    maximo_indice = cantPlatos[x].index(max(cantPlatos[x]))
                    maximo_valor = max(cantPlatos[x])

                    print("El plato \"{0}\", es el tipo {1} más pedido, con una cantidad de {2}"
                        .format(
                            platos[indices_platos_por_tipo_unico[x][maximo_indice]][0],
                            tipos[x][1],
                            maximo_valor
                        )
                    )
            
        elif(subopcion == "3"):
            indice_pedidos_entradas = []
            cant_pedidos_entradas = []

            for pedido in range(len(pedidos)):
                contador_entrada = 0

                for indices in range(len(pedidos[pedido]) - 1):
                    for indicePlato in pedidos[pedido][indices]:
                        if(platos[indicePlato][1] == "E"):
                            contador_entrada += 1

                if(contador_entrada >= 2):
                    indice_pedidos_entradas.append(pedido)
                    cant_pedidos_entradas.append(contador_entrada)

            if(not cant_pedidos_entradas):
                print("\nNo hay ningún pedido con más de 2 entradas\n")
            else:
                print()

                for indice in range(len(indice_pedidos_entradas)):
                    print("En el pedido N° {0} se ha solicitado {1} entradas"
                        .format(
                            indice_pedidos_entradas[indice] + 1,
                            cant_pedidos_entradas[indice]
                        )
                    )  

    # Se mostrará el mensaje y las opciones, sólo si no elige la opción de salir
    if(opcion == "4"): 
        flag_salir = True
    else:
        print("\nOpciones válidas: \n")

        for x in range(len(opciones)):
            print(x + 1, "-", opciones[x])

        opcion = input("\nIngrese otra opción que desee realizar: ")
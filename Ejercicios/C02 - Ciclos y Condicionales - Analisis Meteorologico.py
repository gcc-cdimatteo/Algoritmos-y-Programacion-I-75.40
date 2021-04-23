'''
Se ingresan las 30 temperaturas de los 12 meses del año y se desea saber cual fue el mes de mayor temperatura promedio.
(Si, se supone que todos los meses tienen 30 días para simplificar el ejercicio)
(Para simplificar supongamos 5 meses del año de 3 días cada uno)
'''
CANT_DIAS = 3
CANT_MESES = 5

tempTotalMes1 = 0.0
tempTotalMes2 = 0.0
tempTotalMes3 = 0.0
tempTotalMes4 = 0.0
tempTotalMes5 = 0.0
promedioMes1 = 0.0
promedioMes2 = 0.0
promedioMes3 = 0.0
promedioMes4 = 0.0
promedioMes5 = 0.0
temperatura = ""


for mes in range(CANT_MESES):
    if(mes == 0):
        print("\nEnero\n")
        
        for dia in range(CANT_DIAS):
            temperatura = input(f"Ingrese la temperatura del día {dia + 1}: ")
            tempTotalMes1 += float(temperatura)

        promedioMes1 = tempTotalMes1 / CANT_DIAS

        print("Enero: {0:.{1}f}°C".format(promedioMes1, 1))
    
    elif(mes == 1):
        print("\nFebrero\n")

        for dia in range(CANT_DIAS):
            temperatura = input(f"Ingrese la temperatura del día {dia + 1}: ")
            tempTotalMes2 += float(temperatura)

        promedioMes2 = tempTotalMes2 / CANT_DIAS

        print("Febrero: {0:.{1}f}°C".format(promedioMes2, 1))

    elif(mes == 2):
        print("\nMarzo\n")

        for dia in range(CANT_DIAS):
            temperatura = input(f"Ingrese la temperatura del día {dia + 1}: ")
            tempTotalMes3 += float(temperatura)

        promedioMes3 = tempTotalMes3 / CANT_DIAS

        print("Marzo: {0:.{1}f}°C".format(promedioMes3, 1))

    elif(mes == 3):
        print("\nAbril\n")

        for dia in range(CANT_DIAS):
            temperatura = input(f"Ingrese la temperatura del día {dia + 1}: ")
            tempTotalMes4 += float(temperatura)

        promedioMes4 = tempTotalMes4 / CANT_DIAS

        print("Abril: {0:.{1}f}°C".format(promedioMes4, 1))
            
    else:
        print("\nMayo\n")

        for dia in range(CANT_DIAS):
            temperatura = input(f"Ingrese la temperatura del día {dia + 1}: ")
            tempTotalMes5 += float(temperatura)

        promedioMes5 = tempTotalMes5 / CANT_DIAS

        print("Mayo: {0:.{1}f}°C".format(promedioMes5, 1))


if promedioMes1 > promedioMes2:

    if promedioMes1 > promedioMes3:

        if promedioMes1 > promedioMes4:

            if promedioMes1 > promedioMes5:
                print("\nEl mes de Enero, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                    .format(
                        promedioMes1, 1
                    )
                )                

            else:
                print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                    .format(
                        promedioMes5, 1
                    )
                )   
                
        elif promedioMes4 > promedioMes5:
            print("\nEl mes de Abril, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes4, 1
                )
            )

        else:
            print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes5, 1
                )
            )            

    elif promedioMes3 > promedioMes4:

        if promedioMes3 > promedioMes5:
            print("\nEl mes de Marzo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes3, 1
                )
            )

        else:
            print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes5, 1
                )
            )

    elif promedioMes4 > promedioMes5:
        print("\nEl mes de Abril, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes4, 1
            )
        )
    
    else:
        print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes5,1 
            )
        )

elif promedioMes2 > promedioMes3:

    if promedioMes2 > promedioMes4:

        if promedioMes2 > promedioMes5:
            print("\nEl mes de Febrero, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes2, 1
                )
            )

        else:
            print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
                .format(
                    promedioMes5, 1
                )
            )

    elif promedioMes4 > promedioMes5:
        print("\nEl mes de Abril, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes4, 1
            )
        )

    else:
        print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes5, 1
            )
        )

elif promedioMes3 > promedioMes4:

    if promedioMes3 > promedioMes5:
        print("\nEl mes de Marzo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes3, 1
            )
        )

    else:
        print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
            .format(
                promedioMes5, 1
            )
        )

elif promedioMes4 > promedioMes5:
    print("\nEl mes de Abril, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
        .format(
            promedioMes4, 1
        )
    )

elif promedioMes5 > promedioMes4:
    print("\nEl mes de Mayo, fue el mes con mayor temperatura promedio, con un promedio de {0:.{1}f}°C"
        .format(
            promedioMes5, 1
        )
    )

else:
    print("Todos los meses tienen el mismo promedio de temperatura")
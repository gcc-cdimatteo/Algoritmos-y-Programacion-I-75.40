def serie_collatz(semilla,lista=[]): #Recibe una lista como segundo parametro y de solo recibir un parametro la lista la predefino como una lista vacia

	lista.append(semilla) #En cada vuelta agrego el valor de la semilla actual

	if semilla==1: #Condicion de corte

		return 
	
	elif semilla%2==0:

		semilla=semilla//2 #Modifico la semilla a la mitad si es par
		
		serie_collatz(semilla,lista) #Vuelvo a invocar a la funcion pero con la semilla modificada y la lista con semillas (la nueva funcion no va a tener una lista vacia)

	else:

		semilla=semilla*3+1 #Modifico la semilla a la mitad si es impar

		serie_collatz(semilla,lista) #Vuelvo a invocar a la funcion pero con la semilla modificada y la lista con semillas (la nueva funcion no va a tener una lista vacia)


	return lista #Devuelvo la lista con todas las semillas




valor_inicial=31 #Coloco una semilla cualquiera



final=serie_collatz(valor_inicial) #Invoco la funcion con la semilla elegida

print("\nLa serie de numeros es :\n" ,final) #Muestro la serie 

print("\nLargo de la serie: " ,len(final)) #Muestro el largo de la serie

print("\nEl maximo es: ",max(final)) #Muestro el valor maximo alcanzado por la serie

print("\nEl promedio es: ",sum(final)/len(final)) #Muestro el promedio de la serie OBS: sum() suma todos los elementos de una lista OBS_2 len nunca puede ser 0


valores_mayores=[] #Inicializo la lista para guardar los mayores a 23


for valores_de_la_secuencia in final: #Recorro la lista de la serie

	if valores_de_la_secuencia >= 23:

		valores_Mmyores.append(valores_de_la_secuencia) #Agrego a la lista los valores


print("\nLos numeros mayores a 23 son: \n", sorted(valores_mayores)) #Muestro la lista de valores mayores a 23 


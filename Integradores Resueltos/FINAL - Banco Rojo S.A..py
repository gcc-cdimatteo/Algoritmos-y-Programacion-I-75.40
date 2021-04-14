'''
El Banco Rojo S.A. es una entidad financiera regulada bajo la órbita del Banco Central de la República Argentina, este como su contralor, está solicitando el envío de la información correspondiente a los datos financieros de los clientes dados de alta en un período. 
Con el objetivo de dar cumplimiento a dicho requerimiento, se nos está solicitando el diseño de un sistema, que además permita visualizar parte de la información que deben presentar.
El banco nos envía, en archivos de extensión csv los datos correspondientes a sus clientes y las operaciones realizadas por los mismos. El formato de cada uno es:
Clientes.csv
Código de Cliente, Razón Social / Nombre y Apellido, Tipo Persona, Tipo de Identificación, Número de Identificación
Operaciones.csv
Número de Operación, Código de Cliente, Fecha de Realización, Importe
De esta forma, debemos armar un menú que permita al usuario realizar las siguientes actividades:
1) Procesar base de datos recibida (desde el sector de operaciones).
2) Obtener detalle de Personas Físicas que se informarán en el período corriente y no han sido informadas previamente.
3) Obtener detalle de Personas Jurídicas que se informarán en el período corriente y han sido informadas previamente.
4) Obtener informe cuantitativo de la evolución a lo largo de los distintos períodos de las personas informadas (cantidad de altas de personas físicas y jurídicas por período).
5) Emitir el Régimen Informativo (se admiten formatos txt o csv). El mismo debe tener el formato que se detalla a continuación:
Código de Cliente, Tipo de Identificación, Número de Identificación, Total Operado
IMPORTANTE:
Las Personas Físicas (Tipo Persona = 1) que superen un monto total de $10.000 por Tipo de Operación deberán ser informadas.
Las Personas Jurídicas (Tipo Persona = 2) que superen un monto total de $50.000 por Tipo de Operación deberán ser informadas.
El Período Corriente es: 202103.
'''

import csv
import os
import codecs
import datetime

def leer_archivo(nombre_archivo):
	lines = []
	with codecs.open(os.path.dirname(os.path.abspath(__file__))+'/'+nombre_archivo, "r", encoding='utf-8', errors='ignore') as f:
		r = csv.reader(f, delimiter=';', quotechar='|')
		for row in r:
			lines.append(row)
	return lines

def procesar_clientes(clientes):
	cli = {}
	for c in clientes:
		id = c[0]
		razon_social = c[1]
		t_persona = int(c[2])
		t_identificacion = c[3]
		nro_identificacion = c[4]
		cli[id] = {'RAZON_SOCIAL': razon_social, 'T_PERSONA': t_persona, 'T_IDENTIFICACION': t_identificacion, 'N_IDENTIFICACION': nro_identificacion}
	return cli

def procesar_operaciones(operaciones):
	op = {} ## {cliente: {periodo: total_operado}}
	for o in operaciones:
		#id = o[0]
		cliente = o[1]
		periodo = str(o[2].split('/')[2]) + ("00"+str(o[2].split('/')[1]))[-2:]
		monto = int(o[3])
		if cliente not in op: op[cliente] = {}
		if periodo not in op[cliente]: op[cliente][periodo] = 0
		op[cliente][periodo] += monto
	return op

def obtener_informados(clientes, operaciones):
	informados = {}
	for c in clientes:
		for p in operaciones[c]:
			if clientes[c]['T_PERSONA'] == 1 and operaciones[c][p] >= 10000:
				informados

def obtener_informe(clientes, operaciones, tipo_persona, informes_previos, periodo=(str(datetime.datetime.today().year)+("00"+str(datetime.datetime.today().month-1))[-2:])):
	potenciales_informados = set() 
	for c in clientes:
		if (clientes[c]['T_PERSONA'] == tipo_persona) and (periodo in operaciones[c]) and ((tipo_persona == 1 and operaciones[c][periodo] >= 10000) or (tipo_persona == 2 and operaciones[c][periodo] >= 50000)):
			potenciales_informados.add(c)
	informados = set()
	if informes_previos == True:
		for c in potenciales_informados:
			for p in operaciones[c]:
				if (p != periodo) and ((tipo_persona == 1 and operaciones[c][p] >= 10000) or (tipo_persona == 2 and operaciones[c][p] >= 50000)):
					informados.add(c)
	else:
		informados = potenciales_informados
	informe = {}
	for c in informados:
		informe[c] = [clientes[c]['T_IDENTIFICACION'], clientes[c]['N_IDENTIFICACION'], operaciones[c][periodo]]
	obtener_informados(clientes, operaciones)
	return informe

def imprimir_informe(informe):
	print("Durante el periodo solicitado se informaran los clientes: " + informe.keys().join(', '))
	return

def evolucion_cuantitativa(clientes_operaciones):
	return

def imprimir_regimen(informe):
	text = [] ## Código de Cliente, Tipo de Identificación, Número de Identificación, Total Operado
	for c in informe:
		text.append([c]+informe[c])
	with codecs.open(os.path.dirname(os.path.abspath(__file__))+'/'+'Regimen_Informativo.csv', "w", encoding='utf-8', errors='ignore') as f:
		w = csv.writer(f)
		w.writerows(text)
	return

def main():
	salir = False
	while not salir:
		print("MENU")
		print("1 - Procesar Base de Datos Recibida")
		print("2 - Obtener detalle de Personas Físicas que se informarán en el período corriente y no han sido informadas previamente")
		print("3 - Obtener detalle de Personas Jurídicas que se informarán en el período corriente y han sido informadas previamente")
		print("4 - Obtener informe cuantitativo de la evolución a lo largo de los distintos períodos de las personas informadas")
		print("5 - Emitir Régimen Informativo")
		opcion = input("Ingrese la opcion a realizar: ")
		while not opcion.isnumeric() or int(opcion) not in range(6):
			opcion = input("Por favor, ingrese una opcion que pertenezca al menú: ")
		opcion = int(opcion)
		if opcion == 1:
			clientes = leer_archivo('FINAL - Banco Rojo S.A. - Clientes.csv')
			clientes = procesar_clientes(clientes)
			operaciones = leer_archivo('FINAL - Banco Rojo S.A. - Operaciones.csv')
			operaciones = procesar_operaciones(operaciones)
		elif opcion == 2:
			imprimir_informe(obtener_informe(clientes, operaciones, 1, False))
		elif opcion == 3:
			imprimir_informe(obtener_informe(clientes, operaciones, 2, True))
		elif opcion == 4:
			evolucion_cuantitativa(clientes_operaciones)
		elif opcion == 5:
			imprimir_regimen(obtener_informe(clientes, operaciones, 1, False))
		elif opcion == 6:
			salir = True
	print("Adios!")

main()
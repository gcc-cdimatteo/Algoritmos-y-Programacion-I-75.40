#Hacer una función que permita leer los mensajes de un usuario dado y escribir en un log
#El archivo de log debe tener padrón y mensaje

def Log(mensaje):
    #escribir en el archivo de log
    with open("archivo.log","a") as ptroArchivo:
        ptroArchivo.write(mensaje+"\n")
def cargaAlumno(lista):
    #Voy a cargar los alumnos y sus notas
    padron = input("Ingrese el padrón")
    alumnoNro = 1
    while(padron!=""):
        nombre = input("Ingrese el nombre del alumno")
        nota = int(input("Ingrese la nota"))
        datos=(padron,nombre,nota)
        lista.append(datos)
        Log("FechayHora: Se cargó el alumno nro:"+ str(alumnoNro))
        padron = input("Ingrese el padrón")
        alumnoNro += 1
    Log("FechayHora: Se terminarón de cargar todos los alumnos")
def main():
    listaAlumnos = []
    Log("2020/12/03 20:26_ Comienza el programa")
    #hago cosas!
    cargaAlumno(listaAlumnos)
    Log("2020/12/03 20:40_ Finaliza el programa")
main()
"""
La facultad de Ingeniería de la Universidad de Buenos Aires nos encarga la confección de un sistema de análisis de los alumnos activos que cursan carreras en dicha casa de estudios.
La información que nos bridan se encuentra en dos archivos. El primero conteniendo información general de cada alumno y el segundo con el detalle de materias y notas de cada uno de los alumnos.

alumnos.csv

Padrón, Nombre, Apellido, Carrera, Año de Ingreso
Ej de una línea de este archivo:
77024, Guido, Costa, Ing. en Informática, 1997

El padrón define unívocamente a un alumno.

materias.csv

Padrón, materia1, nota1, materia2, nota2, materia3, nota3, … , materiaN , notaN
Ej de una línea de este archivo:
77024, 75.40, 9, 62.01, 7, 61.03, 6, 75.12, 4

El programa deberá tener un menú poder cumplir lo siguiente:
a- Procesar información de entrada
b- Determinar la antigüedad promedio por carrera de los alumnos activos indicando la fecha actual
c- Indicar cual es el mejor alumno activo de la facultad (en base a su promedio)
d- Determinar el promedio de materias aprobadas de los alumnos de una carrera que se le solicita al usuario
e- Indicar cual es el departamento con mayor cantidad de materias aprobadas por alumnos (Recordar que el departamento son los primeros dos dígitos de la materia.
Ej: Si un alumno tiene aprobadas N materias del departamento de computación (75) se deben contar esas N).
Aclaración: Recuerde que es un programa, con lo cual deberá tener funciones y programa principal.
"""

import re
import copy

from datetime import date, datetime
from dateutil.relativedelta import relativedelta


OPTIONS = [
    "Procesar información de entrada",
    "Determinar antigüedad promedio por carrera",
    "Indicar mejor alumno activo de la facultad",
    "Determinar promedio de materias aprobadas, de los alumnos de una carrera",
    "Indicar departamento con mayor cantidad de materias aprobadas por alumnos",
    "Salir"
]

STUDENT_HEADERS = ["Padrón", "Nombre", "Apellido", "Carrera", "Año de Ingreso"]

RESUME_HEADERS = ["Padrón", "Materias"]

SUBJECT_HEADERS = ["Materia", "Nota"]

SUBJECTS = {
    "61.03": "Análisis Matemático II A",
    "62.01": "Física I A",
    "75.40": "Algoritmos y Programación I",
    "61.08": "Álgebra II A",
    "62.03": "Física II A",
    "63.01": "Química",
    "75.41": "Algoritmos y Programación II",
    "75.12": "Análisis Numérico I"
}

DEPARTMENTS = {
    75: "Departamento de Computación",
    62: "Departamento de Física",
    61: "Departamento de Matemática",
    63: "Departamento de Química"
}


def read_file(filepath  # type: str
              ):

    # PRE: 'filepath', debe ser una variable de tipo str
    # POST: Devuelve una lista, que representa a las lineas leidas del archivo  
    #       que fue abierto y leido posteriormente

    data = []

    try:
        f = open(filepath, "r", encoding="utf-8")
    except IOError:
        print("\nNo se pudo leer el archivo: ", filepath)
    
    with f:
        data = f.read().splitlines()

    return data


def validate_number(number  # type: str
                    ):

    # PRE: 'number', debe ser una variable de tipo str
    # POST: Devuelve un int o float, que representa al número pasado por 
    #       parámetro, al cual se le ha eliminado los caracteres alfabeticos

    formatted_number = ""
    value = 0

    formatted_number = re.sub("[a-zA-Z]+", "", number)

    try:
        value = int(formatted_number)

    except ValueError:
        value = float(formatted_number)

    return value    


def parse_data_to_student(data  # type: str
                          ):
    
    # PRE: 'data', debe ser una variable de tipo str
    # POST: Devuelve un dict, que representa a la información pasada por 
    #       parámetro y que ha sido parseada al modelo 'student'

    # student = { 
    #   'Padrón': int, 'Nombre': str, "Apellido": str,
    #   'Carrera': str, "Año de Ingreso": int    
    # }

    formatted_data = []
    student = {}

    formatted_data = re.split("\,\s*|\,", data)

    for x in range(len(STUDENT_HEADERS)):

        if (STUDENT_HEADERS[x] == "Padrón" or STUDENT_HEADERS[x] == "Año de Ingreso"):
            student[STUDENT_HEADERS[x]] = validate_number(formatted_data[x])

        else:
            student[STUDENT_HEADERS[x]] = formatted_data[x]        

    return student


def parse_data_to_subjects(data  # type: list[str]
                           ):

    # PRE: 'data', debe ser una variable de tipo list
    # POST: Devuelve una lista de dicts, que representa a la información 
    #       pasada por parámetro y que ha sido parseada al modelo 'subject'

    # subject = { 'Materia': str, 'Nota': int }

    subjects = []
    qty_subjs = 0

    qty_subjs = len(data) // 2

    for x in range(qty_subjs):
        subject = {}

        subject[SUBJECT_HEADERS[0]] = data[x * 2]
        subject[SUBJECT_HEADERS[1]] = validate_number(data[x * 2 + 1])

        subjects.append(subject)

    return subjects
        

def parse_data_to_resume(data  # type: str
                         ):
    
    # PRE: 'data', debe ser una variable de tipo str
    # POST: Devuelve un dict, que representa a la información pasada por 
    #       por parámetro y que ha sido parseada al modelo 'resume'

    # resume = { 'Padrón': int, 'Materias': list[subject] }

    formatted_data = []
    resume = {}

    formatted_data = re.split("\,\s*|\,", data)

    for x in range(len(RESUME_HEADERS)):

        if(RESUME_HEADERS[x] == "Padrón"):
            resume[RESUME_HEADERS[x]] = validate_number(formatted_data[x])

        else:
            formatted_data.pop(x - 1)

            resume[RESUME_HEADERS[x]] = parse_data_to_subjects(formatted_data)

    return resume    


def filter_unique_values(data,  # type: list[dict]
                         key  # type: str
                         ):
    
    # PRE: 'data', debe ser una variable de tipo list
    #      'key', debe ser una variable de tipo str
    # POST: Devuelve una lista de str, que representa a la información 
    #       pasada por parámetro y que ha sido filtrada de modo que 
    #       queden únicamente los 'values' de dicha 'key'

    filtered_data = []

    filtered_data = list({v[key]:v for v in data})

    return filtered_data


def validate_date(input_date  # type: str
                  ):

    # PRE: 'input_date', debe ser una variable de tipo str
    # POST: Devuelve un boolean, que representa a si la fecha pasada 
    #       por parámetro, tiene un formato válido, existe y se trata  
    #       de la misma fecha de hoy.

    matched_date = []
    tot_diff_in_days = 0
    flag_valid_date = False

    # Regex para validar una fecha de tipo 'dd/mm/yyyy'
    pattern = re.compile("^(((0)[0-9])|((1)[0-2]))(\/)([0-2][0-9]|(3)[0-1])(\/)\d{4}$")

    matched_date = re.findall(pattern, input_date)

    if len(matched_date) != 0:

        # Ésta función, permite obtener la diferencia entre una fecha de
        # de inicio, y una fecha de final. De dicha diferencia, se obtienen
        # los días
        tot_diff_in_days += relativedelta(
            date.today(), 
            datetime.strptime(input_date, "%d/%m/%Y")
        ).days

        if tot_diff_in_days == 0:
            flag_valid_date = True
        
        else:
            print(f"\n¡Sólo puedes ingresar la fecha del día de hoy!")

    else:
        print(f"\n¡Sólo puedes ingresar fechas con el formato 'dd/mm/yyyy' y que existan!")

    return flag_valid_date    


def validate_input_date():

    # POST: Devuelve un str, que representa a la entrada hecha por el  
    #       usuario, de una fecha, a la cual se la valida  

    input_date = ""
    flag_valid_date = False

    input_date = input("\nIngrese la fecha del día de hoy en formato 'dd/mm/yyyy': ")

    while flag_valid_date:
        flag_valid_date = validate_date(input_date) 

    return input_date


def calculate_seniority_average(degree,  # type: str
                                input_date,  # type: str
                                students  # type: list[dict]
                                ):

    # PRE: 'degree', debe ser una variable de tipo str
    #      'input_date', debe ser una variable de tipo str
    #      'students', debe ser una variable de tipo list
    # POST: Devuelve un int, que representa al promedio de antigüedad
    #       de los alumnos de una carrera

    snr_avg = 0
    qty_students = 0
    tot_diff_in_years = 0

    for student in students:

        if student.get("Carrera") == degree:
            tot_diff_in_years += relativedelta(
                datetime.strptime(input_date, "%d/%m/%Y"), 
                datetime(student.get("Año de Ingreso"), 4, 5)
            ).years

            qty_students += 1

    snr_avg = round(tot_diff_in_years / qty_students, 2)

    return snr_avg


def calculate_calification_average(subjects  # type: list[dict]
                                   ):

    # PRE: 'subjects', debe ser una variable de tipo list
    # POST: Devuelve un float, que representa al promedio de las 
    #       calificaciones de las materias

    calification_avg = 0
    qty_subjects = 0
    tot_califications = 0

    qty_subjects = len(subjects)

    for subject in subjects:
        tot_califications += subject.get("Nota")

    calification_avg = round(tot_califications / qty_subjects, 2)

    return calification_avg


def validate_option(option,  # type: str
                    options  # type: list[str]
                    ):

    # PRE: 'option', debe ser una variable de tipo str
    #      'options', debe ser una variable de tipo list
    # POST: Devuelve un boolean, que representa a si la opcion pasada 
    #       por parámetro, es un número y si se encuentra dentro del 
    #       rango de las posibles opciones a elegir

    option_number = 0
    flag_valid_option = False

    if option.isnumeric():
        option_number = int(option)

        if option_number > 0 and option_number <= len(options):
            flag_valid_option = True

        else:
            print(f"\n¡Sólo puedes ingresar una opción entre el 1 y el {len(options)}!")

    else:
        print(f"\n¡Las opciones son numeros enteros, sin decimales!")

    return flag_valid_option


def validate_input_option():

    # POST: Devuelve un int, que representa a la entrada hecha por el  
    #       usuario, de una opcion, a la cual se la valida  

    input_option = ""
    number = 0
    flag_valid_option = False

    input_option = input("\nIngrese una opción: ")

    while not flag_valid_option:
        try:
            number = validate_number(input_option)

            flag_valid_option = validate_option(input_option, OPTIONS) 

        except ValueError:
            print("\n¡Sólo se pueden ingresar numeros!")

    return number


def get_user_input(options  # type: list[str]
                   ):

    # PRE: 'options', debe ser una variable de tipo list
    # POST: Devuelve un int, que representa a la entrada hecha por el  
    #       usuario, de una opcion, a la cual se la valida

    option = 0

    print("\nOpciones válidas: \n")

    for x in range(len(options)):
        print(x + 1, "-", options[x])

    option = validate_input_option()

    return option


def process_input_information():

    # POST: Devuelve dos listas de dicts, que representa a la 
    #       información procesada de los archivos 'alumnos.csv' y  
    #       'materias.csv'

    students_data = []
    resumes_data = []
    students = []
    resumes = []

    students_data = read_file("2020C2F1-20210309-alumnos.csv")
    resumes_data = read_file("2020C2F1-20210309-materias.csv")

    for x in range(len(students_data)):

        students.append(
            parse_data_to_student(students_data[x])
        )

    for x in range(len(resumes_data)):

        resumes.append(
            parse_data_to_resume(resumes_data[x])
        )

    return students, resumes


def print_seniority_averages(students  # type: list[dict]
                             ):

    # PRE: 'students', debe ser una variable de tipo list
    # POST: Imprime los promedios de antigüedad, por carrera,
    #       de los alumnos

    degrees = []
    snr_avgs = []
    input_date = ""

    degrees = filter_unique_values(students, "Carrera")

    input_date = validate_input_date()

    for degree in degrees:
        
        snr_avgs.append(
            calculate_seniority_average(degree, input_date, students)
        )

    for x in range(len(degrees)):
        print("\nLa carrera de '{0}', tiene un promedio de alumnos activos de {1}"
            .format(
                degrees[x],
                snr_avgs[x]
            )
        )


def print_best_active_student(resumes,  # type: list[dict]
                              students  # type: list[dict]
                              ):

    # PRE: 'resume', debe ser una variable de tipo list
    #      'students', deber ser una variable de tipo list
    # POST: Imprime el alumno más activo, de acuerdo a su 
    #       promedio de materias

    calification_avg = 0
    completed_resumes = []
    max_avg_resume = {}
    max_avg_student = {}

    completed_resumes = copy.deepcopy(resumes)

    for resume in completed_resumes:
        calification_avg = calculate_calification_average(resume.get("Materias"))

        resume["Promedio total de materias"] = calification_avg

    max_avg_resume = max(completed_resumes, key=lambda x:x["Promedio total de materias"])
    max_avg_student = next(student for student in students if student["Padrón"] == max_avg_resume.get("Padrón"))

    print("\nEl mejor alumno activo es {0} {1}, que cuenta con un promedio de {2}"
        .format(
            max_avg_student.get("Nombre"),
            max_avg_student.get("Apellido"),
            max_avg_resume.get("Promedio total de materias")
        )
    )


def filter_by_degree(students,  # type: list[dict]
                     degree  # type: str
                     ):

    filtered_students = []

    for x in range(len(students)):

        if students[x].get("Carrera") == degree:
            filtered_students.append(students[x])

    return filtered_students


def filter_by_department(subjects,  # type: list[dict]
                         department_code  # type: int
                         ):

    filtered_subjects = []
    matched_department = []

    for subject in subjects:
        pattern = re.compile("^" + str(department_code) + "{1}")
        matched_department = re.findall(pattern, subject.get("Materia"))

        if len(matched_department) != 0:
            filtered_subjects.append(
                {"Materia": subject.get("Materia")}
            )

    return filtered_subjects


def filter_by_subject(subjects,  # type: list[dict]
                      subject_code  # type: str
                      ):

    filtered_subjects = []
    matched_subject = []

    for subject in subjects:
        pattern = re.compile(f"^{subject_code}")
        matched_subject = re.findall(pattern, subject.get("Materia"))

        if len(matched_subject) != 0:
            filtered_subjects.append(subject)

    return filtered_subjects    


def count_approved_subjects(subjects  # type: list[dict]
                            ):

    qty_appr_subjs = 0

    for subject in subjects:
        if subject.get("Nota") >= 4:
            qty_appr_subjs += 1

    return qty_appr_subjs


def accumulate_notes(subjects  # type: list[dict]
                     ):

    tot_califications = 0

    for subject in subjects:
        tot_califications += subject.get("Nota")

    return tot_califications


def calculate_approved_subjects_average(students_id,  # type: list[int]
                                        resumes  # type: list[dict]
                                        ):

    appr_subjs_avg = 0
    qty_appr_subjs = 0
    tot_califications = 0

    for student_id in students_id:
        for resume in resumes:

            if student_id == resume.get("Padrón"):
                qty_appr_subjs += count_approved_subjects(resume.get("Materias"))
                tot_califications += accumulate_notes(resume.get("Materias"))

    appr_subjs_avg = round(tot_califications / qty_appr_subjs, 2)

    return appr_subjs_avg


def print_average_approved_subjects(students,  # type: list[dict]
                                    resumes  # type: list[dict]
                                    ):

    degrees = []
    filtered_students = []
    students_id = []
    option = 0
    appr_subjs_avg = 0

    degrees = filter_unique_values(students, "Carrera")

    option = get_user_input(degrees) - 1

    filtered_students = filter_by_degree(students, degrees[option])

    students_id = filter_unique_values(filtered_students, "Padrón")

    appr_subjs_avg = calculate_approved_subjects_average(students_id, resumes)

    print("\nEl promedio de materias aprobadas de la carrera '{0}', con una cantidad de alumnos de {1}, es de {2}"
        .format(
            degrees[option],
            len(students_id),
            appr_subjs_avg
        )
    )


def get_departments(resumes  # type: list[dict]
                    ):

    resumes_copy = []
    subjects = []
    list_departments = []
    departments = []

    resumes_copy = copy.deepcopy(resumes)

    for resume in resumes_copy:
        for materia in resume.get("Materias"):
            materia["Departamento"] = validate_number(
                materia.get("Materia").split(".")[0]
            )

            subjects.append(materia)

    list_departments = filter_unique_values(subjects, "Departamento")

    departments = [{"Departamento": list_departments[x]} for x in range(len(list_departments))]

    return departments


def print_best_department(resumes  # type: list[dict]
                          ):

    departments = []

    departments = get_departments(resumes)

    for department in departments:
        dept_subjs = []

        for resume in resumes:
            dept_subjs += filter_by_department(
                resume.get("Materias"), 
                department.get("Departamento")
            )

        department["Materias"] = filter_unique_values(dept_subjs, "Materia")

    for department in departments:
        filtered_subjs = []

        for subject in department.get("Materias"):
            for resume in resumes:
                filtered_subjs += filter_by_subject(resume.get("Materias"), subject)

        department["Cant. materias aprobadas por alumnos"] = count_approved_subjects(filtered_subjs)

    max_qty_approv_subjc_department = max(departments, key=lambda x:x["Cant. materias aprobadas por alumnos"])

    print("\nEl '{0}', es el departamento con mayor cantidad de materias aprobadas por alumnos, con una cantidad de {1} materias aprobadas"
        .format(
            DEPARTMENTS.get(
                max_qty_approv_subjc_department.get("Departamento")
            ),
            max_qty_approv_subjc_department.get("Cant. materias aprobadas por alumnos")
        )
    )


def main():
    students = []
    resumes = []

    option = 0
    flag_is_valid = False

    option = get_user_input(OPTIONS)

    while option != 6:

        if option == 1:
            students, resumes = process_input_information()

            print("\n¡Archivos procesados!")

            flag_is_valid = True

        elif(option == 2 and flag_is_valid):
            print_seniority_averages(students)

        elif(option == 3 and flag_is_valid):
            print_best_active_student(resumes, students)

        elif(option == 4 and flag_is_valid):
            print_average_approved_subjects(students, resumes)

        elif(option == 5 and flag_is_valid):
            print_best_department(resumes)

        else:
            print("\n¡Debes procesar información primero, antes de elegir esa opción!")

        option = get_user_input(OPTIONS)

    print("\nPrograma finalizado")


if __name__ == "__main__":
    main()
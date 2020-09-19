"""
Una facultad tiene un archivo secuencial CSV por cada una de sus 4 Sedes.
Dichos archivos están ordenados en forma ascendente, por Padrón, y contienen la información de las evaluaciones
tomadas en cada una de las 4 sedes.
Los campos son:
padron (numérico), cod_materia (numérico), fecha (AAAAMMDD), calificación (numérico).
Se tiene también en memoria una lista de tuplas con el siguiente formato:
                                   [(cod_materia, nombre_materia),…].
Declarar en el programa, una acorde a los datos contenidos en los archivos.

Se pide:

    Procesar los archivos obteniendo como resultado un único archivo CSV, ordenado
    ascendentemente por Padrón, dónde cada línea esté compuesta por:
    padrón, cod_materia, nombre_materia, fecha, calicacion ; y sólo si la materia fue aprobada por el alumno.

    Informar las 5 materias con menos aprobados, ordenadas ascendentemente por cantidad de aprobados.
"""

materias = [('7540', "computacion"), ('7541', "programacion I"), ('7542', "programacion II"), ('6469', "Analisis I"),
            ('7501', "Algebra I"), ('6103', "Discreta"), ('6105', "Probabilidad"), ('7065', "Programacion III"),
            ('8200', "Contabilidad"), ('8100', "Economia"), ('9100', "Quimica")]

MAX = ['999999999999', 0, 0, 0]

'''# funcion para leer lineas'''


def leer_lineas(archivo):
    linea = archivo.readline()
    return linea.rstrip('\n').split(',') if linea else MAX


'''# funcion para crear el csv ordenado (no retorna nada)'''


def crear_csv_ordenado(padron, cod_materia, nombre_materia, fecha, calicacion):
    with open("total.csv", "a+") as ordenado:
        ordenado.write(str(padron) + ',' + str(cod_materia) + ',' + str(nombre_materia) + ',' + str(fecha) + ',' + str(
            calicacion) + '\n')


''' Prceso los datos'''



'''# crear el merge:'''


def merge():
    sede1 = open("sede1.csv", 'r')
    sede2 = open("sede2.csv", 'r')
    sede3 = open("sede3.csv", 'r')
    sede4 = open("sede4.csv", 'r')

    '''invocando a la funcion para leer la primera linea de cada csv'''
    linea1 = leer_lineas(sede1)
    linea2 = leer_lineas(sede2)
    linea3 = leer_lineas(sede3)
    linea4 = leer_lineas(sede4)

    '''vamos a recorrer las listas creadas anteriormente con la funcion leer_lineas y verificamos que siempre haya una 
    que leer'''
    while linea1[0] != MAX[0] or linea2[0] != MAX[0] or linea3[0] != MAX[0] or linea4[0] != MAX[0]:
        minimo = min(linea1[0], linea2[0], linea3[0], linea4[0])  # sacamos el minimo para ir de manera ordenada

        while linea1[0] == minimo:
            if int(linea1[3]) >= 4:
                i = 0
                while i < len(materias):
                    if materias[i][0] == linea1[1]:
                        padron1 = linea1[0]
                        cod_materia1 = materias[i][0]
                        nombre_materia1 = materias[i][1]
                        fecha1 = linea1[2]
                        calificacion1 = linea1[3]
                        crear_csv_ordenado(padron1, cod_materia1, nombre_materia1, fecha1, calificacion1)
                    i = i + 1
            linea1 = leer_lineas(sede1)  # paso a cargar la proxima linea de ese archivo en memoria para que siga
            # leyendo

        while linea2[0] == minimo:
            if int(linea2[3]) >= 4:
                i = 0
                while i < len(materias):
                    if int(linea2[1]) == materias[i][0]:
                        padron1 = linea2[0]
                        cod_materia1 = materias[i][0]
                        nombre_materia1 = materias[i][1]
                        fecha1 = linea2[2]
                        calificacion1 = linea2[3]
                        crear_csv_ordenado(padron1, cod_materia1, nombre_materia1, fecha1, calificacion1)
                    i = i + 1
            linea2 = leer_lineas(sede2)  # paso a cargar la proxima linea de ese archivo en memoria para que siga
            # leyendo

        while linea3[0] == minimo:
            if int(linea3[3]) >= 4:
                i = 0
                while i < len(materias):
                    if materias[i][0] == int(linea3[1]):
                        padron1 = linea3[0]
                        cod_materia1 = materias[i][0]
                        nombre_materia1 = materias[i][1]
                        fecha1 = linea3[2]
                        calificacion1 = linea3[3]
                        crear_csv_ordenado(padron1, cod_materia1, nombre_materia1, fecha1, calificacion1)
                    i = i + 1
            linea3 = leer_lineas(sede3)  # paso a cargar la proxima linea de ese archivo en memoria para que siga
            # leyendo

        while linea4[0] == minimo:
            if int(linea4[3]) >= 4:
                i = 0
                while i < len(materias):
                    if materias[i][0] == int(linea4[1]):
                        padron1 = linea4[0]
                        cod_materia1 = materias[i][0]
                        nombre_materia1 = materias[i][1]
                        fecha1 = linea4[2]
                        calificacion1 = linea4[3]
                        crear_csv_ordenado(padron1, cod_materia1, nombre_materia1, fecha1, calificacion1)
                    i = i + 1
            linea4 = leer_lineas(sede4)  # paso a cargar la proxima linea de ese archivo en memoria para que siga
            # leyendo



    sede1.close()
    sede2.close()
    sede3.close()
    sede4.close()


def main():
    merge()


main()

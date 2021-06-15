#!/usr/bin/python3

'''Nombre del reto: Clasificación de nódulos tiroideos y acciones a tomar.'''

# Declaracion e inicializacion de variables Globales
overallScore = 0
numPatients = 0
i = 1
benign = 0
noSuspicious = 0
slightlySuspicious = 0
moderatelySuspicious = 0
highlySuspicious = 0
sizeSum = 0
aaf = 0
noAaf = 0
monitoring = 0

# Inicio de funciones


def composicion(codeC):
    ''' Composicion
    SE DEBE ESCOGER SOLO UNO.

    Codigo  Puntaje
    C1          0
    C2          0
    C3          1
    C4          2
    '''
    global overallScore

    if codeC == "C1" or codeC == "C2":
        overallScore += 0
    elif codeC == "C3":
        overallScore += 1
    elif codeC == "C4":
        overallScore += 2


def ecogenicidad(codeE):
    ''' Ecogenicidad
    SE DEBE ESCOGER SOLO UNO
    Codigo  Puntaje
    E1          0
    E2          1
    E3          2
    E4          3
    '''
    global overallScore

    if codeE == "E1":
        overallScore += 0
    elif codeE == "E2":
        overallScore += 1
    elif codeE == "E3":
        overallScore += 2
    elif codeE == "E4":
        overallScore += 3


def forma(codeF):
    ''' Forma
    SE DEBE ESCOGER SOLO UNO.

    Codigo  Puntaje
    F1          0
    F2          3
    '''
    global overallScore

    if codeF == "F1":
        overallScore += 0
    elif codeF == "F2":
        overallScore += 3


def margen(codeM):
    ''' Margen
    SE DEBE ESCOGER SOLO UNO.

    Codigo  Puntaje
    M1          0
    M2          0
    M3          2
    M4          3
    '''
    global overallScore

    if codeM == "M1":
        overallScore += 0
    elif codeM == "M2":
        overallScore += 0
    elif codeM == "M3":
        overallScore += 2
    elif codeM == "M4":
        overallScore += 3


def focosEcogenicos(valueFE):
    ''' Focos ecogenicos
    SE DEBEN SELECCIONAR TODOS LOS QUE APLIQUEN.

    Codigo  Puntaje
    FE1         0
    FE2         1
    FE3         2
    FE4         3
    '''
    global overallScore
    variables = {'FE1': 0, 'FE2': 1, 'FE3': 2, 'FE4': 3}
    i = 0
    for var in variables:
        if valueFE[i] == "1":
            overallScore += variables[var]
        i += 1


def clasificacioNodulos(valueSize):
    ''' Calculado el puntaje almacenado en overallScore,
    esta funcion realiza la clasificacion de los nodulos.
    '''
    global overallScore
    global numPatients
    global i
    global sizeSum
    global aaf
    global noAaf
    global monitoring
    global benign
    global noSuspicious
    global slightlySuspicious
    global moderatelySuspicious
    global highlySuspicious

    sizeSum = sizeSum + valueSize

    # Benigno
    if overallScore >= 0 and overallScore <= 1:
        benign += 1
        noAaf += 1

    # No sospechoso
    elif overallScore == 2:
        noSuspicious += 1
        noAaf += 1

    # Levemente sospechoso
    elif overallScore == 3:
        slightlySuspicious += 1
        if valueSize >= 2.5:
            aaf += 1
        elif valueSize < 2.5:
            monitoring += 1

    # Moderadamente sospechoso
    elif overallScore >= 4 and overallScore <= 6:
        moderatelySuspicious += 1
        if valueSize >= 1.5:
            aaf += 1
        elif valueSize < 1.5:
            monitoring += 1

    # Altamente sospechoso
    elif overallScore >= 7:
        highlySuspicious += 1
        if valueSize >= 1:
            aaf += 1
        elif valueSize < 1:
            monitoring += 1

    # Validacion para impresion final de resultados
    if i == numPatients:
        print(benign, noSuspicious, slightlySuspicious,
              moderatelySuspicious, highlySuspicious)
        print(format((sizeSum/numPatients), '.2f'))
        print(noAaf, monitoring, aaf)


def run():
    '''
        la función inicia el programa y llama a las funciones en orden.
    '''

    global numPatients
    global i

    # Entrada que indiqua el numero de pacientes que se realizaron el test
    numPatients = int(input())

    while i <= numPatients:

        values = input().upper()
        valuesList = values.split(' ')

        # llamada de metodos
        composicion(valuesList[0])
        ecogenicidad(valuesList[1])
        forma(valuesList[2])
        margen(valuesList[3])
        focosEcogenicos(valuesList[4:8])
        clasificacioNodulos(float(valuesList[8]))

        # Variable re-inicializada en cero para nueva validacion de paciente
        overallScore = 0
        i += 1

if __name__ == "__main__":
    run()

#!/usr/bin/python3

'''Nombre del reto: Clasificación de nódulos tiroideos y acciones a tomar.'''

# Declaracion e inicializacion de variables Globales
overallScore = 0
numPatients = 0
showResults = []
results = []
benign = 'Benigno'
noSuspicious = 'No sospechoso'
slightlySuspicious = 'Levemente sospechoso'
moderatelySuspicious = 'Moderadamente sospechoso'
highlySuspicious = 'Altamente sospechoso'
aaf = 'aaf'
noAaf = 'no aaf'
monitoring = 'seguimiento'

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
    alertType = ''
    treatment = ''

    # Benigno
    if overallScore >= 0 and overallScore <= 1:
        alertType = benign
        treatment = noAaf

    # No sospechoso
    elif overallScore == 2:
        alertType = noSuspicious
        treatment = noAaf

    # Levemente sospechoso
    elif overallScore == 3:
        if valueSize >= 2.5:
            alertType = slightlySuspicious
            treatment = aaf
        elif valueSize < 2.5:
            alertType = slightlySuspicious
            treatment = monitoring

    # Moderadamente sospechoso
    elif overallScore >= 4 and overallScore <= 6:
        if valueSize >= 1.5:
            alertType = moderatelySuspicious
            treatment = aaf
        elif valueSize < 1.5:
            alertType = moderatelySuspicious
            treatment = monitoring

    # Altamente sospechoso
    elif overallScore >= 7:
        if valueSize >= 1:
            alertType = highlySuspicious
            treatment = aaf
        elif valueSize < 1:
            alertType = highlySuspicious
            treatment = monitoring

    results.append((alertType, treatment))
    # Validacion para impresion final de resultados
    if len(results) == numPatients:
        for result in results:
            print(result[0], result[1], sep=',')

    remissionType((alertType, treatment))


def remissionType(result):
    '''Funcion que determina numericamente el tipo de especialista dependiendo
    el resultado realizado por la funcion clasificacioNodulos().
    '''
    global numPatients

    if result[0] == benign and result[1] == noAaf:
        showResults.append('NA')
    elif result[0] == noSuspicious and result[1] == noAaf:
        showResults.append('NA')
    elif result[0] == slightlySuspicious:
        if result[1] == monitoring:
            showResults.append(2)
        elif result[1] == aaf:
            showResults.append(3)
    elif result[0] == moderatelySuspicious:
        if result[1] == monitoring:
            showResults.append(3)
        elif result[1] == aaf:
            showResults.append(3)
    elif result[0] == highlySuspicious:
        if result[1] == monitoring:
            showResults.append(3)
        elif result[1] == aaf:
            showResults.append(4)

    # Validacion para impresion final de resultados
    if len(showResults) == numPatients:
        for data in showResults:
            print(data, end=' ')


def run():
    '''La función inicia el programa y llama a las funciones en orden.'''

    global overallScore
    global numPatients
    i = 1

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

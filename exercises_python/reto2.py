#!/usr/bin/python3

'''Nombre del reto: Clasificación de nódulos tiroideos y acciones a tomar.'''

# Declaracion e inicializacion de variables Globales
overallScore = 0
benign = 0
highlySuspicious = 0
numPatients = 0
i = 1
sizeSum = 0
aaf = 0
noAaf = 0
monitoring = 0

# Inicio de funciones
def composicion():
    ''' Composicion
    SE DEBE ESCOGER SOLO UNO
    Codigo  Puntaje 
    C1          0
    C2          0
    C3          1  
    C4          2
    '''
    global overallScore
    code = input().upper()

    if code == "C1" or code == "C2":
        overallScore += 0
    elif code == "C3":
        overallScore += 1
    elif code == "C4":
        overallScore += 2

def ecogenicidad():
    ''' Ecogenicidad
    SE DEBE ESCOGER SOLO UNO
    Codigo  Puntaje
    E1          0
    E2          1
    E3          2
    E4          3
    '''
    global overallScore
    code = input().upper()

    if code == "E1":
        overallScore += 0
    elif code == "E2":
        overallScore += 1
    elif code == "E3":
        overallScore += 2
    elif code == "E4":
        overallScore += 3

def forma():
    ''' Forma
    SE DEBE ESCOGER SOLO UNO
    Codigo  Puntaje
    F1          0
    F2          3
    '''
    global overallScore
    code = input().upper()

    if code == "F1":
        overallScore += 0
    elif code == "F2":
        overallScore += 3

def margen():
    ''' Margen
    SE DEBE ESCOGER SOLO UNO
    Codigo  Puntaje
    M1          0
    M2          0
    M3          2
    M4          3
    '''
    global overallScore
    code = input().upper()

    if code == "M1":
        overallScore += 0
    elif code == "M2":
        overallScore += 0
    elif code == "M3":
        overallScore += 2
    elif code == "M4":
        overallScore += 3

def focosEcogenicos():
    ''' Focos ecogenicos
    SE DEBEN SELECCIONAR TODOS LOS QUE APLIQUEN
    Codigo  Puntaje
    FE1         0
    FE2         1
    FE3         2
    FE4         3
    '''
    global overallScore
    FE1 = 0
    FE2 = 1 
    FE3 = 2 
    FE4 = 3

    for i in range(4):
        var = int(input())  
        if var == 1 and i == 0:
            overallScore += FE1
        elif var == 1 and i == 1:
            overallScore += FE2
        elif var == 1 and i == 2:
            overallScore += FE3
        elif var == 1 and i == 3:
            overallScore += FE4

def clasificacioNodulos():
    ''' Calculado el puntaje almacenado en overallScore,
    esta funcion realiza la clasificacion de los nodulos
    '''
    global overallScore
    global numPatients
    global i
    global benign
    global highlySuspicious
    global sizeSum
    global aaf
    global noAaf
    global monitoring

    size = float(input())
    sizeSum = sizeSum + size

    # Benigno
    if overallScore >= 0 and overallScore <= 1:
        benign += 1
        noAaf += 1

    # No sospechoso
    elif overallScore == 2:
        noAaf += 1

    # Levemente sospechoso
    elif overallScore == 3:
        if size >= 2.5:
            aaf += 1
        elif size < 2.5:
            monitoring += 1

    # Moderadamente sospechoso
    elif overallScore >= 4 and overallScore <= 6: 
        if size >= 1.5:
            aaf += 1
        elif size < 1.5:
            monitoring += 1

    # Altamente sospechoso
    elif overallScore >= 7:
        highlySuspicious += 1
        if size >= 1:
            aaf += 1
        elif size < 1:
            monitoring += 1

    # Validacion para impresion final de resultados
    if i == numPatients:
        print("benigno", benign)
        print("altamente sospechoso", highlySuspicious)
        print(format((sizeSum/numPatients),'.2f'))
        print("no aaf", noAaf)
        print("seguimiento", monitoring)
        print("aaf", aaf)


if __name__ == "__main__":
    # Entrada que indiqua el numero de pacientes que se realizaron el test
    numPatients = int(input())

    while i <= numPatients:
        # llamada de metodos
        composicion()
        ecogenicidad()
        forma()
        margen()
        focosEcogenicos()
        clasificacioNodulos()

        # Variable re-inicializada en cero para nueva validacion de paciente
        overallScore = 0

        # incremento contador del bucle
        i += 1

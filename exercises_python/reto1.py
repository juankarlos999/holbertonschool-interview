#!/usr/bin/python3

'''Nombre del reto: Clasificación de nódulos tiroideos y acciones a tomar.'''

overallScore = 0

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
    else:
        composicion()

    return overallScore

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
    
    return overallScore

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
    
    return overallScore

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
    
    return overallScore

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
    size = float(input())

    if overallScore >= 0 and overallScore <= 1:
        print("Benigno")
        print("no AAF")
    elif overallScore == 2:
        print("No sospechoso")
        print("no AAF")
    elif overallScore == 3:
        print("Levemente sospechoso")
        if size >= 2.50:
            print("AAF")
        elif size < 2.5:
            print('seguimiento')
    elif overallScore >= 4 and overallScore <= 6:
        print("Moderadamente sospechoso")
        if size >= 1.5:
            print("AAF")
        elif size < 1.5:
            print('seguimiento')
    elif overallScore >= 7:
        print("Altamente sospechoso")
        if size >= 1:
            print("AAF")
        elif size < 1:
            print('seguimiento')

composicion()
ecogenicidad()
forma()
margen()
focosEcogenicos()
clasificacioNodulos()

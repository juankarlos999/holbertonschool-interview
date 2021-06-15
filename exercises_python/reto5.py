#!/usr/bin/python3
import csv
import operator

'''Este modulo contiene funciones que leen un archivo (csv) con informacion de
pacientes en diferentes zonas de las capitales del pais los cuales
recibieron la clasificacion de nodulos tiroideos y con base a esta
clasificacion se debe imprimir por pantalla el conteo general por tipo de
alertas y tratamientos.
'''

# Declaracion e inicializacion de variables
benign = 'benigno'
noSuspicious = 'no sospechoso'
slightlySuspicious = 'levemente sospechoso'
moderatelySuspicious = 'moderadamente sospechoso'
highlySuspicious = 'altamente sospechoso'
aaf = 'aaf'
noAaf = 'no aaf'
monitoring = 'seguimiento'
alertsTreatments = {benign: 0, noSuspicious: 0, slightlySuspicious: 0,
                    moderatelySuspicious: 0, highlySuspicious: 0, aaf: 0,
                    noAaf: 0, monitoring: 0}


def openProcessFile():
    '''Funcion que accede a un archivo csv y filtra la informacion de las
    columnas(alerta y tratamiento), segun la cuiudad solicitada.
    '''

    city = input().lower()
    with open('data.csv', newline='') as datos:
        data = csv.reader(datos)

        for row in data:
            if city in row[2].lower():
                for key, value in alertsTreatments.items():
                    if row[13].lower() == key:
                        alertsTreatments[key] = value + 1
                    if row[14].lower() == key:
                        alertsTreatments[key] = value + 1


def printCount():
    '''Funcion que evalua e imprime el resultado del conteo.'''

    alerts = {}
    treatments = {}
    num = 1

    for key, value in alertsTreatments.items():
        if num <= 5:
            alerts[key] = value
        else:
            treatments[key] = value
        num += 1

    alerts = sorted(alerts.items(), key=operator.itemgetter(1), reverse=True)
    for val in alerts:
        print(val[0], val[1])

    treatments = sorted(treatments.items(), key=operator.itemgetter(1),
                        reverse=True)
    for val in treatments:
        print(val[0], val[1])


def run():
    '''la función inicia el programa y llama a las funciones en orden.'''

    openProcessFile()
    printCount()


if __name__ == "__main__":
    run()

#!/usr/bin/python3
'''
    Algoritmo Division
    inicio
        Definir variable "dividendo" de tipo Entero
        Definir variable "divisor" de tipo Entero
        Definir variable "cociente"
        Leer dividendo y divisor
        cociente = dividendo / divisor
        salida cociente
    Fin
'''


def division(dividendo,divisor):
    '''Funcion que recibe como parametro dos numeros enteros y retorna la
    division de ambos numeros.
    '''
    return dividendo/divisor


def printDivision():
    '''Funcion que llama a la funcion division para imprimir por pantalla el 
    resultado.
    '''
    global dividendo
    global divisor

    dividendo = int(input("ingrese un numero entero para la variable dividendo: "))
    divisor = int(input("ingrese un numero entero para la variable divisor: "))

    cociente = int(division(dividendo, divisor))
    print("El cociente es de:", cociente)
        

if __name__ == "__main__":
    # Declaracion e inicializacion de variables
    dividendo = 0
    divisor = 0

    # Llamado a la funcion printDivision
    printDivision()

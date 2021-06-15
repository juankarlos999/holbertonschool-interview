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

'''
    Funcion que recibe como parametro dos numeros enteros y retorna la
    division de ambos numeros
'''
def division(dividendo,divisor):
    return dividendo/divisor

'''
    Funcion que llama a la funcion division para imprimir por pantalla el 
    resultado
'''
def printDivision():
    # inputs para variables a,b y llamado a la funcion division
    global dividendo
    global divisor

    dividendo = int(input("ingrese un numero entero para la variable dividendo: "))
    divisor = int(input("ingrese un numero entero para la variable divisor: "))

    cociente = int(division(dividendo,divisor))
    print("El cociente es de:",cociente)
        

# Declaracion e inicializacion de variables
dividendo = 0
divisor = 0

# Llamado a la funcion printDivision
printDivision()
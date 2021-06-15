#!/usr/bin/python3
'''
    Algoritmo fizzBuzz
    inicio
        Definir i como tipo Entero = 0
        Definir rango como tipo entero = 101
        Para la variable "i" si es menor que la variable "rango" Haga:
            Si i mod 3 == 0 Entonces
                imprima "Fizz"
            Si i mod 5 == 0 Entonces
                imprima "Buzz"
            Si i mod 5 == 0 Entonces
                imprima "Fizz"
            Si i mod 5 == 0 y i mod 3 == 0 Entonces
                imprima "FizzBuzz"
            Sino imprima "i"
           FinSi
           incremento de la variable i en 1
        FinPara
    Fin

'''
# Funcion que imprime los números del 1 al 100
def fizzbuzz():
    '''
        Multiplos de 3 imprime "Fizz"
        Multiplos de 5 imprime "Buzz"
        Multiplos de ambos imprime "FizzBuzz"
    '''
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Llamado a la funcion
fizzbuzz()
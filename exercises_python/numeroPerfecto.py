#!/usr/bin/python3


def numeroPerfecto(num):
    '''Funcion que recibe como entrada n numeros enteros positivos, y por cada
    uno de ellos imprime sus divisores e indica si es perfecto o no.
    '''
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
            print("divisor=", i)
    if num == suma:
        print(f"suma de divisores = {suma}")
        return True
    else:
        print(f"suma de divisores = {suma}")
        return False


if __name__ == "__main__":
    numInputs = int(input("Introduzca la cantidad de numeros a validar: "))
    i = 1
    while i <= numInputs:
        num = int(input("introduzca un numero: "))
        # llamada al metodo numeroPerfecto
        if numeroPerfecto(num):
            print(f"{num} es un numero perfecto")
        else:
            print(f"{num} no es un numero perfecto")
        # incremento contador del bucle
        i += 1

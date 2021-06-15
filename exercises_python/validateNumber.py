#!/usr/bin/python3

'''Funcion capaz de ingresar valores enteros y verificar si están dentro de un
rango especificado.
'''


def readint(prompt, min, max):
    num = input(prompt)
    try:
        if '-' in num[0]:
            num = int(num)
        else:
            if not num.isdigit():
                raise ValueError("Error: entrada incorrecta")
            else:
                num = int(num)
        if num < min or num > max:
            raise Exception("Error: el valor no está dentro del rango permitido (-10..10)")
    except ValueError as msm:
        print(msm)
    except Exception as outRange:
        print(outRange)
    else:
        return num

if __name__ == "__main__":
    while True:
        v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
        if v is not None:
            break

    print("El numero es:", v)

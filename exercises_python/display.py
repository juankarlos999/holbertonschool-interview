#!/usr/bin/python3

'''Programa que puede simular el funcionamiento de un display de siete
segmentos.
'''

numbers = {
            1: [[" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"],
                [" ", " ", "#"], [" ", " ", "#"]],
            2: [["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"],
                ["#", " ", " "], ["#", "#", "#"]],
            3: [["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"],
                [" ", " ", "#"], ["#", "#", "#"]],
            4: [["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"],
                [" ", " ", "#"], [" ", " ", "#"]],
            5: [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"],
                [" ", " ", "#"], ["#", "#", "#"]],
            6: [["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"],
                ["#", " ", "#"], ["#", "#", "#"]],
            7: [["#", "#", "#"], [" ", " ", "#"], [" ", "#", "#"],
                [" ", " ", "#"], [" ", " ", "#"]],
            8: [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"],
                ["#", " ", "#"], ["#", "#", "#"]],
            9: [["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"],
                [" ", " ", "#"], [" ", " ", "#"]],
            0: [["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"],
                ["#", " ", "#"], ["#", "#", "#"]]
            }


def display():

    try:
        num = input("Ingrese un numero: ")
        print()

        if not num : #cadena vacia
            raise TypeError
        elif not num.isdigit():
            raise ValueError

        num = [int(x) for x in num]
        printDisplay = [[] for row in range(5)]

        for row in range(5):
            key = 0
            while key < len(num):
                col = 0
                while col < 3:
                    printDisplay[row].append(numbers[num[key]][row][col])
                    col += 1
                printDisplay[row].append("  ")
                key += 1

        for row in printDisplay:
            for col in row:
                print(col, end="")
            print()
    except ValueError:
        print("Error\nIngrese unicamente numeros")
        respuesta = input("Desea volver a intentarlo ? y / n :")
        if respuesta.lower() == 'y':
            display()
        else:
            print("FIN...")
    except TypeError:
        print("Error\ningreso vacio")
        respuesta = input("Desea volver a intentarlo ? y / n :")
        if respuesta.lower() == 'y':
            display()
        else:
            print("FIN...")


if __name__ == "__main__":
    display()

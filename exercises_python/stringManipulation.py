
def palindromo():

    cadena1 = "Ten animals I slam in a net"
    print("cadena 1 ", cadena1)

    cadena2 = cadena1[::-1]  # Uso Slicing para invertir el orden del arreglo
    print("cadena 2 ", cadena2)

    var = cadena1.split()
    var = "".join(var).lower()
    print("cadena 1 ", cadena1)

    cadena2 = cadena2.split()
    cadena2 = "".join(cadena2).lower()
    print("cadena 2 ", cadena2)

    if cadena1 == cadena2:
        print("Es palindromo")


def anagrama():
    palabra1 = input("Ingrese la palabra 1: ")
    palabra2 = input("Ingrese la palabra 2: ")

    palabraClon = palabra1.lower()
    palabra2 = palabra2.lower()

    palabraClon = list(palabraClon)
    palabra2 = list(palabra2)
    index = 0

    if len(palabra1) == len(palabra2):
        for letra in palabra2:
            if letra in palabraClon:
                index = palabraClon.index(letra)
                del palabraClon[index]
            if not palabraClon:
                print(f"La palabra '{''.join(palabra2)}' es Anagrama de\
                     '{palabra1}'.")

        if palabraClon:
            print(f"*La palabra '{''.join(palabra2)}' NO es un Anagrama de\
                 '{palabra1}'.")
    else:
        print(f"**La palabra '{''.join(palabra2)}' NO es un Anagrama de\
             '{palabra1}'.")


if __name__ == "__main__":

    # anagrama()
    # palindromo()

    print(float("1, 3"))
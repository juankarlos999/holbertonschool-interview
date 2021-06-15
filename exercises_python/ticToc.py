#!/usr/bin/python3
from random import randint

board = [[0 for col in range(3)] for row in range(3)]
val = 1
for row in board:
    for col in range(3):
        if val != 5: row[col]=val
        else: row[col]='X'
        val += 1

def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print("+","-"*7,"+","-"*7,"+","-"*7,"+",sep="")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("|"," "*3,board[0][0]," "*3,"|"," "*3,board[0][1]," "*3,"|"," "*3,board[0][2]," "*3,"|",sep="")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+",sep="")
    
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("|"," "*3,board[1][0]," "*3,"|"," "*3,board[1][1]," "*3,"|"," "*3,board[1][2]," "*3,"|",sep="")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+",sep="")
    
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("|"," "*3,board[2][0]," "*3,"|"," "*3,board[2][1]," "*3,"|"," "*3,board[2][2]," "*3,"|",sep="")
    print("|"," "*7,"|"," "*7,"|"," "*7,"|",sep="")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+",sep="")
    
    
def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    select = int(input("Ingresa tu movimiento: "))
    freeBoard = MakeListOfFreeFields(board)
    for tupla in freeBoard:
        if board[tupla[0]][tupla[1]] == select:
            board[tupla[0]][tupla[1]] = 'O'
    DisplayBoard(board)

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    freeBoard = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'X' and board[row][col] != 'O':
                freeBoard.append((row,col))
    return freeBoard
        
def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

    if sign == 'O' or sign == 'X':
        for row in board:
            if row[0] == row[1] == row[2] == 'O':
                print("¡Has Ganado!")
                return True
            elif row[0] == row[1] == row[2] == 'X':
                print("¡Has Perdido!")
                return True
            for col in range(len(row)):
                if board[0][col] == board[1][col] == board[2][col] == 'O':
                    print("¡Has Ganado!")
                    return True
                elif board[0][col] == board[1][col] == board[2][col] == 'X':
                    print("¡Has Perdido!")
                    return True
                elif board[0][0] == board[1][1] == board[2][2] == 'X':
                    print("¡Has Perdido!")
                    return True
                elif board[0][2] == board[1][1] == board[2][0] == 'X':
                    print("¡Has Perdido!")
                    return True

    return False

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    true = 0
    while true == 0:
        select = randint(1,9)
        freeBoard = MakeListOfFreeFields(board)
        for tupla in freeBoard:
            if board[tupla[0]][tupla[1]] == select:
                board[tupla[0]][tupla[1]] = 'X'
                true = 1
    DisplayBoard(board)


def run():
#
# la función inicia el programa y llama a otras funciones
#
    DisplayBoard(board)
    resultado = False
    opciones = 1

    while opciones <= 8:
        if resultado == False:
            EnterMove(board)
            opciones += 1
            resultado = VictoryFor(board, 'O')
        else:
            break
        if resultado == False:
            DrawMove(board)
            opciones += 1
            resultado = VictoryFor(board, 'X')
        else:
            break
    print(__name__)
        


if __name__ == "__main__":  
    
    run()
    print("FIN...")
    print(__name__)
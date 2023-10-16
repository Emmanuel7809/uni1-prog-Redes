#Alan Francisco Emmanuel Aguilar Fuentes
#Programacion de Redes 
# 12/10/2023
#Modulo 4
from random import randrange

def DisplayBoard(board):
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")

def EnterMove(board):
    move = input("Ingresa tu movimiento (número del cuadro): ")
    if not move.isdigit():
        print("Entrada no válida. Debes ingresar un número del 1 al 9.")
        return False

    move = int(move)
    if move < 1 or move > 9 or board[(move - 1) // 3][(move - 1) % 3] != str(move):
        print("Movimiento no válido. El cuadro está ocupado o no existe.")
        return False

    return True

def MakeListOfFreeFields(board):
    free_fields = []
    for row in board:
        free_fields.extend([str(x) for x in row if x.isdigit()])
    return free_fields

def VictoryFor(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    move = int(free_fields[randrange(len(free_fields))])
    for row in board:
        if str(move) in row:
            row[row.index(str(move))] = 'X'
            break

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

while True:
    DisplayBoard(board)
    if not EnterMove(board):
        continue

    if VictoryFor(board, 'O'):
        DisplayBoard(board)
        print("¡Has Ganado!")
        break

    if len(MakeListOfFreeFields(board)) == 0:
        DisplayBoard(board)
        print("Empate")
        break

    DrawMove(board)

    if VictoryFor(board, 'X'):
        DisplayBoard(board)
        print("¡La máquina ha ganado!")
        break

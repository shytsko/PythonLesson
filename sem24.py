# 41. Создайте программу для игры в "Крестики-нолики".

from random import randint
import re


board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def printBoard(brd):
    print(" ".join(brd[0]))
    print(" ".join(brd[1]))
    print(" ".join(brd[2]))


def CheckBoard(brd):
    if ((brd[0][0] == "х" and brd[0][1] == "х" and brd[0][2] == "х") or
        (brd[1][0] == "х" and brd[1][1] == "х" and brd[1][2] == "х") or
        (brd[2][0] == "х" and brd[2][1] == "х" and brd[2][2] == "х") or
        (brd[0][0] == "х" and brd[1][0] == "х" and brd[2][0] == "х") or
        (brd[0][1] == "х" and brd[1][1] == "х" and brd[2][1] == "х") or
        (brd[0][2] == "х" and brd[1][2] == "х" and brd[2][2] == "х") or
        (brd[0][0] == "х" and brd[1][1] == "х" and brd[2][2] == "х") or
            (brd[0][2] == "х" and brd[1][1] == "х" and brd[2][0] == "х")):
        return 1
    elif ((brd[0][0] == "o" and brd[0][1] == "o" and brd[0][2] == "o") or
          (brd[1][0] == "o" and brd[1][1] == "o" and brd[1][2] == "o") or
          (brd[2][0] == "o" and brd[2][1] == "o" and brd[2][2] == "o") or
          (brd[0][0] == "o" and brd[1][0] == "o" and brd[2][0] == "o") or
          (brd[0][1] == "o" and brd[1][1] == "o" and brd[2][1] == "o") or
          (brd[0][2] == "o" and brd[1][2] == "o" and brd[2][2] == "o") or
          (brd[0][0] == "o" and brd[1][1] == "o" and brd[2][2] == "o") or
          (brd[0][2] == "o" and brd[1][1] == "o" and brd[2][0] == "o")):
        return 2

    if '-' in set(brd[0]) | set(brd[1]) | set(brd[2]):
        return -1

    return 0


def GetMove(brd):
    while True:
        try:
            m = input("Сделайте ход (строка-столбец): ")
            i, j = list(map(int, m.split("-")))
            if brd[i][j] != '-':
                raise
        except:
            print("Неверный ввод")
        else:
            return (i, j)


whoseMove = randint(0, 1)
if whoseMove == 1:
    print("Первым ходит x")
else:
    print("Первым ходит o")
total = -1
printBoard(board)
while total < 0:
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == 0:
        print("Ход х")
        move = GetMove(board)
        board[move[0]][move[1]] = "х"
    else:
        print("Ход o")
        move = GetMove(board)
        board[move[0]][move[1]] = "o"
    printBoard(board)
    total = CheckBoard(board)

if total == 1:
    print("Победил х!!!")
elif total == 2:
    print("Победил o!!!")
else:
    print("Ничья!!!")

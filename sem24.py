# 41. Создайте программу для игры в "Крестики-нолики".

from random import randint

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

symbols = {0: "-", 1: "X", -1: "O"}

def CheckBoard(brd):
    winCombinationX = (1, 1, 1)
    winCombinationO = (-1, -1, -1)
    combinations = tuple(map(tuple, [brd[0:3], brd[3:6], brd[6:9],
                                    brd[0:9:3], brd[1:9:3], brd[2:9:3],
                                    brd[0:9:4], brd[-3:-8:-2]]))
    if winCombinationX in combinations:
        return 1
    elif winCombinationO in combinations:
        return -1
    elif 0 in brd:
        return 0
    else:
        return -2


def PrintBoard(brd):
    print(" ".join(map(lambda i: symbols[i], brd[0:3])))
    print(" ".join(map(lambda i: symbols[i], brd[3:6])))
    print(" ".join(map(lambda i: symbols[i], brd[6:9])))


def GetMove(brd):
    while True:
        try:
            m = input("Сделайте ход (строка-столбец): ")
            i, j = list(map(int, m.split("-")))
            move = (i-1)*3 + (j-1)
            if brd[move] != 0:
                raise
        except:
            print("Неверный ввод")
        else:
            return move


whoseMove = randint(0, 1)
if whoseMove == 1:
    print("Первым ходит X")
else:
    print("Первым ходит O")
end = 0
PrintBoard(board)
while not end:
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == 0:
        print("Ход X")
        move = GetMove(board)
        board[move] = 1
    else:
        print("Ход O")
        move = GetMove(board)
        board[move] = -1
    PrintBoard(board)
    end = CheckBoard(board)

if end == 1:
    print("Победил X!!!")
elif end == -1:
    print("Победил O!!!")
else:
    print("Ничья!!!")

# 41. Создайте программу для игры в "Крестики-нолики".

from random import randint

EPMTY = 0
X = 1
O = -1
SYMBOLS = {EPMTY: "-", X: "X", O: "O"}

X_WIN = X
O_WIN = O
NOT_END = 0
DRAW = -2


def CheckBoard(brd):
    winCombinationX = (X, X, X)
    winCombinationO = (O, O, O)
    combinations = tuple(map(tuple, [brd[0:3], brd[3:6], brd[6:9],
                                     brd[0:9:3], brd[1:9:3], brd[2:9:3],
                                     brd[0:9:4], brd[-3:-8:-2]]))
    if winCombinationX in combinations:
        return X_WIN
    elif winCombinationO in combinations:
        return O_WIN
    elif EPMTY in brd:
        return NOT_END
    else:
        return DRAW


def PrintBoard(brd):
    print(" ".join(map(lambda i: SYMBOLS[i], brd[0:3])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[3:6])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[6:9])))


def GetMove(brd):
    while True:
        try:
            m = input("Сделайте ход (строка столбец через пробел): ")
            i, j = list(map(int, m.split()))
            move = (i-1)*3 + (j-1)
            if brd[move] != EPMTY:
                raise
        except:
            print("Неверный ввод")
        else:
            return move

board = [EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY]

whoseMove = randint(0, 1)
if whoseMove != X:
    print("Первым ходит X")
else:
    print("Первым ходит O")
end = NOT_END
PrintBoard(board)
while not end:
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == X:
        print("Ход X")
        move = GetMove(board)
        board[move] = X
    else:
        print("Ход O")
        move = GetMove(board)
        board[move] = O
    PrintBoard(board)
    end = CheckBoard(board)

if end == X_WIN:
    print("Победил X!!!")
elif end == O_WIN:
    print("Победил O!!!")
else:
    print("Ничья!!!")

# 41. Создайте программу для игры в "Крестики-нолики".
import random

EPMTY = 0
X = 1
O = -1
SYMBOLS = {EPMTY: "-", X: "X", O: "O"}

X_WIN = X
O_WIN = O
DRAW = 0
NOT_END = -2


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


def PrintBoard(brd: list):
    print(" ".join(map(lambda i: SYMBOLS[i], brd[0:3])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[3:6])))
    print(" ".join(map(lambda i: SYMBOLS[i], brd[6:9])))


def HumanMove(brd: list):
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


def BotMove(brd: list):
    possibleMoves = {m for m, s in enumerate(brd) if s == EPMTY}
    cornerСellsEmpty = possibleMoves & {0, 2, 6, 8}
    sideСellsEmpty = possibleMoves & {1, 3, 5, 7}
    for move in possibleMoves:
        newBrd = brd[::]
        newBrd[move] = O
        if CheckBoard(newBrd) == O_WIN:
            return move
    for move in possibleMoves:
        newBrd = brd[::]
        newBrd[move] = X
        if CheckBoard(newBrd) == X_WIN:
            return move
    if 4 in possibleMoves:
        return 4
    else:
        if len(cornerСellsEmpty) == 2 and ((brd[0] == X and brd[8] == X) or (brd[2] == X and brd[6] == X)):
            for firstMove in sideСellsEmpty:
                newBrd = brd[::]
                newBrd[firstMove] = O
                for secondMove in possibleMoves - {firstMove}:
                    newBrdSecond = newBrd[::]
                    newBrdSecond[secondMove] = O
                    if CheckBoard(newBrdSecond) == O_WIN:
                        return firstMove
    for firstMove in cornerСellsEmpty:
        newBrd = brd[::]
        newBrd[firstMove] = O
        for secondMove in possibleMoves - {firstMove}:
            newBrdSecond = newBrd[::]
            newBrdSecond[secondMove] = O
            if CheckBoard(newBrdSecond) == O_WIN:
                return firstMove
    for firstMove in possibleMoves:
        newBrd = brd[::]
        newBrd[firstMove] = O
        for secondMove in possibleMoves - {firstMove}:
            newBrdSecond = newBrd[::]
            newBrdSecond[secondMove] = O
            if CheckBoard(newBrdSecond) == O_WIN:
                return firstMove
    if len(cornerСellsEmpty) != 0:
        return random.choice(tuple(cornerСellsEmpty))
    return random.choice(tuple(possibleMoves))


board = [EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY,
         EPMTY, EPMTY, EPMTY]

whoseMove = random.randint(0, 1)
if whoseMove != X:
    print("Первым ходит X")
else:
    print("Первым ходит O")
gameState = NOT_END
PrintBoard(board)
while gameState == NOT_END:
    whoseMove = (whoseMove + 1) % 2
    if whoseMove == X:
        print("Ход X")
        move = HumanMove(board)
        board[move] = X
    else:
        print("Ход O")
        move = BotMove(board)
        board[move] = O
    PrintBoard(board)
    print("-----------------")
    gameState = CheckBoard(board)

if gameState == X_WIN:
    print("Победил X!!!")
elif gameState == O_WIN:
    print("Победил O!!!")
else:
    print("Ничья!!!")

# 41. Создайте программу для игры в "Крестики-нолики".
import random

HUMAN = 0
BOT = 1

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


def OneMoveWin(brd: list, moves: set, wMove: int) -> int:
    for move in moves:
        newBrd = brd[::]
        newBrd[move] = wMove
        if CheckBoard(newBrd) == wMove:
            return move
    return -1


def TwoMoveWin(brd: list, priorityMoves: set, allMoves: set, wMove: int) -> int:
    for firstMove in priorityMoves:
        newBrd = brd[::]
        newBrd[firstMove] = wMove
        for secondMove in allMoves - {firstMove}:
            newBrdSecond = newBrd[::]
            newBrdSecond[secondMove] = wMove
            if CheckBoard(newBrdSecond) == wMove:
                return firstMove
    return -1


def BotMove(brd: list, wMove: int):
    possibleMoves = {m for m, s in enumerate(brd) if s == EPMTY}
    opponent = X if wMove == O else O
    cornerСellsEmpty = possibleMoves & {0, 2, 6, 8}
    sideСellsEmpty = possibleMoves & {1, 3, 5, 7}
    center = 4
    move = OneMoveWin(brd, possibleMoves, wMove)
    if move != -1:
        return move
    move = OneMoveWin(brd, possibleMoves, opponent)
    if move != -1:
        return move
    if brd[center] == EPMTY:
        return center
    else:
        if len(cornerСellsEmpty) == 2 and ((brd[0] == opponent and brd[8] == opponent)
                                           or (brd[2] == opponent and brd[6] == opponent)):
            move = TwoMoveWin(brd, sideСellsEmpty, possibleMoves, wMove)
            if move != -1:
                return move
    move = TwoMoveWin(brd, cornerСellsEmpty, possibleMoves, wMove)
    if move != -1:
        return move
    move = TwoMoveWin(brd, possibleMoves, possibleMoves, wMove)
    if move != -1:
        return move
    if len(cornerСellsEmpty) != 0:
        return random.choice(tuple(cornerСellsEmpty))
    return random.choice(tuple(possibleMoves))


def TycTacToe(player1, player2):
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
            if player1 == HUMAN:
                move = HumanMove(board)
            else:
                move = BotMove(board, X)
            board[move] = X
        else:
            print("Ход O")
            if player2 == HUMAN:
                move = HumanMove(board)
            else:
                move = BotMove(board, O)
            board[move] = O
        PrintBoard(board)
        print("-----------------")
        gameState = CheckBoard(board)
    return gameState


gameRusult = TycTacToe(BOT, BOT)
if gameRusult == X_WIN:
    print("Победил X!!!")
elif gameRusult == O_WIN:
    print("Победил O!!!")
else:
    print("Ничья!!!")

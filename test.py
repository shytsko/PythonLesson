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

board = [['-', 'х', '-'], ['-', '-', '-'], ['-', '-', '-']]

print(GetMove(board))
# КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла
# чтоб статистика сохранялась, и можно было играть неограниченное количество раундов

import random


moves = {'1': '💎',
    '1': '💎',
         '2': '✂️',
         '3': '📜',
         'q': '🚪'}
winCombination = [('1', '2'), ('2', '3'), ('3', '1')]
scoreGamer = 0.0
scoreBot = 0.0


def PrintMoves():
    global moves
    for k, v in moves.items():
        print(f'{k}\t{v}')


while True:
    print('---------------------------------------------')
    print(f'Игрок - {scoreGamer} : {scoreBot} - Компьютер')
    PrintMoves()
    moveGamer = input("Ваш ход: ")
    if moveGamer in moves:
        if moveGamer == 'q':
            break
        moveBot = str(random.randint(1, 3))
        print(
            f'Ваш ход - {moves[moveGamer]}, ход компьютера - {moves[moveBot]}')
        if moveGamer == moveBot:
            print('Ничья!')
            scoreGamer += 0.5
            scoreBot += 0.5
        elif (moveGamer, moveBot) in winCombination:
            print('Игрок выиграл!')
            scoreGamer += 1.0
        else:
            print('Компьютер выиграл!')
            scoreBot += 1.0
    else:
        print('Повторите ввод.')

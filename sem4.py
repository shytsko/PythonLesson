# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

f = float(input('Введите вещественное число: '))

def fun(f):
    if(f != int(f)):
        return (int(f * 10)) % 10
    else:
        return 'Нет'

print(fun(f))
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


def check(x):
    return ((x % 5 ==0) and (x % 10 ==0)) or ((x % 15 ==0) and (x % 30 != 0))

x = int(input('Введите число: '))
print(check(x))
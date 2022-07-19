# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

A = int(input("A="))
B = int(input("B="))


def gcd(a, b):
    if(a < b):
        (a, b) = (b, a)
    return gcd(b, a % b) if b != 0 else a


def lcm(a, b):
    return a // gcd(a, b) * b


print(lcm(A, B))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#     *Пример:*
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10


def DecToBin(n):
    lstBin = []
    while n > 0:
        lstBin.append(str(n%2))
        n //= 2
    return "".join(lstBin[::-1])

print(DecToBin(6))

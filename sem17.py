# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1,



def Fibbonacci(n):
    result = []
    
    for i in range(n+1):
        if i == 0:
            result.append(0)
        elif i==1:
            result.append(1)
            result.insert(0, 1)
        else:
            result.append(result[-1] + result[-2])
            result.insert(0, result[1] - result[0])
    return result

print(Fibbonacci(8))
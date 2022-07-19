# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from difflib import Match


input = [1.1, 1.2, 3.1, 5.0, 10.01]

def fun(lst):
    lstF = []
    for a in lst:
        lstF.append(a - int(a))

    return max(lstF) - min(lstF)
    

print(fun(input))
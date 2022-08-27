# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

def FindUnique(source: list) -> list:
    return [x for x in source if source.count(x) == 1]


test = [1, 5, 674, 7, 6, 5, 'hg', 78, 2, 1, 'abc', 54, 'abc']
print(FindUnique(test))

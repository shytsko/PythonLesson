# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# сохраните список в формате JSON.

import json


def CreateList(n):
    result = []
    for i in range(-n, n+1):
        result.append(i)
    return result

n = int(input("Введите n: "))

with open('sem12.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
               fh.write(json.dumps(CreateList(n), ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
print('Файл сохранен')
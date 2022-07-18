# сделать функцию, на вход принимающую список, на выходе возращающая словарь,
# где указаны максимальное число, минимальное, их индексы, и среднее арифметическое
import json

input = [56, 5645, 4, 68, 64, 96, 64, 64, 496, -2415, 6412, -452, 0]


def fun(input_list):
    max = input_list[0]
    min = input_list[0]
    max_index = 0
    min_index = 0
    avg = 0
    for i in range(len(input_list)):
        if input_list[i] > max:
            max = input_list[i]
            max_index = i
        if input_list[i] < min:
            min = input_list[i]
            min_index = i
        avg += input_list[i]
    avg /= len(input_list)
    output = {}
    output["Минимальное значение"] = min
    output["Максимальное значение"] = max
    output["Индек минимального значения"] = min_index
    output["Индек максимального значенияе"] = max_index
    output["Среднее арифметическое"] = avg
    return output


output = fun(input)
print(input)
for k, v in output.items():
    print(f"{k} - {v}")

# Задайте список из n чисел ряда фибоначчи

n = int(input("Введите N = "))

def fibonacci(n):
    fibonacci_list = []

    for i in range(n):
        if i in (0, 1):
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

    return fibonacci_list

print(fibonacci(n))
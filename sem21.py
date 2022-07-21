# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.

#     Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint


def GenerateTerms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"


try:
    k = int(input("Введите степень многочлена (натуральное число): "))
    if k <= 0:
        raise
except:
    print("Нужно было ввести натуральное число.")
else:
    coefficients = [randint(0, 100) for _ in range(k+1)]
    print(coefficients)
    terms = [GenerateTerms(c, p) for (p, c) in enumerate(coefficients) if c != 0]
    result = " + ".join(terms[::-1]) + " = 0"
    print(result)

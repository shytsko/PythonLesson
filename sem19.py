# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

#     2) с помощью дополнительных библиотек Python

from math import sqrt


A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

D = B**2 - 4*A*C

if D == 0:
    x = -B/(2*A)
    print(f"Уравнение имеет один корень: {x}")
elif D > 0:
    x1 = (-B + sqrt(D)) / (2 * A)
    x2 = (-B - sqrt(D)) / (2 * A)
    print(f"Уравнение имеет два корня: x1={x1}; x2={x2}")
else:
    print("Уравнение не имеет вещественных корней")


# inp = input('Введите значения через пробел')
# inp = inp.split(' ')
# if(len(inp)==3):
#     print("Ввели 3 значения, выбрано квадратное уравнение")
#     print(Root(inp[0],inp[1],inp[2]))
# elif (len(inp)==2):
#     print("Ввели 2 значения, выбрано обычное уравнение")
#     print(Normal(inp[0],inp[1]))
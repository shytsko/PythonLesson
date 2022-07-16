# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def LeftExpression(x, y, z):
    return not (x or y or z)

def RightExpression(x, y, z):
    return not x and not y and not z


print('X\tY\tZ\t\t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            print(f'{x}\t{y}\t{z}\t\t{LeftExpression(x, y, z) == RightExpression(x, y, z)}')


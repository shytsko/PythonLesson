# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def Find(inStr: str):
    items = list(map(int, inStr.split()))
    min = items[0]
    max = items[-1]
    for i in range(min, max+1):
        if i not in items:
            return i
   

inputStr = ""

try:
    with open("file.txt", "r") as f:
        inputStr = f.read()
except:
    print("Не удалось прочитать файл")
else:
    print(Find(inputStr))

    

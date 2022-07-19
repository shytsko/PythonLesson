
file = open("text.txt", "r")
lst = file.read().split()
file.close()

result = [(int(i), int(i)**2) for i in lst if int(i) %2 == 0]

print(result)

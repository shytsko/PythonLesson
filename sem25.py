# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


def DeleteABV(source: str) ->str:
    words = source.split()
    for word in words:
        if "абв" in word:
            words.remove(word)
    return " ".join(words)

test = "Напишите прогабврамму, удаляющую из текста абввсе слова, содеабвржащие"
print(DeleteABV(test))
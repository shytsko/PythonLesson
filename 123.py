import json
sp=[5,11,2,3,4,8,157,555]

def max_average(sp):
    maxx=sp[0]
    sr=0
    for i in sp:
        if i > maxx:
            maxx=i
        sr+=i
    sr=sr/len(sp)
    rez={}
    rez['максимальный элемент']=maxx
    rez['среднее арифметическое']=sr
    k=(maxx,sr,rez)
    return k

with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD = json.load(fh)  # загружаем из файла данные в словарь data
print('БД успещно загружена')
print(type(BD))


#res=max_average(sp)

#with open('data.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
    
 #           fh.write(json.dumps(res, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#print('БД успещно сохранена')
#print(res[2])
#for x,y in res[2].items():
 #   print(x,y)

'''
print(len(rez))
for x,y in rez.items():
    print(x,y)
'''    
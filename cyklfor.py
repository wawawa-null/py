"""
m = 'stroka text'
count = 0

for i in m:
    if i == 't':
        print ('В строке есть бува t')
        count += 1

    if i == 'a':
        break

else:
    print ('Цикл завершён, кол-во букв t: ', count)
        
print ('программа работает дальше')
"""
"""
m = 'stroka text'
count = 0

for i in m:
    if i == 't':
        continue
        print ('В строке есть бува t')
        count += 1
    print (i)
    

else:
    print ('Цикл завершён, кол-во букв t: ', count)
        
print ('программа работает дальше')
"""

"""
x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
y = input ('Введите строку:\n')

for i in x:
    count = 0
    for r in y: 
        if i == r:
            count += 1
    if count > 0:
        print ('Букв', i, 'было', count)
"""


for x in range (100, -10, -2):
    print (x)

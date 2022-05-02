"""
import os
print ('Введите сайт: ')
sayt = input ()

if 'https://' in sayt:
    os.system ('start ' + sayt)
    print ('if')
elif 'www.' in sayt:
    sayt = 'https://' + sayt
    os.system ('start ' + sayt)
    print ('elif')
else:
    sayt = 'https://www.' + sayt
    os.system ('start ' + sayt)
    print ('else')
"""
import os
while True:
    #print ('Введите сайт: ')
    sayt = input ('Введите адрес сайта:\n')

    if sayt == 'завершить':
        break

    if 'https://' in sayt:
        os.system ('start ' + sayt)
        print ('if')
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system ('start ' + sayt)
        print ('elif')
    else:
        sayt = 'https://www.' + sayt
        os.system ('start ' + sayt)
        print ('else')

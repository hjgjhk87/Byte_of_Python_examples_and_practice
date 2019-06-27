name = 'Swaroop' # Это объект строки

if name.startswith('Swa'):
    print('Да, строка начинается с "Swa"')

if 'a' in name:
    print('Да, строка содержит строку "a"')

if name.find('war') != -1:
    print('Да, строка содержит строку "war" на позиции', name.find('war'))

delimiter = '_*_'

mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print('БРИК - расшифровывается как', delimiter.join(mylist))

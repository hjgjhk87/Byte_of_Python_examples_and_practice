# ab - сокращение от address book

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
    }

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Swaroop']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nАдрес Guido:', ab['Guido'])

print(ab.items())       # работает
#print((ab.items())[0]) # не работает, пишет: TypeError: 'dict_items' object does not support indexing
#print((ab.items()).__getitem__(0)) # не работает, пишет: AttributeError: 'dict_items' object has no attribute '__getitem__'

dic = {2 : 1, 5 : 3, 4 : 6, 1 : 9}
print(dic.items())
##result = sorted(dic)
##print(result)

# Какой-то непонятный мне пока пример сортировки из комментария в интернете: https://www.ibm.com/developerworks/ru/library/l-python_part_4/index.html
dict = {
'KEY_01': {2010: [8, 16], 2011: [2, 4], 2012: [3, 6], 2013: [1, 2]},
'KEY_0N': {2010: [5, 10], 2011: [9, 18], 2012: [7, 14], 2013: [10, 20]}
}
print([[k] + x[2010] for (k,x) in dict.items()]) # рез-т [['KEY_01', 8, 16], ['KEY_0N', 5, 10]]
print(sorted([[k] + x[2010] for (k,x) in dict.items()], key = lambda x: x[1]))

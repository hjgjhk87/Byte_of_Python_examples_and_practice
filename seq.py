shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

print(shoplist)
print(name)

# Операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Элемент -3 -', shoplist[-3])
print('Символ 0 - ', name[0])
#print('Тест:', 'А'[4])  # IndexError: string index out of range


# Вырезка из списка
# По умолчанию с шагом 1
print('Элементы с 1 по 3:', shoplist[1:3])
print('Элементы с 2 до конца:', shoplist[2:])
print('Элементы c 1 по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:]) # аналогично print(shoplist)
print('Символы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 до -1:', name[1:-1])
print('Символы от начала до конца:', name[:]) # аналогично print(name)
# Здесь выведет пустую строку
print('Тест:', 'А'[4:]) # А здесь IndexError нет, значит, вырезка более защищенная

# С другими шагами
# В вырезку б. добавлены элементы, индексы которых деляться на шаг без остатка
print('shoplist[::2]:', shoplist[::2]) 
print('shoplist[::3]:', shoplist[::3])



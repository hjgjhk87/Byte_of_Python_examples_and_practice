listone = [2, 3, 4]
listtwo = [2 * i for i in listone]
print(listtwo)

# Теперь сгенерирую с определенным условием if
listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)

# Теперь попробую сгенерировать из кортежа. Получилось
listone = (2, 3, 4)
listtwo = [2 * i for i in listone if i > 2]
print(listtwo)
print(type(listone))

#
a = [1, 2, 3]
str = 'test'
b = [str]
print(b)
b = [[str]]
print(b)
b = [[str] + a]
print(b)

# Это мой список покупок
shoplist = ['яблоки','манго','морковь','бананы']

print('Я должен сделать', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже надо купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок выгдядит так:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выгдядит так:', shoplist)

print('Первое, что мне надо купить - это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)

nestedList = [[1, 2, 3], [4, 5, 6, 7]]
print(nestedList)
del nestedList[1][2]
print(nestedList)

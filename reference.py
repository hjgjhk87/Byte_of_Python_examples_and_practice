print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist
print('shoplist:', shoplist)
print('mylist:', mylist)

del shoplist[0] # первая покупка удаляется из списка
print('После удаления первого элемента из shoplist')
print('shoplist:', shoplist)
print('mylist:', mylist)
# И shoplist, и mylist выводят один и тот же список
# без пункта "яблокv", подтверждая тем самым, что они указывают на один объект

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]
del shoplist[0] # опять удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist)
# теперь списки разные

print('Опять простое присваивание:  mylist = shoplist')
mylist = shoplist
print('shoplist:', shoplist)
print('mylist:', mylist)

print('Изменим shoplist, сделав его кортежем с числами: shoplist = 1, 2, 3')
shoplist = 1, 2, 3
print('shoplist:', shoplist)
print('mylist:', mylist)
# mylist не меняется

print('Опять простое присваивание, только наоборот: shoplist = mylist')
shoplist = mylist
print('shoplist:', shoplist)
print('mylist:', mylist)

print('Теперь изменим mylist, сделав его кортежем с числами: mylist = 1, 2, 3')
mylist = 1, 2, 3
print('shoplist:', shoplist)
print('mylist:', mylist)
# shoplist не меняется

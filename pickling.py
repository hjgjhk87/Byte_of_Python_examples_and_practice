import pickle

# Имя файла, в котором мы сохраним объект
shoplistfile = "shoplist.data"
# Собственно сам объект, содержащий список покупок
shoplist = ['бананы', 'яблоки', 'помидоры', 'хлеб', 'молоко', 'овсянка', 'шоколад']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist # уничтожаем переменную shoplist
#print(shoplist) # NameError: name 'shoplist' is not defined

# Считываем из хранилища
f = open(shoplistfile, 'rb')
shoplist = pickle.load(f) # загружаем объект из файла
f.close()
print(shoplist)

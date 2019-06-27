def printMax(x, y):
    '''Выводит максимальное из двух чисел.

Оба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно
    y = int(y)

    if(x > y):
        print(x, 'наибольшее')
    elif x == y:
        print (x, 'равно', y)
    else:
        print(y, 'наибольшее')

printMax(3, 5)
print(printMax.__doc__)
help(printMax)

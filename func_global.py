x = 50

def func():
    global x  # присваивание x нельзя сделать здесь
    
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
    
func()
print('Значение x составляет', x)

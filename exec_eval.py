exec('print("Привет, мир!")') # работает; exec() arg 1 must be a string, bytes or code object
#exec("Привет, мир!") # ошибка: SyntaxError: invalid syntax
eval('2*3') # почему-то при запуске из текста программы вообще ничего не отображается
print(eval('2*3')) # работает
exec('print(2*3)') # работает
eval('print(2*3)') # работает
exec('print(2*3)') # работает, в чем тогда разница между exec и eval
print(2*3) # тоже естественно работает


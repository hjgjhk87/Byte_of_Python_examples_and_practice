from mymodule import sayHi, __version__
#from mymodule import *  # импортирует все публичные имена, такие как sayhi, но не импортирует __version__, потому что оно начинается с двойного подчёркивания

sayHi()
print('Версия', __version__)
a = 23
print(a)

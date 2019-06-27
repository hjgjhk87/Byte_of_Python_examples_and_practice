class ShortInputException(Exception):
    '''Пользовательский класс исключения.'''
    def __init__(self, length, atleast):
        Exception(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа с текстом и т.д.
except EOFError:          # нажатие Cntr-d
    print('Ну зачем вы сделали EOF?')
except KeyboardInterrupt: # нажатие Cntr-с
    print('Вы отменили операцию.')
except ShortInputException as ex:
    print('ShortInputException: Длина введенной строки -- {0};\n\
                    ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('Вы ввели {0}'.format(text))
    

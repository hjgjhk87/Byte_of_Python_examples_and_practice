try:
    text = input('Введите что-нибудь --> ')
except EOFError:          # нажатие Cntr-d
    print('Ну зачем вы сделали EOF?')
except KeyboardInterrupt: # нажатие Cntr-с
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))

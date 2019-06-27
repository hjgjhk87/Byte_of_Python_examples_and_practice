from sys import argv
import pickle

addrBook = {}
addrBookFile = 'addressBook.data'

def displayNameAndData(name):   
    print('\n  {0}:'.format(name), end = '')
    
    counter = 0
    for value in addrBook[name]:
        counter += 1
        print('\n\t{0}. {1}'.format(counter, value), end = '')
    print()

def confirmChoice(message):
    print('\n  {0}\n'.format(message))
    response = input(" Введите 'да' или 'нет': ")
    response = splitResponse(response)[0]
    
    return response.lower().startswith('да')

def splitResponse(response):
    '''Разбивает ответ на первое слово в ответе и, при наличии, на то, что осталось (напр. имя, номер).\n
    Остаток собирает в строку, в которой отдельные слова разделены пробелом.\n
    Игнорирует лишние пробелы и табуляции из начала, конца и середины response.'''
    responseSplit = response.split()
    
##    # Отладка
##    print('Разбитая на части строка:', end = ' ')
##    for st in responseSplit:
##        print("{!r}".format(st), end = ' ')
##    print()

    firstWord = ''
    if len(responseSplit):       
        firstWord = responseSplit[0]
        #print("firstWord: {!r}".format(firstWord))
    
    rest = ' '.join(responseSplit[1:])
    #print("rest: {!r}".format(rest))

    return (firstWord, rest)

def findNameInAddrBook(name):
    # Создаю лист вида [['имя1', 'Имя2'], ['имя2', 'ИМЯ2']],
    # где 'Имя2', 'ИМЯ2' ключи-имена в словаре addrBook
    namesList = [[name.lower()] + [name] for name in addrBook]

    # Каждый элемент первой пары (в нижнем регистре) сравниваем с переданным name в нижнем регистре
    for item in namesList:
        if name.lower() == item[0]:
            return (True, item[1]) # если нашли, то возвращаем True и оригинальное имя из словаря
    return (False, name)
    

def add(name = None):
    # Если имя не было передано в функцию
    if name == None:        
        name = input('\n  Введите имя: ')
        name = ' '.join(name.split())
        while len(name) == 0:
                name = input('\n  Введите имя: ')
                name = ' '.join(name.split())

    nameInAddrBook, name = findNameInAddrBook(name) 
    if nameInAddrBook:
        
        print('\n  Для имени "{0}" внесены следующие записи с данными:'.format(name))
        displayNameAndData(name)
            
        while(True):
            response = input("\n  Введите:\n\n\
 'заменить <номер>', чтобы заменить существующую запись под указанным номером\n\n\
 'добавить', чтобы добавить новую запись\n\n\
 'выход', чтобы выйти из меню добавления\n\n  ")

            response, recordNum = splitResponse(response)
            
            if response.lower().startswith('заменить'):
                if recordNum.isdigit():
                    recordNum = int(recordNum) - 1
                    if recordNum >= 0 and recordNum < len(addrBook[name]):
                        value = input('\n  Введите данные: ')
                        value = ' '.join(value.split())
                        while len(value) == 0:
                            value = input('\n  Введите данные: ')
                            value = ' '.join(value.split())
                            
                        addrBook[name][recordNum] = value
                        displayNameAndData(name)
                        
            elif response.lower().startswith('добавить'):
                value = input('\n  Введите данные: ')
                value = ' '.join(value.split())
                while len(value) == 0:
                    value = input('\n  Введите данные: ')
                    value = ' '.join(value.split())
                    
                addrBook[name].append(value)
                displayNameAndData(name)
                
            elif response.lower().startswith('выход'):
                break
    else:
        value = input('\n  Введите данные: ')
        value = ' '.join(value.split())
        while len(value) == 0:
            value = input('\n  Введите данные: ')
            value = ' '.join(value.split())
            
        addrBook[name] = [value]
        displayNameAndData(name)

def display(name = None):
    # Если имя было передано в функцию
    if name:
        nameInAddrBook, name = findNameInAddrBook(name)
        if nameInAddrBook:               
                displayNameAndData(name)
        else:
            print('\n  Имя "{0}" не найдено в адресной книге'.format(name))
    
    while(True):
        
        response = input("\n  Введите:\n\n\
 'всё', чтобы просмотреть всю адресную книгу\n\n\
 'имена', чтобы посмотреть только имена\n\n\
 'имя [<имя>]', чтобы просмотреть контактные данные для одного имени\n\n\
 'выход', чтобы выйти из этого меню просмотра\n\n  ")

        response, name = splitResponse(response)

        if response.lower().startswith('вс'):
            if len(addrBook):
                for name in addrBook:
                  displayNameAndData(name)
            else:
                print('\n  Адресная книга пуста.')
                break # адресная книга пуста, из меню просмотра можно уходить

        elif response.lower().startswith('имена'):
            if len(addrBook):
                for name in addrBook.keys():
                    print('\t', name)
            else:
                print('\n  Адресная книга пуста.')
                break # адресная книга пуста, из меню просмотра можно уходить

        elif response.lower().startswith('имя'):
            while len(name) == 0:
                name = input('\n  Введите имя: ')
                name = ' '.join(name.split())
                
            nameInAddrBook, name = findNameInAddrBook(name)
            if nameInAddrBook:
                displayNameAndData(name)
            else:
                print('\n  Имя "{0}" не найдено в адресной книге'.format(name))
                
        elif response.lower().startswith('выход'):
                    break

def deleteForName(name):     
    print('\n  Для имени "{0}" внесены следующие записи с данными:'.format(name))
    displayNameAndData(name)

    while(True):
        response = input("\n  Введите:\n\n\
 'удалить <номер>', чтобы удалить только запись под указанным номером\n\n\
 'всё', чтобы удалить имя и все записи, относящиеся к нему\n\n\
 'выход', чтобы выйти из меню удаления для одного имени\n\n  ")

        response, recordNum = splitResponse(response)
        
        if response.lower().startswith('вс'):
            if confirmChoice("Вы действительно хотите удалить имя и все записи, относящиеся к нему?"):
                del addrBook[name]
                print('\n  Имя "{0}" и все записи, относящиеся к нему, удалены.'.format(name))
                break # имя и его записи удалены, из меню удаления для одного имени можно выходить 
        
        elif response.lower().startswith('удалить'):
            if recordNum.isdigit():
                recordNum = int(recordNum) - 1
                
                if recordNum >= 0 and recordNum < len(addrBook[name]):
                    del addrBook[name][recordNum]
                    displayNameAndData(name)
                
        elif response.lower().startswith('выход'):
            break

def delete(name = None):
    # Если имя было передано в функцию
    if name:        
        nameInAddrBook, name = findNameInAddrBook(name)
        if nameInAddrBook:               
                deleteForName(name)
        else:
            print('\n  Имя "{0}" не найдено в адресной книге'.format(name))

    while(True):
        
        response = input("\n  Введите:\n\n\
 'имя [<имя>]', чтобы удалить контактные данные для одного имени\n\n\
 'всё', чтобы удалить всю адресную книгу\n\n\
 'выход', чтобы выйти из меню удаления\n\n  ")

        response, name = splitResponse(response)

        if response.lower().startswith('вс'):
            if confirmChoice("Вы действительно хотите удалить всю адресную книгу?"):
                addrBook.clear()
                print('\n  Адресная книга удалена.')
                break # адресная книга пуста, из меню удаления можно уходить
            
        elif response.lower().startswith('имя'):
            while len(name) == 0:
                name = input('\n  Введите имя: ')
                name = ' '.join(name.split())
                
            nameInAddrBook, name = findNameInAddrBook(name)
            if nameInAddrBook:
                deleteForName(name)
            else:
                print('\n  Имя "{0}" не найдено в адресной книге'.format(name))
                
        elif response.lower().startswith('выход'):
            break
    

try:
    f = open(addrBookFile, 'rb')
    addrBook = pickle.load(f)
    f.close()
except:
    pass

# Обработка аргументов командной строки, если они есть   
if len(argv) > 1:
    
    if argv[1].lower().startswith('-add'):       
        if len(argv) > 2:
            name = ' '.join(argv[2:])
            add(name)
        else:
            add()
            
    elif argv[1].lower().startswith('-del'):       
        if len(argv) > 2:
            name = ' '.join(argv[2:])
            delete(name)
        else:
            delete()
        
    elif argv[1].lower().startswith('-display'):       
        if len(argv) > 2:
            name = ' '.join(argv[2:])
            display(name)
        else:
            display()
            
    elif argv[1] == '-help':
        print("\n  Справка. Аргументы командной строки:\n\n\
 '-add [<имя>]' - для перехода в меню добавления контактных данных\n\n\
 '-del [<имя>]' - для удаления контактных данных для имени или перехода в меню удаления\n\n\
 '-display' [<имя>] - для просмотра контактных данных для имени или перехода в меню просмотра\n")
        exit(0)
        
    else:
        print("\n  Справка. Аргументы командной строки:\n\n\
 '-add [<имя>]' - для перехода в меню добавления контактных данных\n\n\
 '-del [<имя>]' - для удаления контактных данных для имени или перехода в меню удаления\n\n\
 '-display' <имя> - для просмотра контактных данных для имени или перехода в меню просмотра\n\n\
 '-help' - для просмотра этой справки")
        exit(0)

# Основной блок работы программы
while(True):
    response = input("\n  Введите:\n\n\
 'добавить [<имя>]' или '-add [<имя>]', чтобы перейти в меню добавления контактных данных\n\n\
 'удалить [<имя>]' или '-del [<имя>]', чтобы удалить контактные данные для имени или перейти в меню удаления \n\n\
 'просмотреть [<имя>]' или '-display [<имя>]', чтобы просмотреть контактные данные для имени или перейти в меню просмотра\n\n\
 'выход', чтобы выйти из программы\n\n  ")

    response, name = splitResponse(response)
    
    if response.lower().startswith('добавить') or response.lower().startswith('-add'):
        if len(name):
            add(name)
        else:
            add()
        
    elif response.lower().startswith('удалить') or response.lower().startswith('-del'):
        if len(name):
            delete(name)
        else:
            delete()
        
    elif response.lower().startswith('просмотреть') or response.lower().startswith('-display'):
        if len(name):
            display(name)
        else:
            display()
        
    elif response.lower().startswith('выход'):
        break           
    
try:
    f = open(addrBookFile, 'wb')
    pickle.dump(addrBook, f)
    f.close()
except:
    print('Ошибка при сохранении данных в файл: ', addrBookFile)
    

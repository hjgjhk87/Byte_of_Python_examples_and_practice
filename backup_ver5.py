import zipfile
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['E:\\books\\progit.ru.pdf', '"E:\\Новая папка"', 'C:\\hh_contest_result.txt']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.


# 2. Резервные копии должны храниться в основном каталоге резерва.

target_dir = 'E:\\Testing_backuping_with_Python'

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге резерва
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Создаем каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'

# 5. Используем команду "zipfile" для помещения файлов в zip-архив
#zip_command = "-m zipfile -c {0} {1}".format(target, ' '.join(source))

print(source[0])

# Запускаем создание резервной копии
myzip = zipfile.ZipFile(target, 'a')
myzip.write('E:\\Новая папка (2)\\1.txt')
myzip.close()

##    print('Резервная копия успешна создана в ', target)
##else:
##    print('Создание резервной копии НЕ УДАЛОСЬ')

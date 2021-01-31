'''
Имитация работы с БД с использованием бинарного файла.

Никишин Владимир Иу7-15Б
'''

import pickle as p  # Подключение библиотеки


def Show_menu():
    print('''
Меню:
1) Создать БД
2) Добавить запись в БД
3) Вывести всю базу данных
4) Найти записи по одному полю
5) Найти записи по двум полям
0) Выйти из программы 
'''
)


def Get_key_words():

    '''
    Функция возвращает список со значениями полей,
    которые задаются пользователем
    '''

    a = []
    size = int(input("Введите кол-во полей: "))
    for i in range(size):
        x = input("Введите название поля: ")
        a.append(x)
    return a


def Get_record(key_words):

    '''
    Функция возвращает словарь со значениями, выбранными пользователем:
    '''

    record = {}
    for word in key_words:
        print("Введите значение для поля", word)
        record[word] = input()
    return record


def Choice(key_words):

    '''
    Функия для выбора поля для поиска в БД.
    Возвращает ключ словаря.
    '''

    print("Для поиска поля по значению введите соответствующий ключ: ")
    for word in key_words:
        print(word)
    res = input()
    while res not in key_words:
        res = input("Введите корректное значение: ")
    return res


def Print_record(d:dict):
    for key, value in d.items():
        print("{0:s}: {1:s}, ".format(key, value), end='')
    print()


filename = 'data.bin'  # Имя бинарного файла
keys = []  # Названия полей
exist = True  # Существует ли файл

# Получаем названия полей из файла, если он существует
try:
    f = open(filename, 'rb')
    data = p.load(f)
    for key, value in data.items():
        keys.append(key)
    f.close()
except FileNotFoundError:
    exist = False

Show_menu()
while True:
    operation_code = input("Ваш выбор: ")  # Выбор пользователя

    if operation_code == '0':
        print("Программа завершена")
        break

    elif operation_code == '1':
        f = open(filename, 'wb')
        keys = Get_key_words()
        f.close()
        exist = True
        print("БД создана / очищена")

    elif operation_code == '2':
        if exist:
            f = open(filename, 'ab')
            dictionary = Get_record(keys)  # Запись для вставки
            p.dump(dictionary, f)  # Вставка
            f.close()
            print("Запись успешно добавлена")
        else:
            print("Файла не существует")

    elif operation_code == '3':
        if exist:
            f = open(filename, 'rb')
            # Пока не конец фала считываем записи
            while True:
                try:
                    Print_record(p.load(f))
                except EOFError:
                    break
            f.close()
        else:
            print("Файла не существует")

    elif operation_code == '4':
        if exist:
            n = Choice(keys)
            base = input("Введите искомое значение: ")

            f = open(filename, 'rb')
            while True:
                try:
                    data = p.load(f)
                    if data[n] == base:
                        Print_record(data)
                except EOFError:
                    break
            f.close()
        else:
            print("Файла не существует")

    elif operation_code == '5':
        if exist:
            n1 = Choice(keys)
            base1 = input("Введите искомое значение: ")
            n2 = Choice(keys)
            base2 = input("Введите искомое значение: ")
            f = open(filename, 'rb')
            while True:
                try:
                    data = p.load(f)
                    if data[n1] == base1 and data[n2] == base2:
                        Print_record(data)
                except EOFError:
                    break
            f.close()
        else:
            print("Файла не существует")

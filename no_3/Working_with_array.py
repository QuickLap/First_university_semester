'''
Программа c использованием меню позволяет:

1. Проинициализировать список первыми N элементами заданного ряда
    ряд: 1 + x/2 - x**2 / 2 / 4 + x**3 * 3 / 2 /4 / 6 - x**4 * 3 * 5 / 2 /4 /6 / 8 ...
2. Добавить элемент в произвольное место списка
3. Удалить произвольный элемент из списка
4. Очистить список
5. Найти значение K-го экстремума в списке, если он является списком чисел
6. Найти наиболее длинную последовательность чисел в которой все элементы, начиная с 3-го, являются суммой двух предыдущих
7. Найти последовательность, включающую в себя
   наибольшее количество cтрок, содержащих удвоенные согласные.

Никишин Владимир Иу7-15
'''

# Описание Меню
print('''Меню:
Для выбора команды соответственно введите:

1 - Проинициализировать список первыми N элементами заданного ряда
2 - Добавить элемент в заданное место списка
3 - Удалить заданный элемент из списка
4 - Очистить список
5 - Найти значение K-го экстремума в списке, если он является списком чисел
6 - Найти наиболее длинную последовательность чисел в которой все элементы,
    начиная с 3-го, являются суммой двух предыдущих
7 - Найти последовательность, включающую в себя
    наибольшее количество cтрок, содержащих удвоенные согласные.
0 - Для выхода из программы
''')

#TESTS
#A = [1,2,3,5,8,2,1,2,3,4,5,6,11,17,28,45,55,100] #Создание списка
#A = ["abba","peru","pinapple","swwa","asasas","clown_cрр","ahaahh","щща","yy"]
#A = [1,1,2,3,5,8]
#A = ["swwa","wwr","saw","llo"]

A = []  
eps = 1e-8

operation_code = "" # Команда, вводимая пользователем

while operation_code != "0":
    operation_code = input()

    # Выход из программы
    if operation_code == "0":
        print("Программа закрыта.")

    # Доавление элемента
    elif operation_code == "1":
        n = int(input("Введитe N ")) # Ввод кол-ва элементов
        x = float(input("Введитe X ")) # Ввод переменной для подсчета ряда
        value = x / 2
        coef = 1

        # Вычисление новых элементов ряда
        for i in range(1,n+1):
            if i == 1:
                value = 1
            elif i == 2:
                value = x/2
            else:
                value *= -1 * x * coef / (coef + 3)
                coef += 2
            A.append(value)
        print("Массив проинициализирован. Возврат в меню.")

    # Вставка элемента
    elif operation_code == "2":
        
        elem = input("Введите элмент для вставки ")

        # Проверка на то, является ли ввод числом
        count_point = 0
        count_e = 0
        int_flag = True
        float_flag = True
        for part in elem: 
            if part not in "1234567890":
                int_flag = False
            if part not in "1234567890.e+-":
                float_flag = False
            if part == "e":
                count_e += 1
            elif part == ".":
                count_point += 1
        # Преобразования к числу (при необходимости)
        if int_flag:
            elem = int(elem)
        elif float_flag and count_e < 2 and count_point < 2:
            elem = float(elem)

        ind = int(input("Введите индекс для вставки: От {0:d} До {1:d} ".format(0,len(A))))
        if ind < 0 or ind > len(A):
            print("Команда введена некорректно! Возврат в меню.")
        else:
            A.insert(ind, elem)
            print("Элемент успешно добавлен. Возврат в меню.")

    # Удаление элемента
    elif operation_code == "3":
        
        ind = int(input("Введите индекс для удаления: От {0:d} До {1:d} ".format(0,len(A) - 1)))
        if ind < 0 or ind > len(A) - 1:
            print("Команда введена некорректно! Возврат в меню.")
        else:
            A.pop(ind)
            print("Элемент успешно удален. Возврат в меню.")

    # Очищение массива
    elif operation_code == "4":
        
        A.clear()
        print("Список успешно очищен. Возврат в меню.")

    # Поиск экстремума
    elif operation_code == "5":
        
        if len(A) < 3:
            print("Список слишком мал для нахождения экстремумов. Возврат в меню.")
        else:
            k = int(input("Введите К "))
            curr_k = 0
            answer = -1

            #Проверка массива на наличие различных типов данных
            diffr_elements = False
            for elem in A:
                if type(elem) != float and type(elem) != int:
                    print("Cписок содержит не только числа. Невозможно посчитать K. Возврат в меню.")
                    diffr_elements = True
                    break
            if diffr_elements:
                continue

            # Поиск экстремумов
            for i in range(1,len(A) - 1):
                if (A[i-1] < A[i] and A[i+1] < A[i]) or (A[i-1] > A[i] and A[i+1] > A[i]):
                    curr_k += 1
                if curr_k == k:
                    answer = A[i]
                    break
            if answer == -1:
                print("К-го экстремума не существует. Возврат в меню.")
            else:
                print("Значение K-го экстремума в списке = {:.5g} , Возврат в меню.".format(answer))

    # Поиск числовой последовательности
    elif operation_code == "6":

        if len(A) < 3:
            print("Cписок содержит меньше 3 чисел. Возврат в меню.")
            continue

        result_array = [] # Искомая последовательность
        tmp_array = [] # Доп. последовательность

        # Поиск последовательности
        for i in range(2,len(A)):
            if (type(A[i]) != float and type(A[i]) != int) or \
               (type(A[i-1]) != float and type(A[i-1]) != int) or \
               (type(A[i-2]) != float and type(A[i-2]) != int):

                if len(tmp_array) > len(result_array):
                    result_array.clear()
                    for elem in tmp_array:
                        result_array.append(elem)
                    tmp_array.clear()
                else:
                    tmp_array.clear()
            else:    
                if abs(A[i] - A[i-1] - A[i-2]) < eps:
                    tmp_array.append(A[i])
                elif len(tmp_array) > len(result_array):
                    result_array.clear()
                    for elem in tmp_array:
                        result_array.append(elem)
                    tmp_array.clear()
                else:
                    tmp_array.clear()
                
        if len(tmp_array) > len(result_array):
            result_array.clear()
            for elem in tmp_array:
                result_array.append(elem)
            tmp_array.clear()

        for elem in result_array:
            print("{0:.5g} ".format(elem), end="")
        if len(result_array) == 0:
            print("Искомая последовательность отсутствует ",end="")
        print("\nВозврат в меню")

    # Поиск строчной последовательности 
    elif operation_code == "7":

        #Вычисления по анологии с числ. посл.        
        result_array = []
        tmp_array = []
        alphabet = ['bb', 'cc', 'dd', 'ff', 'gg','hh','jj','kk','ll','mm',
        			'nn','pp','qq','rr','ss','tt','vv','ww','xx','zz',
					'бб', 'вв', 'гг', 'дд', 'жж','зз','йй','кк','лл','мм',
					'нн','пп','рр','сс','тт','фф','хх','цц','чч','шш','щщ'] 

        for i in range(len(A)):
            has_two_letters = False
            if type(A[i]) != str:
                if len(tmp_array) > len(result_array):
                    result_array.clear()
                    for elem in tmp_array:
                        result_array.append(elem)
                    tmp_array.clear()
                else:
                    tmp_array.clear()
            else:
                for value in alphabet:
                    if A[i].lower().find(value) != -1:
                        has_two_letters = True

                if has_two_letters:
                    tmp_array.append(A[i])
                elif len(tmp_array) > len(result_array):
                    result_array.clear()
                    for elem in tmp_array:
                        result_array.append(elem)
                    tmp_array.clear()
                else:
                    tmp_array.clear()
                
        if len(tmp_array) > len(result_array):
            result_array.clear()
            for elem in tmp_array:
                result_array.append(elem)
            tmp_array.clear()

        for elem in result_array:
            print("{0:s} ".format(elem), end="")
        if len(result_array) == 0:
            print("Искомая последовательность отсутствует ",end="")
        print("\nВозврат в меню")
    	
    else:
        print("Команда введена некорректно! Возврат в меню.")

    print(A)
    

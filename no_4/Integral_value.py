'''
Никишин В И : метод правых прямоугольников, метод трапеций
'''

# Заданная функция
def Function(value:float):
    return value ** 2 + 1

# Заданная первообразная
def Integral(value:float):
    return 1/3 * value**3 + value

# Вывод для 2 задания
def Print_table(splits_count:int, answer:float, real_answer:float):
    abs_error = abs(real_answer - answer)
    other_error = abs((real_answer - answer) / real_answer)
    print("|{0:^29d}|{1:^29.7g}|{2:^29.7g}|{3:^29.7g}|".format(splits_count, answer, abs_error, other_error))
    print(('|' + '-' * 29) * 4 + '|')

# Метод правых прямоугольников
def Get_rect_integral(start_point:float, stop_point:float, split_count:int):
    step = (stop_point - start_point) / split_count
    new_start = start
    area = 0
    
    while new_start < stop:
        area += step * Function(new_start + step)
        new_start += step
    return area


# Метод трапеций
def Get_trap_integral(start_point:float, stop_point:float, split_count:int):
    step = (stop_point - start_point) / split_count
    new_start = start_point
    area = 0
    old_value = Function(new_start)
    
    while new_start < stop_point:
        new_value = Function(new_start + step)
        area += step * (old_value + new_value) / 2
        old_value = new_value
        new_start += step
    
    return area


# Ввод данных
start = float(input("Введите начальное значение "))
stop = float(input("Введите конечное значение "))
n1, n2 = map(int, input("Введите кол-во разбиений (2 натуральных числа) ").split())
eps = float(input("Введите точноcть "))

step_1 = (stop - start) / n1 # Шаг для 1 разбиения
step_2 = (stop - start) / n2 # Шаг для 2 разбиения

rect_method_1 = rect_method_2 = trap_method_1 = trap_method_2 = 0 # Будушие ответы

# Метод прямоугольников

rect_method_1 = Get_rect_integral(start, stop, n1)
rect_method_2 = Get_rect_integral(start, stop, n2)

# Метод трапеций

trap_method_1 = Get_trap_integral(start, stop, n1)
trap_method_2 = Get_trap_integral(start, stop, n2)

# Вывод таблицы
print(('|' + '-' * 29) * 3 + '|')

print("|{0:^29s}|{1:^29s}|{2:^29s}|".format("Метод", "n1 = %d" % n1, "n2 = %d" % n2))
print(('|' + '-' * 29) * 3 + '|')

print("|{0:^29s}|{1:^29.7g}|{2:^29.7g}|".format("Правых прямоугольников", rect_method_1, rect_method_2))
print(('|' + '-' * 29) * 3 + '|')

print("|{0:^29s}|{1:^29.7g}|{2:^29.7g}|".format("Трапеций", trap_method_1, trap_method_2))
print(('|' + '-' * 29) * 3 + '|\n')

# Задание № 2

print("Погрешности представлены для менее точного метода - правых прямоугольников")
print(('|' + '-' * 29) * 4 + '|')
print("|{0:^29s}|{1:^29s}|{2:^29s}|{3:^29s}|".format("Кол-во разбиений", "Значение", "Абс. ошибка", "Отн. ошибка"))
print(('|' + '-' * 29) * 4 + '|')
      
number_of_splits = 100

#Вычисление первых 2 значений
real_value = Integral(stop) - Integral(start)

old_answer = Get_rect_integral(start, stop, number_of_splits)
Print_table(number_of_splits, old_answer, real_value)

number_of_splits *= 2

new_answer = Get_rect_integral(start, stop, number_of_splits)
Print_table(number_of_splits, new_answer, real_value)

# Вычисление последующих значений
while abs(new_answer - old_answer) >= eps:
    number_of_splits *= 2
    old_answer = new_answer
    new_answer = Get_rect_integral(start, stop, number_of_splits)
    Print_table(number_of_splits, new_answer, real_value)




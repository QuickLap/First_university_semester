'''
Никишин Владимир Иу7-15
'''

def Get_coef(string_end: str):
    while string_end[0] == ' ':
        string_end = string_end[1:]
    return int(string_end[:string_end.find(' ')])


def Get_names(string: str):
    return string[1:6], string[6:11]


def Get_distances(tree, row_number, tree_size, distance=0):
    results = {}
    for i in range(tree_size):
        curr_distance = tree[row_number][i]
        if (curr_distance is not None) and (curr_distance > 0):
            results.update({i: distance + curr_distance})
            results.update(Get_distances(tree, i, tree_size, distance + curr_distance))
    return results


def Get_distances_with_zero_coef(tree, row_number, tree_size, distance=0, count_zeros=True):
    results = {}
    for i in range(tree_size):
        curr_distance = tree[row_number][i]
        if curr_distance is not None:
            if curr_distance > 0:
                results.update({i: distance + curr_distance})
                results.update(Get_distances_with_zero_coef(tree, i, tree_size,
                                                            distance
                                                            + curr_distance))
            elif curr_distance == 0 and count_zeros:
                results.update({i: distance + curr_distance})
                results.update(Get_distances_with_zero_coef(tree, i, tree_size, distance + curr_distance, False))
    return results


filename = "input.txt"
dictionary = {}
matrix = list([] for i in range(1))
matrix_size = 0

with open(filename, 'r') as file_handler:
    for line in file_handler:
        operation_code = line[0]

        if operation_code == '#':
            continue

        elif operation_code == 'R':
            # Обработка строки
            first_name, second_name = Get_names(line)
            coef = Get_coef(line[11:])

            # Заполнение словаря и увеличение размера матрицы
            for elem in first_name, second_name:
                if elem not in dictionary:
                    dictionary.update({elem: len(dictionary)})
                    if matrix_size != 0:
                        matrix.append([None] * len(matrix[0]))
                    for row in matrix:
                        row.append(None)
                    matrix_size += 1

            # Заполнение матрицы
            matrix[dictionary[first_name]][dictionary[second_name]] = coef
            if coef == 0:
                matrix[dictionary[second_name]][dictionary[first_name]] = coef

        elif operation_code == 'F':
            # Обработка строки
            first_name, second_name = Get_names(line)

            if (first_name not in dictionary) or (second_name not in dictionary):
                print("{0:^5s} и {1:^5s} не являются родственниками".format(first_name, second_name))
            else:
                first_ind, second_ind = dictionary[first_name], dictionary[second_name]

                # Вычисление "расстояний" до предков выбранных личностей
                dict_1 = Get_distances(matrix, first_ind, matrix_size)
                dict_1.update({first_ind: 0})

                dict_2 = Get_distances_with_zero_coef(matrix, second_ind, matrix_size)
                dict_2.update({second_ind: 0})

                # Определение степени родства
                min_distance = float('+inf')
                distance_1 = distance_2 = -1

                for key_1 in dict_1:
                    for key_2 in dict_2:
                        if key_1 == key_2 and dict_1[key_1] + dict_2[key_2] < min_distance:
                            min_distance = dict_1[key_1] + dict_2[key_2]
                            distance_1, distance_2 = dict_1[key_1], dict_2[key_2]

                if (distance_1 == distance_2 == -1) or (first_name == second_name):
                    print("{0:^5s} и {1:^5s} не являются родственниками".format(first_name, second_name))
                elif distance_1 == 0 and distance_2 == 0:
                    print("{0:^5s} и {1:^5s} являются кузин-0-0".format(first_name, second_name))
                elif distance_1 == 0 or distance_2 == 0:
                    print("{0:^5s} и {1:^5s} являются потомком-{2:d}".format(first_name,
                                                                             second_name,
                                                                             max(distance_1, distance_2)))
                else:
                    print("{0:^5s} и {1:^5s} являются кузин-{2:d}-{3:d}".format(first_name,
                                                                                second_name,
                                                                                min(distance_2, distance_1) - 1,
                                                                                abs(distance_2 - distance_1)))

        elif operation_code == 'E':
            break

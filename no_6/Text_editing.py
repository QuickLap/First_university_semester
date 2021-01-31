'''
Программа работает с заданным текстом и может выполнять:

1. Выравнивание текста по левому краю.
2. Выравнивание текста по правому краю.
3. Выравнивание текста по ширине.
4. Удаление заданного слова.
5. Замену одного слова другим во всем тексте.
6. Вычисление арифметического выражения.
7. Нахождение предложения с максимальным количеством слов, начинающихся на заданную букву.
8. Вывод текст на экран.

Никишин Владимир Иу7-15
(Текст взят из aillarionov LiveJournal)
'''

from math import pow, sqrt


def Deleted_spaces(element):
	'''

	Функция удаляет лишние пробелы в строке,
	также добавляет в конец 1 пробел, в случае его отсутствия.

	Возвращает измененную строку, либо пустую строку, в случае
	отсутствия в исходной строке символов, отличных от пробела.

	'''
	element = ' '.join(element.split())
	if len(element) == 0:
		return ""
	if element[0] == ' ':
		element = element[1:]
	if element[-1] != ' ' and element[-1] != ',' and element[-1] != '.':
		element += ' '
	return element


def Move_spaces(text, str_length, method:str):
	'''

	Функция для выравнивания текста в зависимости
	от параметра method:
	method = "left" - выравнивание слева
	method = "right" - выравнивание справа
	method = "middle" - выравнивание по ширине

	'''
	for index, elem in enumerate(text):
		elem = Deleted_spaces(elem)  # Полное удаление лишних пробелов
		spaces_add_count = str_length - len(elem)  # кол-во пробелов, необходимое для выравнивания
		if method == "left":
			text[index] = elem + ' ' * spaces_add_count
		elif method == "right":
			text[index] = (' ' * spaces_add_count) + elem
		elif method == "middle":
			words_count = elem.count(' ')
			if elem[-1] != ' ':
				words_count += 1
			else:
				elem = elem[:-1]
			if words_count == 1:
				text[index] = elem + ' ' * spaces_add_count  # вкенргшолщвкаенптргшоьл
				'''
				text[index] = ' ' * (spaces_add_count //2) + elem + ' ' * (spaces_add_count //2)
				if spaces_add_count % 2 == 1:
					text[index] += ' '
				'''
			else:
				spaces_per_word = (spaces_add_count // (words_count - 1))
				trash = spaces_add_count - spaces_per_word * (words_count - 1)
				answer = ""
				for ch in elem:
					if ch == " ":
						answer += ' '
						answer += ' ' * spaces_per_word
						if trash > 0:
							answer += ' '
						trash -= 1
					else:
						answer += ch
				text[index] = answer


def Change_word(text, word_for_check, word_for_paste="", change_method=False):
	'''

	Функция для удаления слова из текста, либо замены на другое.

	·параметр word_for_paste вводится в случае с заменой слова word_for_check
	·параметр change_method:
		= True  в случае с заменой слова word_for_check
		= False в случае с удаления слова word_for_check (по умлочанию)

	'''
	special_symbols = ['.', ',', '!', ':', '(', ')', ';', ' ', '*']
	for index, elem in enumerate(text):
		answer = ""  # Строка, полученная в результате изменений
		curr_word = ""  # Текущее слово
		curr_ind = 0  # Индекс для подсчета конца текущего слова
		while len(elem) > 0:
			if elem[curr_ind] not in special_symbols:
				curr_word += elem[curr_ind]
				curr_ind += 1
			else:
				if curr_word != word_for_check:
					answer += curr_word
				elif change_method:  # В случае замены слова:
					answer += word_for_paste
				answer += elem[curr_ind]
				elem = elem[curr_ind + 1:]
				curr_ind = 0
				curr_word = ""
		text[index] = answer


def Find_expression(text):
	'''

	Функция находит арифметическое выражение в тексте

	Возвращает строку - арифм. выражение, если оно имеется в тексте,
	в противном случае возвращает пустую строку.

	'''
	special_symbols = ['+', '-', '*', '(', ')', '/', '√', '^']
	numbers = "1234567890"
	unique_symbols = "+-*/√^" # Символы встречающиеся в тексте только в арифм. выражении
	answer = ""
	for elem in text:
		for index, ch in enumerate(elem):
			if ch in unique_symbols:
				index_plus = index - 1
				while index_plus >= 0 and (elem[index_plus] in numbers or elem[index_plus] in special_symbols):
					answer = elem[index_plus] + answer
					index_plus -= 1
				while index < len(elem) and (elem[index] in numbers or elem[index] in special_symbols):
					answer += elem[index]
					index += 1
				return answer
	return ""


def Calculate(expression: str):
	'''

	Рекурентная функция. Подсчитывает выражение в виде строки.

	Возвращает строку с численным ответом.

	'''

	operators = ['+','^','-','*','/','√']

	while '(' in expression:
		stop = start = expression.rfind('(')
		while expression[stop] != ')':
			stop += 1
		answer = Calculate(expression[start + 1:stop])
		expression = expression[:start] + answer + expression[stop + 1:]

	if len(expression) > 0 and expression[0] == '-':
		expression = '?' + expression[1:]

	if '??' in expression:
		position = expression.find('??')
		expression = expression[:position] + expression[position + 2:]

	while '√' in expression:
		middle = right = expression.find('√')
		right += 1
		while right < len(expression) and expression[right] not in operators:
			right += 1
		right_number = expression[middle + 1: right]
		print(right_number)
		answer = str(sqrt(float(right_number)))
		expression = expression[:middle] + answer + expression[right:]

	while '^' in expression:
		middle = left = right = expression.find('^')
		left -= 1
		right += 1
		while left >= 0 and expression[left] not in operators:
			left -= 1
		while right < len(expression) and expression[right] not in operators:
			right += 1
		left += 1

		left_number = expression[left: middle]
		right_number = expression[middle + 1: right]

		if left_number[0] == '?':
			left_number = '-' + left_number[1:]
		if right_number[0] == '?':
			right_number = '-' + right_number[1:]

		answer = pow(float(left_number), float(right_number))

		if answer < 0:
			answer = '?' + str(answer)[1:]
		else:
			answer = str(answer)

		expression = expression[:left] + answer + expression[right:]

	while '*' in expression or '/' in expression:
		if expression.find('/') == -1 or expression.find('*') == -1:
			middle = left = right = max(expression.find('/'), expression.find('*'))
		else:
			middle = left = right = min(expression.find('/'), expression.find('*'))

		left -= 1
		right += 1

		while left >= 0 and expression[left] not in operators:
			left -= 1
		while right < len(expression) and expression[right] not in operators:
			right += 1
		left += 1

		left_number = expression[left: middle]
		right_number = expression[middle + 1: right]

		if left_number[0] == '?':
			left_number = '-' + left_number[1:]
		if right_number[0] == '?':
			right_number = '-' + right_number[1:]

		if expression[middle] == '/':
			answer = float(left_number) / float(right_number)
		else:
			answer = float(left_number) * float(right_number)

		if answer < 0:
			answer = '?' + str(answer)[1:]
		else:
			answer = str(answer)

		expression = expression[:left] + answer + expression[right:]


	while '+' in expression or '-' in expression:
		if expression.find('+') == -1 or expression.find('-') == -1:
			middle = left = right = max(expression.find('+'), expression.find('-'))
		else:
			middle = left = right = min(expression.find('+'), expression.find('-'))

		left -= 1
		right += 1

		while left >= 0 and expression[left] not in operators:
			left -= 1
		while right < len(expression) and expression[right] not in operators:
			right += 1
		left += 1

		left_number = expression[left: middle]
		right_number = expression[middle + 1: right]

		if left_number[0] == '?':
			left_number = '-' + left_number[1:]
		if right_number[0] == '?':
			right_number = '-' + right_number[1:]

		if expression[middle] == '+':
			answer = float(left_number) + float(right_number)
		else:
			answer = float(left_number) - float(right_number)

		if answer < 0:
			answer = '?' + str(answer)[1:]
		else:
			answer = str(answer)

		expression = expression[:left] + answer + expression[right:]

	return expression


def Find_sentence(text, symbol):
	'''

	Функция находит и возвращает предложение с максимальным
	количеством слов, начинающихся на заданную букву.

	'''
	special_symbols = ['.', ',', '!', ':', '(', ')', ';', ' ', '*']
	answer = ""  # Искомая строка
	curr_answer = ""  # Текущая строка
	max_count = count = 0  # Кол-ва слов, на заданную букву
	for index, elem in enumerate(text):
		for i in range(len(elem)):
			curr_answer += elem[i]
			if elem[i] == symbol and (i == 0 or elem[i-1] in special_symbols):
				count += 1
			elif elem[i] == '.' or elem[i] == '!' or elem[i] == '?':
				if count > max_count:
					answer = curr_answer
					max_count = count
				count = 0
				curr_answer = ""
	return answer


def Print_text(text):
	'''

	Функция выводит текст на экран.

	'''
	for elem in text:
		print(elem)


def Change_strings_length(text):
	strings_length = max(len(elem) for elem in text)  # Длина максимальной строки в тексте
	for ind, item in enumerate(text):
		input_text[ind] += ' ' * (strings_length - len(item))  # Преобразование строк текста к единой длине


def Show_menu():
	print('''Меню:
1. Выравнивание текста по левому краю.
2. Выравнивание текста по правому краю.
3. Выравнивание текста по ширине.
4. Удаление заданного слова.
5. Замена одного слова другим во всем тексте.
6. Вычисление арифметического выражения.
7. Найти предложение с максимальным количеством слов, начинающихся на заданную букву.
8. Вывести текст на экран.
0. Выход из программы.''')


'''
(2^(-1)-(-(-31)))
(-(-1/(-(-2))))*(27-5^2)
√(-(-1/(-(-2)))*4)
((3-2)*5)-4/3+(1-22/32))
'''

input_text = [
	"Взято из aillarionov LiveJournal. ",
	"Мотивированное феодальное дворянство, составлявшее не ",
	"более одного процента населения многих стран средневековой ",
	"Европы, эффективно контролировало (и эксплуатировало) крестьянство,",
	" примерно в сто раз превосходившее дворянство по своей численности,",
	" время от времени восстававшее в ходе крестьянских войн, ни одна",
	" из которых в исторической перспективе так и ",
	"не оказалась успешной. Сформулируем ответ на интересующий общественность",
	" вопрос о необходимых 4 условиях отставки не пользующегося",
	" общественной поддержкой режима для четырех вариантов ",
	"политической ситуации. Главными параметрами этих вариантов являются:",
	"1 : характер политического режима, ",
	"√(-(-1/(-(-2)))*4): степень соблюдения режимом требований верховенства права, ",
	"3 : готовность к использованию режимом насилия (избирательного, массового) против своих оппонентов.",
	"В условиях свободного политического режима, опирающегося на безусловное",
	" соблюдение всеми участниками политического процесса жестких требований ",
	"верховенства права, для смены власти достаточно лишь победы оппозиции ",
	"на честно проведенных президентских или парламентских выборах; при этом",
	" дополнительной мобилизации граждан для защиты корректно объявленных",
	" результатов выборов не требуется. В условиях мягкого авторитарного режима,",
	" не соблюдающего базовые требования верховенства права, но не готового",
	" применять насилие против своих оппонентов, для смены политической",
	" власти необходима массовая мобилизация граждан, готовых защищать",
	" результаты выборов (или иным образом выявленное волеизъявление граждан), ",
	"принимающая форму ненасильственной бархатной революции ",
	"В условиях мягкого авторитарного режима, не соблюдающего базовые требования",
	" верховенства права, но готового применять избирательное насилие против",
	" своих оппонентов, смена политической власти требует массовой",
	" мобилизации граждан, их отказа от инструментов только ненасильственного",
	" сопротивления, следовательно, применения ими избирательного насилия против ",
	"сил сопротивляющегося режима. В условиях жесткого авторитарного режима,",
	" игнорирующего базовые требования верховенства права, готового применять",
	" систематическое насилие против своих оппонентов, смена политической власти",
	" требует массовой мобилизации граждан, их отказа от инструментов только",
	" ненасильственного сопротивления, следовательно, применения ими систематического",
	" насилия."
]

Change_strings_length(input_text)
Show_menu()

while True:

	strings_length = max(len(elem) for elem in input_text)  # Длина максимальной строки в тексте
	operation_code = input("Ваш выбор:")

	if operation_code == '0':
		print("Программа завершена.")
		break

	elif operation_code == '1':
		Move_spaces(input_text, strings_length, "left")

	elif operation_code == '2':
		Move_spaces(input_text, strings_length, "right")

	elif operation_code == '3':
		Move_spaces(input_text, strings_length, "middle")

	elif operation_code == '4':
		w = input("Введите слово для удаление из текста: ")
		Change_word(input_text, w)
		Change_strings_length(input_text)

	elif operation_code == '5':
		w1 = input("Введите слово для удаления из текста: ")
		w2 = input("Введите слово для вставки в текст: ")
		Change_word(input_text, w1, w2, True)
		Change_strings_length(input_text)

	elif operation_code == '6':
		string_number = -1
		string_expression = Find_expression(input_text)
		for i in range(len(input_text)):
			if string_expression in input_text[i]:
				string_number = i
				pos1 = input_text[i].find(string_expression)
				pos2 = pos1 + len(string_expression)
		if len(string_expression) > 0:
			result = Calculate(string_expression)
			if result[0] == '?':
				result = '-' + result[1:]
			if string_number != -1:
				input_text[string_number] = input_text[string_number][:pos1] + result + input_text[string_number][pos2:]
			print(string_expression, '=', result)
		else:
			print("Арифметическое выражение не найдено в тексте.")
		Change_strings_length(input_text)


	elif operation_code == '7':
		char = input("Введите символ: ")
		output_string = Deleted_spaces(Find_sentence(input_text, char))
		if len(output_string) == 0:
			print("Такого предложения нет.")
		else:
			print("Искомое предложение:\n", output_string)

	elif operation_code == '8':
		Print_text(input_text)


'''

Программа позвлояет зашифровать / расшифровать заданную строку
с использованием заданного ключ-слова.

Иу7-15 Никишин Владимир

'''

def Encrypt(word:str, key_word:str, alphabet:str):
	
	'''
	Функция для шифрования сообщения. Получает на вход
	исходное слово, ключ-слово, алфавит(латнинца)
	'''
	
	answer = ""
	i = k = 0 # индексы для вычислений
	
	while i < len(word):
		# Элемент для шифрования
		elem = word[i].lower()
		
		#Проверка на регистр
		is_uppercase = word[i].isupper()
		
		if elem not in alphabet:
			answer += elem
			i += 1 # +Шаг
			continue

		# Попарный элемент для шифрования
		elem_2 = key_word[k%len(key_word)]
			
		# Находим индекс зашифрованного элементоа в алфавите
		ans_ind = (alphabet.index(elem) + alphabet.index(elem_2)) % len(alphabet)

		# Добовляем полученный элемент к полному ответу
		if is_uppercase:
			answer += alphabet[ans_ind].upper()
		else:
			answer += alphabet[ans_ind]
		
		# +Шаг
		i += 1
		k += 1
		
	return answer
	

def Decrypt(word:str, key_word:str, alphabet:str):
	
	'''
	Функция для расшифровки сообщения. Получает на вход
	исходное слово, ключ-слово, алфавит(латнинца)
	'''
	
	answer = ""
	i = k = 0 # индексы для вычислений
	
	while i < len(word):
		# Элемент для расшифровки
		elem = word[i].lower()
		
		#Проверка на регистр
		is_uppercase = word[i].isupper()
		
		if elem not in alphabet:
			answer += elem
			i += 1 # +Шаг
			continue
		
		# Попарный элемент для расшифровки
		elem_2 = key_word[k%len(key_word)]
		
		# Находим индексы расшифрованного элементоа в алфавите
		ans_ind = (alphabet.index(elem) - alphabet.index(elem_2) + len(alphabet)) % len(alphabet)
		
		# Добовляем полученный элемент к полному ответу
		if is_uppercase:
			answer += alphabet[ans_ind].upper()
		else:
			answer += alphabet[ans_ind]
		
		# +Шаг
		i += 1
		k += 1

	return answer

	
print('''Меню:
 1) Ввод строки
 2) Настройка шифрующего алгоритма
 3) Шифрование строки используя шифр Виженера
 4) Расшифрование строки
 0) Выход из программы
''')

my_alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
	operation_code = input("Ваш выбор: ")
	if operation_code == '0':
		break
	
	elif operation_code == '1':
		s = input("Введите строку: ")
	
	elif operation_code == '2':
		key = input("Введите ключ шифрования: ").lower()
	
	elif operation_code == '3':
		s = Encrypt(s,key,my_alphabet)
		print("Зашифрованная строка: %s" % s)
	
	elif operation_code == '4':
		s = Decrypt(s,key,my_alphabet)
		print("Расшифрованная строка: %s" % s)


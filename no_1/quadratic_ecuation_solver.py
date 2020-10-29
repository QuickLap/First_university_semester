
'''
Программа вычисляет корни квадратного уравнения вида a*x^2+b*x+c = 0

Никишин Владимир Иу7-15
'''

from math import sqrt #Подключение библиотек

#Ввод данных
a = float(input('''Введите входные данные:
Коэфициенты уравнения вида ax^2+bx+c=0
a = '''))
b = float(input("b= "))
c = float(input("c= "))


if a!=0:
    d = b*b-4*a*c

    if d < 0:
        print("Решений нет")
    elif d == 0:
        x = -b/2/a
        print("x = {0:.4g}".format(x))
    else:
        x1 = (-b-sqrt(d))/2/a
        x2 = (-b+sqrt(d))/2/a
        print("x1 = {0:.4g}, x2 = {1:.4g}".format(x1,x2))
elif b ==0:
    print("Решений нет" if c!=0 else "Решений бесконечно много")
else:
    x = -c/b
    print("x = {0:.4g}".format(x))

# Алгоритмы на Python 3. Лекция №4
# Практика: http://judge.mipt.ru/mipt_cs_on_python3/
# Видео - https://www.youtube.com/watch?v=DvsCUI5FNnI
# Практика - https://github.com/mipt-cs/course-site-python3/wiki

# курс: Информатика. Алгоритмы и структуры данных на Python 3.
# лектор: Хирьянов Тимофей Фёдорович
# 26.09.2017

# Темы, рассмотренные на лекции №4:
# - Описание простых функций с параметрами.
# - Декомпозиция задачи.
# - Структурное программирование. Проектирование «сверху-вниз».
# - Стек вызовов.
# - Полиморфизм в Python. Duck typing.
# - Значения параметров по умолчанию.
# - Именованные параметры функций
# - Мастер-класс по структурному программированию на проекторе
# - Метод грубой силы.
# - Тест простоты числа.
# - Разложение числа на множители.

# Функции
def hello():
    print('Hello, World')
hello()
f = hello
f()

# Функция с формальным параметром
def hello(name):
    print('Hello,', name)
hello('John')
hello('Alice')
hello('Peter')

# Функция со значением параметра по умолчанию
def hello(name='Mario'):
    print('Hello,', name)
hello()

# Функция сравнения двух числе
def max2(x,y):
    if x>y:
        return x # return - прекращает выполнение Функции!!!
    return y # else: можно не писать
print(max2(10,7)) # Вывод на экран большего из двух чисел - 10 и 7

# Функция сравнения трех чисел
def max3(x,y,z):
    return max2(x,max2(y,z)) # Сравнение при помощи, ранее написаной, функции max2. Функция max3 два раза вызывает функцию max2!!!
print(max3(3,5,7)) # Вывод на экран большего из трех чисел - 3, 5, 7
print(max3('ab','abc','abd')) # Duck Typing - если что-то выглядит как Утка, крякает как утка, то это - Утка. 
                              # Лексикографический порядок сравнения строк. Буква D старше (дальше по алфавиту), чем С.
                              # "Кот" меньше, чем "Котенок" - больше букв в слове, слово позже записано в словаре. 

# Раздельный Hello. Hello с условиями.
def hello_separated(name="World", separator="-"): # Разделитель "-" - тире.
    print("Hello,", name, sep=separator)
hello_separated("John","***")
hello_separated(separator="***", name="John") # Другой порядок параметров также возможен. Именованные параметры.

# Структурное программирование
# 
# Проектирование "сверху-вниз"

import graphics as gr

def build_house(window, upper_left_corner, width):
    """ Функция, которая рисует Дом """
    # height = calculate_height(width)
    pass
    
window = gr.GraphWin("Russian Game", 300,300)
build_house(window, gr.Point(100,100), 100)
print("Ура! Дом построен!")
input()

# Метод грубой силы - Brute Force

# Тест простоты числа
def is_simple_number(x):
    """ Определяет является ли число простым. x - целое положительное число. Если простое, то возвращает True, а иначе - False """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor +=1
    return True

# Разложение числа на множители
def factorize_number(x):
    """ Раскладывает число на множители. Печатает их на экран. x - целое положительное число. """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1


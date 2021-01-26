# Алгоритмы на Python 3. Лекция №3
# Практика: http://judge.mipt.ru/mipt_cs_on_python3/
# Видео - https://www.youtube.com/watch?v=b8m9uRMpKJk
# Практика - https://github.com/mipt-cs/course-site-python3/wiki

# курс: Информатика. Алгоритмы и структуры данных на Python 3.
# лектор: Хирьянов Тимофей Фёдорович
# прочитана 19.09.2017

# Темы, рассмотренные на лекции №3:
# - Позиционные системы счисления
# - Литералы чисел в Python
# - Разложение числа на цифры.
# - Однопроходные алгоритмы без реализации.

# Вывод числа в разных системах исчисления в Python 3

# x = int(input())
# print('BIN:', bin(x))
# print('OCT:', oct(x))
# print('HEX:', hex(x))
# print('DEC:', x)

# Перевод числа в произвольную систему исчисления

print('BASE?') #Ввод основания системы исчисления - 2, 4, 8, 10, 16 и т.д.
BASE = int(input())

print('Input Digit:') #Ввод числа
x = int(input())

while x>0:
    digit = x%BASE # Получаем последнюю цифру числа
    print(digit, end='') # Вывод чисел в обной строке без перехода на новую строку
    x //= BASE # Зачеркиваем (убираем) последнюю цифру числа


# Однопроходные алгоритмы

# Подсчет - n, начальное состояние = 0, n += 1
# Сумма - s, начальное состояние = 0, s += x
# Произведение - p, начальное состояние = 1, p *= x
# Максимум - m, начальное состояние = 0, m = max(max,x) или if x>m: m=x
# Поиск числа - f, начальное состояние = False,  f = f or (x==x0)

# Алгоритмы на Python 3. Лекция №8
# Практика: http://judge.mipt.ru/mipt_cs_on_python3/
# Видео - https://www.youtube.com/watch?v=2XFaK3bgT7w
# Практика - https://github.com/mipt-cs/course-site-python3/wiki

# курс: Информатика. Алгоритмы и структуры данных на Python 3.
# лектор: Хирьянов Тимофей Фёдорович
# 24.10.2017

# Темы, рассмотренные на лекции №8:
# - Генерация комбинаторных объектов.
# - Рекурсивная генерация всех чисел длины M.
# - Генерация всех перестановок (рекурсивная).
# - Быстрые сортировки: Тони Хоара и слиянием (без реализации).

# Генерация всех перестановок
# Для двоичной системы счисления
def gen_bin(M,prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)

# gen_bin(3) # Вызов функции для числа из трех разрядов

# Для N-ричной системы счисления
def generate_numbers(N:int, M:int, prefix=None): # N - основание системы исчисления, M - длина числа (кол-во разрядов)
    """ Функция генерирует все числа (с лидирующими незначащими нулями) в N-ричной системе счисления (N <= 10) длины M. """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

generate_numbers(3,3)

def find(number, A):
    """ Функция ищет number в А и возвращает True, если такой есть или False, если такого нет. """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Функция генерирует все перестановки N чисел в M позициях с префиксом prefix """
    M = N if M == -1 else M # По умолчанию N чисел в N позициях
    # if M == -1:
    #     M = N # По умолчанию N чисел в N позициях. То же самое, но длиннее.
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range (1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

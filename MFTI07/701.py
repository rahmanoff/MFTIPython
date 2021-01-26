# Алгоритмы на Python 3. Лекция №7
# Практика: http://judge.mipt.ru/mipt_cs_on_python3/
# Видео - https://www.youtube.com/watch?v=0Bc8zLURY-c
# Практика - https://github.com/mipt-cs/course-site-python3/wiki

# курс: Информатика. Алгоритмы и структуры данных на Python 3.
# лектор: Хирьянов Тимофей Фёдорович
# 17.10.2017

# Темы, рассмотренные на лекции №7:
# - Рекурсия.
# - Сказка "Репка" и изготовление матрёшки.
# - Прямой и обратный ход рекурсии.
# - Фрактальный квадрат в квадрате.
# - Факториал числа.
# - Алгоритм Евклида.
# - Быстрое возведение в степень.
# - Ханойские башни.

# Рекурсия

# В процессе углубления в рекурсию - Подзадача проще, чем задача!!!
# - Репка
# Мышка в Репке - крайний случай рекурсии
# Все остальные в Репке - рекурентные случаи

# У рекурсии должен быть рекурентный случай и крайни случай!!!

# Переполнение стека: так делать нельзя!
# def f():
#   f()

# Матрешка
def matryoshka(n):
   if n == 1: # Проверка - является ли текущий случай крайним, если да, то выводим сообщение
      print("Матрешечка")
   else:
      print("Верх матрешки n=", n)
      matryoshka(n-1)
      print("Низ матрешки n=", n)

matryoshka(5)

# Глубина рекурсии должна быть определена

# Фрактальный квадрат
import graphics as gr
window = gr.GraphWin("Fractal Rectangle", 500, 500)
alpha = 0.1 # Коэффициент сдвига по стороне квадрата

def fractal_rectangle(A, B, C, D, deep=10): # A,B,C,D - кортежи (пары чисел через запятую) с координатами точек квадрата, deep - глубина рекурсии, в данном случае - 10
   if deep < 1: # Проверяем сколько осталось нарисовать прямоугольников. Если 0, то выходим из функции.
      return
   gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)  # *A - функция разворачивания кортежа - использует значения кортежа A[0], A[1], A[2] и т.д.
   gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
   gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
   gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)

   # или тоже самое, но короче:
   # for M,N in (A,B), (B,C), (C,D), (D,A):
   #      gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

   A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha) # Вычисляем координаты новых точек
   B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
   C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
   D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)

   fractal_rectangle(A1, B1, C1, D1, deep-1)
   
fractal_rectangle((0,0), (500,0), (500,500), (0,500), 100)

# Факториал
# n! = (n-1)! * n - то, как делать не нужно!
def f(n:int):
   assert n>=0, "Факториал отрицательного числа не определен!"
   if n == 0:
      return 1
   return f(n-1)*n

# Алгоритм Евклида - Наибольший Общий Делитель - Grand Common Devisor
# 1-й Вариант
def gcd(a,b): # Считаем, что a и b - целые числа
   if a == b:
      return a
   elif a > b:
      return gcd(a-b,b)
   else: # a < b
      return gcd(a,b-a)

# 2-й вариант
def gcd(a,b):
   if b == 0:
      return a
   else:
      return gcd(a,a%b)
# или
def gcd (a,b):
   return a if b == 0 else gcd(b, a%b)

# Быстрое возведение в степень
def pow(a:float, n:int): # Принимаем, что n > 0 и целое число
   if n == 0:
      return 1
   elif n%2 == 1: # когда n - нечетное
      return pow(a,n-1)*a
   else: # когда n - четное
      return pow(a**2, n//2)

# Ханойские башни
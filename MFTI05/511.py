# Задача A-Принадлежность точки кругу

# Даны координаты точки и радиус круга с центром в начале координат. 
# Определить, принадлежит ли данная точка кругу. Напомним, что круг – это часть плоскости, 
# состоящая из всех точек окружности и всех точек, лежащих внутри окружности.

# Формат входных данных
# Три целых числа на одной строке: координата точки по оси x, координата точки по оси y, радиус круга r (r > 0).

# Формат выходных данных
# Вывести "YES" без кавычек, если точка принадлежит кругу, "NO" без кавычек в противном случае.

import math
# Ввод 3 чисел через пробел. 1 - координата точки по Х, 2 - координата точки по Y, 3 - радиус круга
A = list(map(int,input().split()))
# Рассчет расположения точки
n = math.sqrt(A[0]**2+A[1]**2)
# Сравнение расположения точки и радиуса круга
if n <= A[2]:
    print('YES')
else:
    print('NO')
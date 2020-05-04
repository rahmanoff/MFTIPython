import turtle as t
import math as m

t.shape('turtle')
t.pencolor("black")
# Vars:
loops = 0               # Начальное количество итераций для отрисовки многоугольников:
n = 3                   # Количество сторон многоугольника N > 3
r = 15                  # Начальный радиус окружности. (иначе говоря точка на оси X)
                        # Формула радиуса  R = a / 2 * m.sin(180) / n) но тут нам не пригодится,
                        # так как смещать будем по оси X а не произвольно.
# def:
def polygon(n,L):
    a = (n - 2) * 180 / n   # Угол между вершинами многоугольника
    for i in range(n):
        t.right(180 - a)
        t.forward(L)
while loops < 10:
    L = 2 * r * m.sin(m.pi / n)   # Длинна стороны многоугольника
    ang = ((n - 2) * 180/n) / 2  # Угол поворота каждого построенного многоугольника
    t.right(ang)                        # Поворачиваем на угол ang
    polygon(n, L)                     # Рисуем многоугольник
    t.left(ang)                         # Возвращаем угол в исходное положение.
    t.penup()
    t.forward(15)                # Смещаем на расстояние по оси X
    t.pendown()
    r += 15                      # Увеличиваем радиус на расстояние между многоугольниками, для увелечения длинны L
    n += 1                       # Увеличиваем количество сторон многоугольника
    loops += 1                 # Увеличиваем итерацию
t.mainloop()
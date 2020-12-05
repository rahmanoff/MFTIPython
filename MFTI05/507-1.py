# Моделирование движения материальной точки

# Равномерное движение
# Подключаем библиотеку для работы с графикой
import graphics as gr

# Задаем размер окна программы
SIZE_X = 1200
SIZE_Y = 720
# Выводим окно программы
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

# Равномерное движение шарика на плоскости
# Начальное положение шарика
coords = gr.Point(200, 200)
# Скорость шарика

# Функция суммы двух векторов
def add(point_1, point_2):
    new_point = Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point

# Процесс отрисовки шарика
def draw_circle(coords):
    circle = gr.Circle(coords,10)
    circle.setFill('red')

    #circle.draw(window)
i = 1
# Рассчитываем координаты шарика и отрисовываем его в полученных координатах
while True:
    
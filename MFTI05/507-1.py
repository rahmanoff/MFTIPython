# Моделирование движения материальной точки

# Равномерное движение
# Подключаем библиотеку для работы с графикой
import graphics as gr

# Задаем размер окна программы
SIZE_X = 1200
SIZE_Y = 600
# Выводим окно программы
window = gr.GraphWin("Моделирование движения материальной точки", SIZE_X, SIZE_Y)

# Равномерное движение шарика на плоскости
# Начальное положение шарика
coords = gr.Point(16, 16)
# Скорость шарика
velocity = gr.Point(1,-2)
# Ускорение
acceleration = gr.Point(0, 0.1)

# Функция суммы двух векторов
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point

# Процесс отрисовки шарика
def draw_ball(coords):
    circle = gr.Circle(coords,10)
    circle.setFill('red')
    circle.draw(window)

# Отражение от стенок
def check_coords(coords, velocity):
    if coords.x < 0+10 or coords.x > SIZE_X-10:
        velocity.x = -velocity.x
    if coords.y < 0+10 or coords.y > SIZE_Y-10:
        velocity.y = -velocity.y

# Обновление координаты
def update_coords(coords, velocity):
    return add(coords, velocity)  

# Расчет скорости с учетом равномерной силы тяжести (равноускоренное движение)
def update_velocity(coords, acceleration):
    return add(velocity, acceleration)

# Функция, которая очищает экран
def clear_window():
    rectangle = gr.Rectangle(gr.Point(0,0), gr.Point(SIZE_X,SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)

    # Рисуем Солнце
    sun = gr.Circle(gr.Point(600,300),50)
    sun.setFill('yellow')
    sun.draw(window)

# Рассчитываем и "рисуем"
while True:
    clear_window()
    draw_ball(coords)
    coords = update_coords(coords,velocity)
    check_coords(coords,velocity)
    gr.time.sleep(0.02)
    
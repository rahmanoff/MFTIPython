import graphics as gr

SIZE_X = 1200
SIZE_Y = 600

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(16, 16)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

# Скорость вперед
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point

# Смена напраления движения при достижении границ экрана
def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point

# Прорисовка окна программы и Солнца
def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('black')
    rectangle.draw(window)
    
    # Рисуем Солнце
    sun = gr.Circle(gr.Point(600, 300), 50)
    sun.setFill('yellow')
    sun.draw(window)

# Прорисовка Планеты
def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('blue')
    circle.draw(window)

# Проверка выхода Планеты за пределы экрана
def check_coords(coords, velocity):
    if coords.x < 0+15 or coords.x > SIZE_X-15:
        velocity.x = -velocity.x

    if coords.y < 0+15 or coords.y > SIZE_Y-15:
        velocity.y = -velocity.y

# Расчет координат Планеты в зависимости от скорости
def update_coords(coords, velocity):
    return add(coords, velocity)

# Расчет сокрости в зависимости от ускорения
def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)

# Расчет гравитационнного типа движения в зависимости от близости к Солнцу
def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    # Эмпирическая гравитационная постоянная
    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)


while True:
    clear_window()
    draw_ball(coords)

    acceleration = update_acceleration(coords, gr.Point(600, 300))

    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)

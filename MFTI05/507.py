import graphics as gr

# Размеры окна программы
SIZE_X = 1200
SIZE_Y = 600

# Вывод на экран окна программы
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(15, 15)
velocity = gr.Point(2, 1)
acceleration = gr.Point(0, 0)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def check_coords(coords, velocity):
    if coords.x < 10 or coords.x > SIZE_X-10:
        velocity.x = -velocity.x

    if coords.y < 10 or coords.y > SIZE_Y-10:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)


while True:
    clear_window()
    draw_ball(coords)

    acceleration = update_acceleration(coords, gr.Point(SIZE_X/2, SIZE_Y/2))

    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.02)
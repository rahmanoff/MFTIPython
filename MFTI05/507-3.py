import graphics as gr
SIZE_X = 1200
SIZE_Y = 600

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(1,1)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

# Проверка выхода Планеты за пределы экрана
def check_coords(coords, velocity):
    if coords.x < 0+15 or coords.x > SIZE_X-15:
        velocity.x = -velocity.x

    if coords.y < 0+15 or coords.y > SIZE_Y-15:
        velocity.y = -velocity.y

#Обьект Circle создается здесь лишь ОДИН раз
planet = gr.Circle(coords, 10)
planet.draw(window)
planet.setFill('red')

while True:
    # Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    planet.move(1,1)
    print(planet.getCenter())

    gr.time.sleep(0.02)
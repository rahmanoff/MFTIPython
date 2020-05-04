import graphics as gr
# Размеры окна программы
SIZE_X = 1200
SIZE_Y = 600
# Параметры окна программы
window = gr.GraphWin("Universe", SIZE_X, SIZE_Y)
# Параметры Планеты
# Центр координаты Планеты
coordX = 10
coordY = 10
center = gr.Point(coordX,coordY)
planet = gr.Circle(center, 10)
planet.setFill('red')
# Параметры Солнца
sun = gr.Circle(gr.Point(SIZE_X/2, SIZE_Y/2), 50)
sun.setFill('yellow')
# Рисуем Планету
planet.draw(window)
# Рисуем Солнце
sun.draw(window)
# Начальная скорость Планеты по X
velocityX = 3
# Начальная скорость Планеты по Y
velocityY = 1
# 
while True:
    # Расстояние от центра Планеты до центра Солнца
    diffX = abs(SIZE_X/2 - coordX)
    diffY = abs(SIZE_Y/2 - coordY)
    # Если расстояние от Планеты до Солнца меньше, чем 25 пикс, то скорость Планеты уменьшается на 0.01
    if diffX <= 75 and diffY <= 75:
        velocityX = velocityX*0.99
        velocityY = velocityY*0.99
    # Если Планета достигает границ по X, то меняем направление движения на противоположное
    if coordX < 10 or coordX > SIZE_X-10:
        velocityX = -velocityX
    # Если Планета достигает границ по Y, то меняем направление движения на противоположное
    if coordY < 10 or coordY > SIZE_Y-10:
        velocityY = -velocityY
    # Расстояние до Солнца
    if (SIZE_X/2-50 < coordX < SIZE_X/2+50) and (SIZE_Y/2-50 < coordY < SIZE_Y/2+50):
        velocityX = -velocityX
        velocityY = -velocityY
    # Движение Планеты
    planet.move(velocityX, velocityY)
    # Новые координаты Планеты
    coordX+=velocityX
    coordY+=velocityY
window.getMouse()
window.close()
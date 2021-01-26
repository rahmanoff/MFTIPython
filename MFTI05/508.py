import graphics as gr
# Размеры окна программы
SIZE_X = 1200
SIZE_Y = 600
# Параметры окна программы
window = gr.GraphWin("Universe", SIZE_X, SIZE_Y)
# Параметры Планеты
# Центр координаты Планеты
x1 = 10
y1 = 10
center = gr.Point(x1,y1)
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
velocityX = 1
# Начальная скорость Планеты по Y
velocityY = -2
# 
while True:
    # Если Планета достигает границ по X, то меняем направление движения на противоположное
    if x1 < 10 or x1 > SIZE_X-10:
        velocityX = -velocityX
    # Если Планета достигает границ по Y, то меняем направление движения на противоположное
    if y1 < 10 or y1 > SIZE_Y-10:
        velocityY = -velocityY
    # Движение Планеты
    planet.move(velocityX, velocityY)
    # Новые координаты Планеты
    x1+=velocityX
    y1+=velocityY
window.getMouse()
window.close()
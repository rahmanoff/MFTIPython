# Модель математического маятника - не доделано!

import graphics as gr
# Размеры окна программы
SIZE_X = 1200
SIZE_Y = 600
# Параметры окна программы
window = gr.GraphWin("Маятник", SIZE_X, SIZE_Y)
# Параметры Маятника
# Центр координаты Маятника
coordX = SIZE_X/2
coordY = SIZE_Y/1.5
# Параметры Солнца
pen = gr.Circle(gr.Point(coordX, coordY), 50)
pen.setFill('yellow')
# Точка подвеса Маятника
mountPoint = gr.Circle(gr.Point(SIZE_X/2, SIZE_Y/10), 10)
mountPoint.setFill('black')
# Рисуем Маятник
pen.draw(window)
# Рисуем точку подвеса
mountPoint.draw(window)
# Начальная скорость Маятника по X
velocityX = 10
# Начальная скорость Маятника по Y
velocityY = 0
# Нить подвеса

# Маятник
while True:
    # Если Маятник достигает границ по X, то меняем направление движения на противоположное
    if coordX < 250 or coordX > SIZE_X-250:
        velocityX = -velocityX
    # Если Маятник достигает границ по Y, то меняем направление движения на противоположное
    if coordY < 200 or coordY > SIZE_Y-200:
        velocityY = -velocityY
    # Движение Маятника
    pen.move(velocityX, velocityY)
    # Новые координаты Планеты
    coordX+=velocityX
    coordY+=velocityY
    cable = gr.Line(gr.Point(SIZE_X/2,SIZE_Y/10),gr.Point(coordX,coordY))
    cable.setFill('black')
    cable.draw(window)
window.getMouse()
window.close()
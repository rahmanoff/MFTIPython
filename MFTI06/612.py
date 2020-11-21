# Алгоритмы на Python 3. Лекция №4
# YouTube - 14 окт 2017

import graphics as gr

def build_house (window, upper_left_corner, width):
    """ Функция, которая рисует дом """
    height = calculate_height(width)



window = gr.GraphWin("Russian game", 300, 300)
build_house(window, gr.Point(100,100), 100)

print("Ура! Дом построен!")
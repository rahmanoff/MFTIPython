# Структурное программирование
# Make of graphic primitives
import graphics as gr

window = gr.GraphWin("Graphic Primitives", 800, 600)

def draw_sky():
    sky = gr.Rectangle(gr.Point(0,0), gr.Point(799,399))
    sky.setFill('blue')
    sky.draw(window)

def draw_earth():
    earth = gr.Rectangle(gr.Point(0,399), gr.Point(799,599))
    earth.setFill('grey')
    earth.draw(window)

def draw_sun():
    sun = gr.Circle(gr.Point(75,75),100)
    sun.setFill('yellow')
    sun.draw(window)

def draw_wall():
    wall = gr.Rectangle(gr.Point(150,300), gr.Point(350,500))
    wall.setFill('grey')
    wall.draw(window)

def draw_glass():
    glass = gr.Rectangle(gr.Point(175,350), gr.Point(250,425))
    glass.setFill('white')
    glass.draw(window)

def draw_hLine():
    hLine = gr.Line(gr.Point(175,380), gr.Point(250,380))
    hLine.draw(window)

def draw_vLine():
    vLine = gr.Line(gr.Point(215,380), gr.Point(215,425))
    vLine.draw(window)

def draw_door():
    door = gr.Rectangle(gr.Point(275,375), gr.Point(325,499))
    door.setFill('brown')
    door.draw(window)

def draw_roof():
    roof = gr.Polygon(gr.Point(135,300), gr.Point(250,200), gr.Point(365,300))
    roof.setFill('black')
    roof.draw(window)

def draw_handle():
    handle = gr.Circle(gr.Point(285,440),3)
    handle.draw(window)

def draw_tree():
    tree = gr.Polygon(gr.Point(450,500), gr.Point(500,400), gr.Point(460,400), gr.Point(510,300), gr.Point(470,300), gr.Point(600,200), gr.Point(730,300), gr.Point(690,300), gr.Point(740,400), gr.Point(700,400), gr.Point(750,500), gr.Point(750,500), gr.Point(750,500))
    tree.setFill('green')
    tree.draw(window)

def draw_world():
    draw_sky()
    draw_earth()
    draw_sun()
    draw_wall()
    draw_glass()
    draw_hLine()
    draw_vLine()
    draw_door()
    draw_roof()
    draw_handle()
    draw_tree()

draw_world()

window.getMouse()

window.close()
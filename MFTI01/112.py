# Практика: Черепаха
# Упражнение №12: пружина

import turtle

turtle.shape('turtle')

loop=0
R=50
r=10

turtle.penup()
turtle.left(180)
turtle.goto(-100,0)
turtle.right(90)
turtle.pendown()

while loop<5:
    turtle.circle(-R,180)
    loop+=1
    if loop<5:
        turtle.circle(-r,180)

turtle.mainloop()
# Практика: Черепаха
# Упражнение №10: «цветок»

import turtle

turtle.shape('turtle')

ang=45
r=100

while ang <180:
    turtle.circle(r)
    turtle.circle(-r)
    turtle.left(ang)
    ang+=45

turtle.mainloop()
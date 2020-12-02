# Практика: Черепаха
# Упражнение №11: «бабочка»

import turtle

turtle.shape('turtle')

loop=0
r=50
ang=90
turtle.left(90)
while loop<11:
    turtle.circle(r)
    turtle.circle(-r)
    r+=10
    loop+=1

turtle.mainloop()
# Практика: Черепаха
# Упражнение №7: спираль

import turtle
import math

turtle.shape('turtle')

i=1 #spiral step

while i<1750:
    p = i / (2 * math.pi) #polar type
    x = p * math.cos(p) #decart type x
    y = p * math.sin(p) #decart type y
    turtle.goto(x,y)
    i+=1

turtle.mainloop()
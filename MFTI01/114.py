import turtle
import math

turtle.shape('turtle')

n = int(input("введите кол-во углов: "))
l = int(input("введите длину стороны: "))

def star(n,l):
    ang=180/n
    for i in range(n):
        turtle.backward(l)
        turtle.right(180+ang)

star(n,l)

turtle.mainloop()

import turtle

turtle.shape('turtle')

x = 100
n = 0

while n < 12:
    turtle.forward(x)
    turtle.stamp()
    turtle.backward(x)
    turtle.right(390)
    n+=1

turtle.mainloop()
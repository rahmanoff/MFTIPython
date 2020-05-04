import turtle

turtle.shape ('turtle')

x = 20
count = 0

while count < 10:

    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)

    turtle.penup()

    turtle.forward(10)
    turtle.left(90)
    turtle.backward(10)

    turtle.pendown()
    
    x+=20
    count+=1

turtle.mainloop()
import turtle

turtle.shape('turtle')

x = 5
count = 0

while count < 35:
    turtle.forward(x)
    turtle.left(90)
    x += 5
    count += 1

turtle.mainloop()
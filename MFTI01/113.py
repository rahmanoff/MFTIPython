import turtle
turtle.shape('turtle')

R=100

# тело
turtle.left(90)
turtle.color("black","yellow")
turtle.begin_fill()
turtle.circle(R)
turtle.end_fill()

# левый глаз
turtle.penup()
turtle.goto(-R*1.5,R/2)
turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
turtle.circle(-R/(0.1*R))
turtle.end_fill()

# правый глаз
turtle.penup()
turtle.goto(-0.75*R,R/2)
turtle.pendown()
turtle.color("black","blue")
turtle.begin_fill()
turtle.circle(-R/(0.1*R))
turtle.end_fill()

# нос
turtle.color('black')
turtle.penup()
turtle.goto(-R,0.25*R)
turtle.pendown()
turtle.pensize(0.2*R)
turtle.right(180)
turtle.forward(R/2)

# рот
turtle.penup()
turtle.goto(-0.25*R,0)
turtle.pendown()
turtle.color('red')
turtle.pensize(.2*R)
turtle.circle(-.75*R,180)

turtle.mainloop()
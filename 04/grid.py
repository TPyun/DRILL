import turtle

turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()

i = 6
while (i > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.pendown()
    turtle.right(90)
    turtle.right(90)
    i -= 1
    
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
turtle.right(90)

i = 6
while (i > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.pendown()
    turtle.left(90)
    turtle.left(90)
    i -= 1

turtle.exitonclick()

import turtle
turtle.shape('turtle')
turtle.stamp()

def up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()


def left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()


def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    turtle.stamp()

turtle.listen()
turtle.onkey(up, 'W')
turtle.onkey(down, 'S')
turtle.onkey(left, 'A')
turtle.onkey(right, 'D')
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(restart, 'Escape')

turtle.exitonclick()



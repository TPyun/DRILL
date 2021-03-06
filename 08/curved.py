import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1920, 1080)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shapesize(2)
    turtle.setheading(90)
    turtle.penup()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(100)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_down_curves_points(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    for i in range(0, 50 + 1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * p1[0] + (-4*t**2 + 4*t) * p2[0] + (2*t**2 - t) * p3[0]
        y = (2*t**2 - 3*t + 1) * p1[1] + (-4*t**2 + 4*t) * p2[1] + (2*t**2 - t) * p3[1]
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2) * p2[0] + (-3*t**3 + 4*t**2 + t) * p3[0] + (t**3 - t**2) * p4[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2) * p2[1] + (-3*t**3 + 4*t**2 + t) * p3[1] + (t**3 - t**2) * p4[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2) * p3[0] + (-3*t**3 + 4*t**2 + t) * p4[0] + (t**3 - t**2) * p5[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2) * p3[1] + (-3*t**3 + 4*t**2 + t) * p4[1] + (t**3 - t**2) * p5[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2) * p4[0] + (-3*t**3 + 4*t**2 + t) * p5[0] + (t**3 - t**2) * p6[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2) * p4[1] + (-3*t**3 + 4*t**2 + t) * p5[1] + (t**3 - t**2) * p6[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2) * p5[0] + (-3*t**3 + 4*t**2 + t) * p6[0] + (t**3 - t**2) * p7[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2) * p5[1] + (-3*t**3 + 4*t**2 + t) * p6[1] + (t**3 - t**2) * p7[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p5[0] + (3*t**3 - 5*t**2 + 2) * p6[0] + (-3*t**3 + 4*t**2 + t) * p7[0] + (t**3 - t**2) * p8[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p5[1] + (3*t**3 - 5*t**2 + 2) * p6[1] + (-3*t**3 + 4*t**2 + t) * p7[1] + (t**3 - t**2) * p8[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p6[0] + (3*t**3 - 5*t**2 + 2) * p7[0] + (-3*t**3 + 4*t**2 + t) * p8[0] + (t**3 - t**2) * p9[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*p6[1] + (3*t**3 - 5*t**2 + 2) * p7[1] + (-3*t**3 + 4*t**2 + t) * p8[1] + (t**3 - t**2) * p9[1]) / 2
        draw_point((x, y))

    for i in range(50, 100 + 1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * p7[0] + (-4*t**2 + 4*t) * p8[0] + (2*t**2-t) * p9[0]
        y = (2*t**2 - 3*t + 1) * p7[1] + (-4*t**2 + 4*t) * p8[1] + (2*t**2-t) * p9[1]
        draw_point((x, y))


def draw_up_curves_points(l1, l2, l3, l4, l5, l6, l7, l8, l9):
    for i in range(0, 50 + 1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * l1[0] + (-4*t**2 + 4*t) * l2[0] + (2*t**2 - t) * l3[0]
        y = (2*t**2 - 3*t + 1) * l1[1] + (-4*t**2 + 4*t) * l2[1] + (2*t**2 - t) * l3[1]
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l1[0] + (3*t**3 - 5*t**2 + 2) * l2[0] + (-3*t**3 + 4*t**2 + t) * l3[0] + (t**3 - t**2) * l4[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l1[1] + (3*t**3 - 5*t**2 + 2) * l2[1] + (-3*t**3 + 4*t**2 + t) * l3[1] + (t**3 - t**2) * l4[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l2[0] + (3*t**3 - 5*t**2 + 2) * l3[0] + (-3*t**3 + 4*t**2 + t) * l4[0] + (t**3 - t**2) * l5[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l2[1] + (3*t**3 - 5*t**2 + 2) * l3[1] + (-3*t**3 + 4*t**2 + t) * l4[1] + (t**3 - t**2) * l5[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l3[0] + (3*t**3 - 5*t**2 + 2) * l4[0] + (-3*t**3 + 4*t**2 + t) * l5[0] + (t**3 - t**2) * l6[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l3[1] + (3*t**3 - 5*t**2 + 2) * l4[1] + (-3*t**3 + 4*t**2 + t) * l5[1] + (t**3 - t**2) * l6[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l4[0] + (3*t**3 - 5*t**2 + 2) * l5[0] + (-3*t**3 + 4*t**2 + t) * l6[0] + (t**3 - t**2) * l7[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l4[1] + (3*t**3 - 5*t**2 + 2) * l5[1] + (-3*t**3 + 4*t**2 + t) * l6[1] + (t**3 - t**2) * l7[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l5[0] + (3*t**3 - 5*t**2 + 2) * l6[0] + (-3*t**3 + 4*t**2 + t) * l7[0] + (t**3 - t**2) * l8[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l5[1] + (3*t**3 - 5*t**2 + 2) * l6[1] + (-3*t**3 + 4*t**2 + t) * l7[1] + (t**3 - t**2) * l8[1]) / 2
        draw_point((x, y))

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*l6[0] + (3*t**3 - 5*t**2 + 2) * l7[0] + (-3*t**3 + 4*t**2 + t) * l8[0] + (t**3 - t**2) * l9[0]) / 2
        y = ((-t**3 + 2*t**2 - t)*l6[1] + (3*t**3 - 5*t**2 + 2) * l7[1] + (-3*t**3 + 4*t**2 + t) * l8[1] + (t**3 - t**2) * l9[1]) / 2
        draw_point((x, y))

    for i in range(50, 100 + 1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * l7[0] + (-4*t**2 + 4*t) * l8[0] + (2*t**2-t) * l9[0]
        y = (2*t**2 - 3*t + 1) * l7[1] + (-4*t**2 + 4*t) * l8[1] + (2*t**2-t) * l9[1]
        draw_point((x, y))


prepare_turtle_canvas()

draw_down_curves_points((-400, -300), (-300, -50), (-200, -300), (-100, -50), (0, -300), (100, -50), (200, -300), (300, -50), (400, -300))
draw_up_curves_points((-400, 300), (-300, 50), (-200, 300), (-100, 50), (0, 300), (100, 50), (200, 300), (300, 50), (400, 300))

turtle.done()

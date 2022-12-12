import turtle
import random


def triangle_click(x, y):
    r = random.random()
    b = random.random()
    g = random.random()
    t.penup()
    t.goto(x, y)
    t.pencolor(r, g, b)
    t.pendown()

    for i in range(3):
        t.forward(60)
        t.left(120)
        t.forward(60)


t = turtle.Turtle()  # turtle name = t 
t.speed(4)
turtle.onscreenclick(triangle_click)

turtle.listen()
turtle.done()

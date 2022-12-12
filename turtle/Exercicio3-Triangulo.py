import turtle


def triangle_click(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.left(120)
        t.forward(100)


t = turtle.Turtle()         # turtle name = t
s = turtle.getscreen()      # screen
t.speed(4)
turtle.onclick(triangle_click, 1)
turtle.listen()
turtle.done()

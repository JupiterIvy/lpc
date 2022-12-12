import turtle


def fractal_tree(sz, lvl):
    if lvl > 0:
        t.forward(sz)
        t.right(30)
        fractal_tree(0.7 * sz, lvl - 1)
        t.left(60)
        fractal_tree(0.7 * sz, lvl - 1)
        t.right(30)
        t.backward(sz)
        t.color("orange")
    elif lvl == 0:
        t.color("yellow")


print("Insert the size: ")
size = int(input())
print("Insert the max level: ")
level = int(input())

t = turtle.Turtle()  # turtle name = t
t.screen.bgcolor("black")
t.color("orange")
t.speed(6)
t.left(90)

fractal_tree(size, level)

turtle.done()

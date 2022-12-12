import turtle


def fibonacci(nte, scale):
    square1, square2 = scale, scale
    rad1, rad2 = scale, scale
    count = 1
    i = 0

    # Creating the first square
    for i in range(4):
        t.right(90)
        t.forward(square2)

    # Series of squares
    while count < nte:
        t.backward(square1)
        t.left(90)
        for i in range(2):
            t.forward(square2)
            t.right(90)
        t.forward(square2)
        nth = square1 + square2
        square1 = square2
        square2 = nth
        count += 1

    t.penup()
    t.home()
    t.pendown()
    t.right(90)
    t.forward(rad1)
    t.right(270)

    # Implementing the Fibonacci spiral
    while i < nte + 1:
        t.circle(rad1, -90)
        aux = rad1 + rad2
        rad1 = rad2
        rad2 = aux
        i += 1


print("Enter the number of terms: ")
total = int(input())

if total > 0:
    print("Enter the plot scale(?:1): ")
    scl = int(input())
    t = turtle.Turtle()  # turtle name = t
    t.write((0, 0))
    t.speed(6)
    fibonacci(total, scl)

    turtle.done()
else:
    print("Term must be equal or greater than 1")

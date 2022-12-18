from turtle import Turtle


class Hud(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(-300, 400)
        self.pendown()
        self.width(20)

        for i in range(4):
        
            if i % 2 == 0:
                self.forward(600) 
                self.right(90)
            else:
                self.forward(1000) 
                self.right(90)

        self.penup()

        

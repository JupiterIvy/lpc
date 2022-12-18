from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('skyblue')
        self.right(90)
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(0, -350)
    

    def paddle_right(self):
        x = self.xcor()
        if x < 250:
            x += 30
        else:
            x = 250
        self.setx(x)


    def paddle_left(self):
        x = self.xcor()
        if x > -250:
            x += -30
        else:
            x = -250
        self.setx(x)

    
    
    


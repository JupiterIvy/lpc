from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.6)
        self.dx = 0.6
        self.dy = -1
    
        
        

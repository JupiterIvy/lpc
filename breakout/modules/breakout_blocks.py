from turtle import Turtle
import random

class Block(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.up()
        self.shapesize(0.7,3)
        self.goto(xpos, ypos)
        if ypos == 270:
            self.color('red')
        if ypos == 250:
            self.color('orange')
        if ypos == 230 or ypos == 210:
            self.color('green')
        if ypos == 170 or ypos == 190:
            self.color('yellow')
    
    def collisions(self, block, ball):
        block_x, block_y = block.xcor(), block.ycor()
        ball_x, ball_y = ball.xcor(), ball.ycor()
        if block.isvisible():
            if block_x - 30 < ball_x < block_x + 30:
                if ((ball_y - 10 <= block_y + 10 and ball_y > block_y) or
                        (ball_y + 10 >= block_y - 10 and ball_y < block_y)):
                    ball.dy *= -1
                    return True
            if block_y + 10 > ball_y > block_y - 10:
                if (block_x - 30 <= ball_x < block_x) or (block_x + 30 >= ball_x > block_x):
                    ball.dy *= -1
                    return True
        return False
            

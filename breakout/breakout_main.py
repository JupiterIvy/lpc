import turtle
from playsound import playsound
from turtle import Screen
from modules.breakout_paddle import *
from modules.breakout_ball import Ball
from modules.breakout_blocks import *
from modules.breakout_hud import *
from modules.breakout_score import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Breakout")
screen.tracer(0)

hud = Hud()
count, att = 0, 0
score = Score()
score.scoring(count)
attempt = Score()
attempt.attempts(att)

paddle = Paddle()
ball = Ball()

x_list = [-245, -175, -105, -35, 35, 105, 175, 245]
y_list = [270, 250, 230, 210, 190, 170]
blocks = []
hid_block = 0

screen.listen()
screen.onkeypress(paddle.paddle_right, "d")
screen.onkeypress(paddle.paddle_left, "a")

for i in x_list:
    for j in y_list:
        block = Block(i, j)
        blocks.append(block)

while True:
    screen.update()
    hud.goto(0, 260)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
        playsound('bop.wav', block=False)

    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
        playsound('bop.wav', block=False)

    if ball.ycor() > 400:
        ball.sety(400)
        ball.dy *= -1
        playsound('bop.wav', block=False)

    if -340 > ball.ycor() > -350 and paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50:
        ball.sety(-340)
        ball.dy *= -1
        playsound('pad.wav', block=False)

    if ball.ycor() < -360:
        ball.goto(0, 0)
        ball.dy = -1
        att += 1
        attempt.attempts(att)
    
    for i in blocks:
        if i.collisions(i, ball):
            i.hideturtle()
            hid_block += 1
            playsound('brick.wav', block=False)
            ball.dy *= 1.05
            if i.color() == ('yellow', 'yellow'):
                count += 1
                score.scoring(count)
            elif i.color() == ('green', 'green'):
                count += 2
                score.scoring(count)
            elif i.color() == ('red', 'red'):
                count += 3
                score.scoring(count)
    
    if hid_block == 48:
        screen.update()
        score.goto(0, 0)
        score.write("YOU WON!", align="center", font=("verdana", 50, "bold"))
        turtle.done()
    
    if att == 5:
        screen.update()
        score.goto(0, 0)
        score.write("GAME OVER", align="center", font=("verdana", 50, "bold"))
        turtle.done()

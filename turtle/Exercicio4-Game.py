import turtle
import random

letter = turtle.Turtle()
letter.hideturtle()

# Player One
playerOne = turtle.Turtle()
playerOne.color("green")
playerOne.shape("turtle")

# Player Two
playerTwo = turtle.Turtle()
playerTwo.color("blue")
playerTwo.shape("turtle")

# Defining finishing points
playerOne.penup()
playerTwo.penup()
playerOne.goto(300, 60)
playerOne.pendown()
playerOne.circle(40)
playerOne.penup()
playerOne.goto(-200, 100)
playerTwo.goto(300, -140)
playerTwo.pendown()
playerTwo.circle(40)
playerTwo.penup()
playerTwo.goto(-200, -100)

# Developing the game
for i in range(20):
    if playerOne.pos() >= (300, 100):
        letter.penup()
        letter.goto(-150,220)
        letter.pendown()
        letter.write("PLAYER ONE WINS", font=("Segoe UI", 32, "normal"))
        break
    elif playerTwo.pos() >= (300, -140):
        letter.penup()
        letter.goto(-150,220)
        letter.pendown()
        letter.write("PLAYER TWO WINS", font=("Segoe UI", 32, "normal"))
        break
    else:
        # PlayerOne turn
        print("Player One turn, press 'Enter' to roll the die ")
        playerOneInput = input()
        dieResult = random.randint(1, 6)
        print(f'Result is {dieResult}, move {dieResult*20} steps!')
        playerOne.forward(dieResult*20)
        # PlayerTwo turn
        print("Player Two turn, press 'Enter' to roll the die ")
        playerTwoInput = input()
        dieResult = random.randint(1, 6)
        print(f'Result is {dieResult}, move {dieResult*20} steps!')
        playerTwo.forward(dieResult*20)

turtle.done()

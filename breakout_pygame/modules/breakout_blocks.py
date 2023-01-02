import pygame

class Block():

    @staticmethod
    def __init__(xpos, ypos, screen):
        block = pygame.image.load("assets/teste.png")
        block = pygame.transform.scale(block, (75,15))
        screen.blit(block, (xpos, ypos))

    '''
    @staticmethod
    def collisions(block, ball):
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
    '''  

import pygame

RED = (255, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 14)

class Block(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([65, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

        if ypos == 130:
            self.image.fill(RED)
        if ypos == 170 or ypos == 190:
            self.image.fill(ORANGE)
        if ypos == 210 or ypos == 230:
            self.image.fill(GREEN)
        if ypos == 250 or ypos == 270:
            self.image.fill(YELLOW)

'''
class Block():

    @staticmethod
    def __init__(xpos, ypos, screen):
        block = pygame.image.load("assets/teste.png")
        block = pygame.transform.scale(block, (75,15))
        screen.blit(block, (xpos, ypos))

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

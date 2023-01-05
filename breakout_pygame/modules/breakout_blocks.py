import pygame

RED = (255, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 14)

class Block(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([65, 15])
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        if ypos == 130 or ypos == 150:
            self.image.fill(RED)
        if ypos == 170 or ypos == 190:
            self.image.fill(ORANGE)
        if ypos == 210 or ypos == 230:
            self.image.fill(GREEN)
        if ypos == 250 or ypos == 270:
            self.image.fill(YELLOW)

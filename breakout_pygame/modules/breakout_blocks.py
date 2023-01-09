import pygame

RED = (255, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 150, 50)
YELLOW = (255, 255, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([36, 14])
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
        if ypos == 150 or ypos == 170:
            self.image.fill(RED)
        if ypos == 190 or ypos == 210:
            self.image.fill(ORANGE)
        if ypos == 230 or ypos == 250:
            self.image.fill(GREEN)
        if ypos == 270 or ypos == 290:
            self.image.fill(YELLOW)

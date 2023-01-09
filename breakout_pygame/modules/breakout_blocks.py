import pygame

RED = (255, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 150, 50)
YELLOW = (255, 255, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([36, 14])
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
        if y_pos == 150 or y_pos == 170:
            self.image.fill(RED)
        if y_pos == 190 or y_pos == 210:
            self.image.fill(ORANGE)
        if y_pos == 230 or y_pos == 250:
            self.image.fill(GREEN)
        if y_pos == 270 or y_pos == 290:
            self.image.fill(YELLOW)

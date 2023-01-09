import pygame

COLOR_WHITE = (255, 255, 255)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([9, 8])
        self.image.fill(COLOR_WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 360
    
    

        

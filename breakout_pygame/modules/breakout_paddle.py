import pygame

Cyan = (10, 189, 200)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([75, 15])
        self.image.fill(Cyan)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 750
        self.move_right = False
        self.move_left = False
        self.accelerate = False

    def movements(self):
        # player 1 up movement
        if self.move_right:
            if self.accelerate:
                self.rect.x -= 8
            else:
                self.rect.x -= 5
        # player 1 down movement
        if self.move_left:
            if self.accelerate:
                self.rect.x += 8
            else:
                self.rect.x += 5
        # player 1 collides with left wall
        if self.rect.x <= 0:
            self.rect.x = 0
        # player 1 collides with right wall
        if self.rect.x > 525:
            self.rect.x = 525


        
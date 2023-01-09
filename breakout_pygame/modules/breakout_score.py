import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


class Score(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.font = pygame.font.Font('assets/JustMyType-KePl.ttf', 130)
        self.rect = pygame.draw.rect(screen, COLOR_BLACK, (0, 0, 0, 0))
        pygame.display.update()
    
    def scoring(self, point, screen, x_pos, y_pos):
        if point < 10:
            screen.blit(self.font.render('00' + str(point), True, COLOR_WHITE, COLOR_BLACK), (x_pos, y_pos))
        elif point >= 100:
            screen.blit(self.font.render('' + str(point), True, COLOR_WHITE, COLOR_BLACK), (x_pos, y_pos))
        elif point >= 10 or point < 100:
            screen.blit(self.font.render('0' + str(point), True, COLOR_WHITE, COLOR_BLACK), (x_pos, y_pos))
        
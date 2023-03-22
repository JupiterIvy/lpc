import pygame
from pygame.locals import *
from config import *

color = 0
class Screen:
    
    def __init__(self) -> None:
        flag = FULLSCREEN
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.font = pygame.font.Font("font/Megafont.ttf", 30)
        pass

    def draw(self, map, score):
        self.surface.fill(BLACK_COLOR)
        for rect in map:
            pygame.draw.rect(self.surface, MAP_COLOR, rect, 10)
        top_bar = pygame.Rect(0, 0, SCREEN_WIDTH, TOP_BAR_HEIGHT)
        pygame.draw.rect(self.surface, BLACK_COLOR, top_bar, 100)
        
        score_players = self.font.render(
            str(score), True, WHITE_COLOR)
        self.surface.blit(score_players, (660, 40))
    


    

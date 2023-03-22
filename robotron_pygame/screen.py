import pygame
from pygame.locals import *
from config import *
from map import MapLoader

color = 0
class Screen:
    
    def __init__(self) -> None:
        flag = DOUBLEBUF
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.font = pygame.font.Font("font/Megafont.ttf", 30)
        pass

    def ambiency(self):
        self.map_loader = MapLoader()
        self.map = []
        self.map = self.map_loader.load("map/map.txt")

    def draw(self, map, score):
        self.surface.fill(BLACK_COLOR)
        for rect in map:
            pygame.draw.rect(self.surface, MAP_COLOR, rect, 10)
        top_bar = pygame.Rect(0, 0, SCREEN_WIDTH, 90)
        pygame.draw.rect(self.surface, BLACK_COLOR, top_bar, 100)
        
        score_players = self.font.render(
            str(score), True, WHITE_COLOR)
        self.surface.blit(score_players, (660, 40))
    


    

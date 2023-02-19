import pygame
from config import *

color = 0
class Screen:
    surface: pygame.Surface
    
    def __init__(self) -> None:
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
        self.font = pygame.font.Font("font/Megafont.ttf", 54)

    def draw(self, map, score):
        self.surface.fill(BG_COLOR)
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                grid_shader = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.surface, GRID_SHADER, grid_shader, 4)
                grid_back = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.surface, GRID_COLOR, grid_back, 2)
                grid_light = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.surface, GRID_LIGHT, grid_light, 1)
        for border in map:
            pygame.draw.rect(self.surface, RECTS_COLOR, border)
        top_bar = pygame.Rect(0, 0, SCREEN_WIDTH, 70)
        pygame.draw.rect(self.surface, BLACK_COLOR, top_bar, 100)
import pygame
import random
from config import GOAL, TOP_BAR_HEIGHT


class Battery:
    size = 45
    collided_player = False
    pygame.mixer.init()

    def __init__(self, rect):
        self.battery_sprite = pygame.image.load("img/battery2.png")
        self.battery_sprite = pygame.transform.scale(self.battery_sprite, (53, 43))
        self.random_pos(rect)
    
    def random_pos(self, rects):
        while True:
            x = random.randint(100, 760 - TOP_BAR_HEIGHT)
            y = random.randint(100, 800 - TOP_BAR_HEIGHT)

            rect = pygame.Rect(x, y, self.size, self.size)
            print(rect)
            if rect.collidelist(rects) < 0:
                self.x = x
                self.y = y
                break

    def is_colliding_player(self, player_rect):
        self.collided_player = pygame.Rect(
            self.x, self.y, self.size, self.size).colliderect(player_rect)
        return self.collided_player


    def get_coord(self):
        return (self.x, self.y)

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.battery_sprite, self.get_coord())
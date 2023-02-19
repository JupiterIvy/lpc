from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from bullet import Bullet
from config import *
from screen import Screen
from tank import Tank
import json, os


class Game:
    def __init__(self) -> None:
        self.playing = True
        self.screen = Screen()
        self.score = (0, 0)
        with open(os.path.join("ps4.json"), 'r+') as file:
            button_keys = json.load(file)
        
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        
        self.tank1 = Tank((45, 243), TANK_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN,
                          pygame.K_SPACE)
        self.tank2 = Tank((710, 243), TANK_2_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'],  button_keys['x'])
        self.tank3 = Tank((710, 250), PLAYER_3_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'],  button_keys['x'])
        self.tank4 = Tank((750, 243), HUNTER_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'],  button_keys['x'])
        
    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.tank1.move(
            self.map, self.tank2.get_rect())
        self.tank2.move(
            self.map, self.tank1.get_rect())

    def loop(self):
        while self.playing:
            self.listen_keyboard()
            self.listen_events()

            self.screen.draw(self.map, self.score)
            self.tank1.draw(self.screen.surface)
            self.tank2.draw(self.screen.surface)
            self.tank3.draw(self.screen.surface)
            self.tank4.draw(self.screen.surface)

            pygame.display.flip()
            self.clock.tick(60)

# The cake is a lie

from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from bullet import Bullet
from config import *
from screen import Screen
from tank import Tank
from grunt import Grunt
from family import Family
from hulk import Hulk
from brain import Brain
import json, os


class Game:
    def __init__(self) -> None:
        self.playing = True
        self.screen = Screen()
        self.score = (0)
        with open(os.path.join("ps4.json"), 'r+') as file:
            button_keys = json.load(file)
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS

        self.enemies = []
        self.family = []
        for i in range(2):
            m = Family(self.map, 0)
            f = Family(self.map, 1)
            c = Family(self.map, 2)
            self.family.append(m)
            self.family.append(f)
            self.family.append(c)
        for i in range(3):
            h = Hulk(self.map)
            b = Brain(self.map)
            self.enemies.append(h)
            self.enemies.append(b)
        for i in range(15):
            grunts = Grunt(self.map)
            self.enemies.append(grunts)
        
        self.tank1 = Tank((620, 355), PLAYER_1_COLOR, button_keys['left_arrow'],
                        button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'])
            
    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        for e in self.enemies:
            self.tank1.move(self.map, e.get_rect())
            if type(e) is Hulk:
                e.move()
            elif type(e) is Grunt:
                e.move_toward_player(self.tank1.get_coord())
            elif type(e) is Brain:
                for f in self.family:
                    e.move(self.family, self.tank1.get_coord())

        for f in self.family:
            f.move()
        if self.tank1.has_shooted_enemy():
            self.score = (self.score + 1)

    def loop(self):
        while self.playing:
            self.listen_keyboard()
            self.listen_events()
            
            self.screen.draw(self.map, self.score)
            self.tank1.draw(self.screen.surface)
            for e in self.enemies:
                e.draw(self.screen.surface)
            for f in self.family:
                f.draw(self.screen.surface)

            pygame.display.flip()
            self.clock.tick(60)

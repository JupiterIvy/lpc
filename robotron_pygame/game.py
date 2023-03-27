# The cake is a lie

from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
import math
from bullet import Bullet
from config import *
from screen import Screen
from player import Player
from grunt import Grunt
from family import Family
from hulk import Hulk
from brain import Brain
from enforcer import Enforcer
import json, os


class Game:
    def __init__(self) -> None:
        self.playing = True
        self.screen = Screen()
        self.score = 0
        with open(os.path.join("ps4.json"), 'r+') as file:
            button_keys = json.load(file)
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        self.family_count = 0
        self.enemies = []
        self.family = []
        for i in range(2):
            m = Family(self.map, 0)
            f = Family(self.map, 1)
            c = Family(self.map, 2)
            self.family.append(m)
            self.family.append(f)
            self.family.append(c)
        for i in range(2):
            h = Hulk(self.map)
            b = Brain(self.map)
            e = Enforcer(self.map)
            self.enemies.append(h)
            self.enemies.append(e)
            self.enemies.append(b)
        for i in range(15):
            grunts = Grunt(self.map)
            self.enemies.append(grunts)
        
        self.player = Player((620, 355), PLAYER_1_COLOR, button_keys['left_arrow'],
                        button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'])
            
    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.player.move(self.map)
        for e in self.enemies:
            if self.player.has_shooted_enemy(e.get_rect()) and type(e) is not Hulk:
                index = self.enemies.index(e)
                self.enemies.pop(index)
                if type(e) is Grunt:
                    self.score = (self.score + 100)
                if type(e) is Brain:
                    self.score = (self.score + 500)
                if type(e) is Enforcer:
                    self.score = (self.score + 150)
            if type(e) is Hulk:
                e.move()
                for f in self.family:
                    if e.is_colliding_player(f.get_rect()):
                        index = self.family.index(f)
                        self.family.pop(index)
            elif type(e) is Grunt or type(e) is Enforcer:
                e.move_toward_player(self.player.get_coord())
            elif type(e) is Brain:
                if self.family:
                    target = self.family[0]
                    closest = math.dist((e.x, e.y), (target.x, target.y))
                    for f in self.family:
                        if math.dist((e.x, e.y), (f.x, f.y)) <= closest:
                            closest = math.dist((e.x, e.y), (f.x, f.y))
                            target = f.get_coord()
                        if e.is_colliding_player(f.get_rect()):
                            f.update_animation()
                    e.move(target)
                else:
                    e.move(self.player.get_coord())
            if e.is_colliding_player(self.player.get_rect()):
                print("jogador")

        for f in self.family:
            if f.is_colliding_player(self.player.get_rect()):
                index = self.family.index(f)
                self.family.pop(index)
                self.family_count += 1000
                self.score = (self.score + self.family_count)
                if self.family_count > 5000:
                    self.family_count = 5000
            f.move()
        
    def loop(self):
        while self.playing:
            self.listen_keyboard()
            self.listen_events()
            
            self.screen.draw(self.map, self.score)
            self.player.draw(self.screen.surface)
            for e in self.enemies:
                e.draw(self.screen.surface)
            for f in self.family:
                f.draw(self.screen.surface)

            pygame.display.flip()
            self.clock.tick(60)

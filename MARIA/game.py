from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from battery import Battery
from config import *
from screen import Screen
from player import Player
from map import MapLoader
import json, os


class Game:
    hunter = 'hunter'
    player = 'player'
    def __init__(self) -> None:
        self.playing = True
        self.screen = Screen()
        self.score = 0
        with open(os.path.join("ps4.json"), 'r+') as file:
            button_keys = json.load(file)

        self.clock = pygame.time.Clock()
        self.map_loader = MapLoader()
        self.map = []
        self.map = self.map_loader.load("map.txt")
        self.goal = []
        for i in range(5):
            battery = Battery(self.map)
            self.goal.append(battery)
        self.door = pygame.Rect(340, 110, 120, 20)
        self.map.append(self.door)

        self.hunter = Player((45, 243), PLAYER_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, self.hunter)
        self.player2 = Player((375, 220), PLAYER_2_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'], self.player)
        self.player3 = Player((417, 220), PLAYER_3_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s, self.player)
        self.player4 = Player((390, 243), HUNTER_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'], self.player)
        
    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def listen_keyboard(self):
        self.hunter.move(
            self.map, self.player2.get_rect(), None)
        self.player2.move(
            self.map, self.hunter.get_rect(), 0)
        self.player3.move(
            self.map, self.hunter.get_rect(), 1)

        if (self.hunter.is_colliding_player(self.player2.get_rect())):
                self.player2.animate_death()

        for i in range(len(self.goal)):
            if (self.goal[i-1].is_colliding_player(self.player2.get_rect())):
                self.goal.pop(i-1)
                self.score += 1
                
    def loop(self):
        while self.playing:
            self.listen_keyboard()
            self.listen_events()

            if self.score == 5:
                self.map.pop(290)
            self.screen.draw(self.map, self.score)
            for i in range(len(self.goal)):
                self.goal[i].draw(self.screen.surface)
            self.hunter.draw(self.screen.surface)
            self.player2.draw(self.screen.surface)
            self.player3.draw(self.screen.surface)

            pygame.display.flip()
            self.clock.tick(60)

from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from Entities.battery import Battery
from config import *
from screen import Screen
from Entities.player import Player
import json, os


class Game:
    hunter = 'player'
    player = 'Invader'
    death_count = 0
    def __init__(self) -> None:
        self.playing = True
        self.screen = Screen()
        self.score = 0
        with open(os.path.join("ps4.json"), 'r+') as file:
            button_keys = json.load(file)
        self.players = {}
        self.exit = []
        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        self.goal = []
        for i in range(7):
            battery = Battery(self.map)
            self.goal.append(battery)
        self.wall = pygame.Rect(340, 110, 120, 20)
        self.map.append(self.wall)

        self.player = Player((620, 355), PLAYER_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, self.hunter)
        self.player2 = Player((375, 220), PLAYER_2_COLOR, button_keys['left_arrow'],
                          button_keys['up_arrow'], button_keys['right_arrow'],button_keys['down_arrow'], self.player)
        self.player3 = Player((417, 220), PLAYER_3_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s, self.player)
        self.players.update({1: self.player2})
        self.players.update({2: self.player3})

    
    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.player.move(
            self.map, self.player2.get_rect(), None)
        self.player2.move(
            self.map, self.player.get_rect(), 0)
        self.player3.move(
            self.map, self.player.get_rect(), 1)

        for player in self.players:
            if (self.player.is_colliding_player(self.players[player].get_rect())):
                self.players[player].dead = True
                self.players[player].x = 900
                self.death_count += 1
                self.player.speed += 0.5
                print(self.death_count)
                
        for i in range(len(self.goal)):
            if (self.goal[i-1].is_colliding_player(self.player2.get_rect())):
                self.goal.pop(i-1)
                self.score += 1
        for i in range(len(self.goal)):
            if (self.goal[i-1].is_colliding_player(self.player3.get_rect())):
                self.goal.pop(i-1)
                self.score += 1
        if self.score == 7:
            self.score = 0
            self.map.pop(290)
    
    def victory(self):
        total_seconds = 0
        minutes = 0
        index = None
        if minutes < 2:
            if self.death_count >= len(self.players):
                self.screen.victory(self.hunter, None)
                for player in self.players:
                    self.players[player].speed = 0
                self.player.speed = 0
            if len(self.exit) >= 1 and self.death_count == 1:
                index = self.exit[0]
                self.screen.victory(self.player, index)
                for player in self.players:
                    self.players[player].speed = 0
                self.player.speed = 0
            if len(self.exit) == len(self.players):
                self.screen.victory(self.player, None)
                for player in self.players:
                    self.players[player].speed = 0
                self.player.speed = 0
            
        elif minutes >= 2:
            self.screen.victory(self.hunter, None)
            for player in self.players:
                self.players[player].speed = 0
            self.player.speed = 0
              
    def loop(self):
        while self.playing:
            self.listen_keyboard()
            self.listen_events()
            self.screen.draw(self.map, self.score)
            for i in range(len(self.goal)):
                self.goal[i].draw(self.screen.surface)
            self.player.draw(self.screen.surface)
            for player in self.players:
                self.players[player].draw(self.screen.surface)
            self.victory()
            pygame.display.flip()
            self.clock.tick(60)
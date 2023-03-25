import random
import pygame
import json, os
from config import SPEED, TOP_BAR_HEIGHT, GRID_LIGHT
from Entities.bullet import Bullet


class Player:
    collided_player = False
    size = 30
    elapsed = 0
    
    def __init__(self, initial_coord, color, key_left, key_up, key_right,
                 key_down, route):
        self.speed = SPEED
        self.player_sprite = pygame.image.load(
        "img/player.png").convert_alpha()
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
        for joystick in self.joysticks:
            joystick.init()
        self.player_angle = 3
        self.x = initial_coord[0]
        self.y = initial_coord[1]
        self.side = 0
        self.direction = 1
        self.x_velocity = 0
        self.y_velocity = 0
        self.running = False
        self.angle = 0
        with open(os.path.join("ps4.json"), 'r+') as file:
            self.button_keys = json.load(file)
        self.LEFT, self.RIGHT, self.UP, self.DOWN = False, False, False, False
        self.analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up

        self.shoot_down = False
        self.bullet = None
        self.dead = False

    def listen_joystick(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                self.running = True
                if event.button == self.key_left:
                    self.LEFT = True
                if event.button == self.key_right:
                    self.RIGHT = True
                if event.button == self.key_down:
                    self.DOWN = True
                if event.button == self.key_up:
                    self.UP = True
                if self.joysticks[0].get_button(0):
                    self.shoot_down = True
            if event.type == pygame.JOYBUTTONUP:
                self.running = False
                if event.button == self.key_left:
                    self.LEFT = False
                if event.button == self.key_right:
                    self.RIGHT = False
                if event.button == self.key_down:
                    self.DOWN = False
                if event.button == self.key_up:
                    self.UP = False
            if event.type == pygame.JOYAXISMOTION:
                self.analog_keys[event.axis] = event.value
                # Horizontal Analog
            
            if abs(self.analog_keys[0]) > .4:
                if self.analog_keys[0] < -.6:
                    self.LEFT = True
                    self.running = True
                else:
                    self.LEFT = False
                    self.running = False
                if self.analog_keys[0] > .6:
                    self.RIGHT = True
                    self.running = True
                else:
                    self.RIGHT = False  
                # Vertical Analog
            if abs(self.analog_keys[1]) > .4:
                if self.analog_keys[1] < -.6:
                    self.UP = True
                    self.running = True
                else:
                    self.UP = False
                    self.running = False
                if self.analog_keys[1] > .6:
                    self.DOWN = True
                    self.running = True
                else:
                    self.DOWN = False
        if self.LEFT:
            self.angle = 'LEFT'
            self.direction = -1
        if self.RIGHT:
            self.angle = 'RIGHT'
            self.direction = -1
        if self.UP:
            self.angle = 'UP'
            self.direction = -1
        if self.DOWN:
            self.angle = 'DOWN'
            self.direction = -1
        if self.shoot_down:
            self.bullet = Bullet(self.x + self.size / 2,
                                     self.y + self.size /
                                     2, -self.x_velocity / SPEED,
                                     -self.y_velocity / SPEED)
        self.animate_run(self.angle)

    def listen_keyboard(self):
        key = pygame.key.get_pressed()
        if not self.dead:
            if key[self.key_left]:
                self.angle = 'LEFT'
                self.direction = -1
                self.running = True
            elif key[self.key_right]:
                self.angle = 'RIGHT'
                self.direction = -1
                self.running = True
            elif key[self.key_down]:
                self.angle = 'DOWN'
                self.direction = -1
                self.running = True
            elif key[self.key_up]:
                self.angle = 'UP'
                self.running = True
                self.direction = -1
            else: 
                self.running = False
            self.animate_run(self.angle)
    
    def colliding_rects(self, rects):
        rect = pygame.Rect(self.x + (self.x_velocity * self.direction),
                           self.y + (self.y_velocity * self.direction),
                           self.size, self.size)

        if rect.collidelist(rects) < 0:
            self.x += self.x_velocity * self.direction
            self.y += self.y_velocity * self.direction
        
    def animate_run(self, direction):
        if self.running:
            self.elapsed += 1
            if self.elapsed == 2:
                self.player_angle += 1
            elif self.elapsed > 2:
                self.elapsed = 0
            if direction == 'DOWN':
                if self.player_angle > 5:
                    self.player_angle = 3
            elif direction == 'LEFT' or direction == 'RIGHT':
                if self.player_angle > 2:
                    self.player_angle = 0
            elif direction == 'UP':
                if self.player_angle > 8:
                    self.player_angle = 6

    def bullet_move(self, map, enemy_rect):
        if self.bullet is not None:
            self.bullet.move(map, enemy_rect)
            if self.bullet.end_life:
                self.bullet = None

    def move(self, map, enemy_rect, joy_number):
        self.direction = 0
        if not self.dead:
            for i in self.joysticks:
                if i.get_instance_id() == joy_number:
                    self.listen_joystick()
                else:
                    self.listen_keyboard()
        
        if self.angle == 'LEFT':
            self.y_velocity = 0
            self.x_velocity = self.speed
            self.side = 1
        elif self.angle == 'RIGHT':
            self.y_velocity = 0
            self.x_velocity = -self.speed
            self.side = 0
        elif self.angle == 'UP':
            self.y_velocity = self.speed
            self.x_velocity = 0
            self.side = 0
        elif self.angle == 'DOWN':
            self.y_velocity = -self.speed
            self.x_velocity = 0
            self.side = 0
        else:
            self.y_velocity = self.speed
            self.x_velocity = self.speed
            self.side = 0
        
        self.colliding_rects(map + [enemy_rect])
        self.is_colliding_player(enemy_rect)
        self.bullet_move(map, enemy_rect)

    def get_image(self) -> pygame.Surface:
        sub = self.player_sprite.subsurface(
            (self.player_angle * self.size , 0, self.size, self.size))

        vertical = 0
        horizontal = self.side > 0
        return pygame.transform.flip(sub, horizontal, vertical)

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)
    
    def get_coord(self):
        return (self.x, self.y)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.get_image(), self.get_coord())
        if self.bullet is not None:
            surface.blit(self.bullet.get_image(), self.bullet.get_coord())
            

    def is_colliding_player(self, player_rect):
        self.collided_player = pygame.Rect(self.x + (self.x_velocity * self.direction),
                           self.y + (self.y_velocity * self.direction),
                           self.size, self.size).colliderect(player_rect)
        return self.collided_player
    
    def has_touched_enemy(self):
        if self.collided_player:
            return True
        return False

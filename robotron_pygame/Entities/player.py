import random
import pygame
import json, os
from config import SPEED, TOP_BAR_HEIGHT


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
                if self.analog_keys[0] < -.7:
                    self.LEFT = True
                    self.running = True
                else:
                    self.LEFT = False
                    self.running = False
                if self.analog_keys[0] > .7:
                    self.RIGHT = True
                    self.running = True
                else:
                    self.RIGHT = False  
                # Vertical Analog
            if abs(self.analog_keys[1]) > .4:
                if self.analog_keys[1] < -.7:
                    self.UP = True
                    self.running = True
                else:
                    self.UP = False
                    self.running = False
                if self.analog_keys[1] > .7:
                    self.DOWN = True
                    self.running = True
                else:
                    self.DOWN = False
        if self.LEFT:
            self.x -= self.speed
            self.angle = 'LEFT'
            self.direction = -1
        if self.RIGHT:   
            self.x += self.speed 
            self.angle = 'RIGHT'
            self.direction = -1
        if self.UP:
            self.y -= self.speed
            self.angle = 'UP'
            self.direction = -1
        if self.DOWN:
            self.y += self.speed
            self.angle = 'DOWN'
            self.direction = -1
        self.animate_run(self.angle)
        print(self.running)

    def listen_keyboard(self):
        key = pygame.key.get_pressed()
        if not self.dead:
            if key[self.key_left]:
                self.x -= self.speed
                self.angle = 'LEFT'
                self.direction = -1
            elif key[self.key_right]:
                self.x += self.speed 
                self.angle = 'RIGHT'
                self.direction = -1
            elif key[self.key_down]:
                self.y += self.speed
                self.angle = 'DOWN'
                self.direction = -1
            elif key[self.key_up]:
                self.y -= self.speed
                self.angle = 'UP'
                self.direction = -1
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
            
    def move(self, map, enemy_rect, joy_number):
        self.direction = 0
        if not self.dead:
            for i in self.joysticks:
                if i.get_instance_id() == joy_number:
                    self.listen_joystick()
                else:
                    self.listen_keyboard()
    
        if self.angle == 'LEFT':
            self.x_velocity = 1
        else:
            self.x_velocity = 0
        self.colliding_rects(map + [enemy_rect])
        self.is_colliding_player(enemy_rect)

    def get_image(self) -> pygame.Surface:
        sub = self.player_sprite.subsurface(
            (self.player_angle * self.size , 0, self.size, self.size))

        vertical = 0
        horizontal = self.x_velocity > 0
        return pygame.transform.flip(sub, horizontal, vertical)

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)
    
    def get_coord(self):
        return (self.x, self.y)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.get_image(), self.get_coord())

    def is_colliding_player(self, player_rect):
        self.collided_player = pygame.Rect(self.x + (self.x_velocity * self.direction),
                           self.y + (self.y_velocity * self.direction),
                           self.size, self.size).colliderect(player_rect)
        return self.collided_player
    
    def has_touched_enemy(self):
        if self.collided_player:
            return True
        return False


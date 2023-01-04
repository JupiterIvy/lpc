import pygame
from modules.breakout_blocks import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2022-12-12")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (300, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()

# sound effects
bop_sfx = pygame.mixer.Sound('bop.wav')
pad_sfx = pygame.mixer.Sound('pad.wav')
brick_sfx = pygame.mixer.Sound('brick.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1 = pygame.transform.scale(player_1, (75,15))
player_1_rect = pygame.Rect((300, 750),(249,56))
player_1_move_right = False
player_1_move_left = False

# ball
ball = pygame.image.load("assets/ball.png")
ball = pygame.transform.scale(ball, (12,12))
ball_rect = pygame.Rect((300, 360),(15,15))
ball_dx = 2
ball_dy = 2

# score
score_1 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

x_list = [10, 80, 150, 220, 290, 360, 430, 500]
y_list = [130, 150, 170, 190, 210, 230, 250, 270]
blocks = []
hid_block = 0

for i in x_list:
        for j in y_list:
                block = Block(i,j)
                blocks.append(block)

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1_move_right = True
            if event.key == pygame.K_RIGHT:
                player_1_move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1_move_right = False
            if event.key == pygame.K_RIGHT:
                player_1_move_left = False

    # checking the victory condition
    if score_1 < 5:

        # clear screen
        screen.fill(COLOR_BLACK)
        
        # ball collision with the wall
        if ball_rect.y <= 0:
            ball_dy *= -1
            bop_sfx.play()
            
            # ball collision with the wall
        if ball_rect.x > 590:
            ball_dx *= -1
            bop_sfx.play()
        elif ball_rect.x <= 0:
            ball_dx *= -1
            bop_sfx.play()

        # ball collision with the player 1 's paddle
        if 740 < ball_rect.y < 750:
            if player_1_rect.x < ball_rect.x + 15 < player_1_rect.x + 100:
                ball_dy *= -1
                pad_sfx.play()

        if ball_rect.y > 780:
            ball_rect.y = 360
            ball_rect.x = 300
            ball_dy *= 1

        # ball movement
        ball_rect.x = ball_rect.x + ball_dx
        ball_rect.y = ball_rect.y + ball_dy

        # player 1 up movement
        if player_1_move_right:
            player_1_rect.x -= 5
        else:
            player_1_rect.x += 0

        # player 1 down movement
        if player_1_move_left:
            player_1_rect.x += 5
        else:
            player_1_rect.x += 0

        # player 1 collides with upper wall
        if player_1_rect.x <= 0:
            player_1_rect.x = 0

        # player 1 collides with lower wall
        if player_1_rect.x > 525:
            player_1_rect.x = 525

        # drawing objects
        screen.blit(ball, ball_rect)
        screen.blit(player_1, player_1_rect)
        screen.blit(score_text, score_text_rect)
        for i in blocks:
            if (i.rect.colliderect(ball_rect) == False):
                screen.blit(i.image, i.rect)
            else:
                blocks.remove(i)
                hid_block += 1
                brick_sfx.play()
                ball_dy *= -1.05
            
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()

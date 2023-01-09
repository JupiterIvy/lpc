import pygame
from modules.breakout_blocks import *
from modules.breakout_ball import *
from modules.breakout_paddle import *
from modules.breakout_score import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition")

# score text
score_text = Score(screen)
att_text = Score(screen)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = victory_text.get_rect()
victory_text_rect.center = (300, 400)

# Game Over text
game_over_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
game_over_text = game_over_font .render('GAME OVER', True, COLOR_WHITE, COLOR_BLACK)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (300, 400)

# sound effects
bop_sfx = pygame.mixer.Sound('bop.wav')
pad_sfx = pygame.mixer.Sound('pad.wav')
brick_sfx = pygame.mixer.Sound('brick.wav')

# player 1
player_1 = Paddle()
player_1_accelerate = False

# ball
ball = Ball()
ball_dx = 2
ball_dy = 2

# score
count, att = 0, 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

x_list = [20, 60, 100, 140, 180, 220, 260, 300, 340, 380, 420, 460, 500, 540]
y_list = [150, 170, 190, 210, 230, 250, 270, 290]
blocks = []
hid_block = 0

for i in x_list:
    for j in y_list:
        block = Block(i, j)
        blocks.append(block)

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.move_right = True
            if event.key == pygame.K_RIGHT:
                player_1.move_left = True
            if event.key == pygame.K_SPACE:
                player_1.accelerate = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1.move_right = False
            if event.key == pygame.K_RIGHT:
                player_1.move_left = False
            if event.key == pygame.K_SPACE:
                player_1.accelerate = False
    
    # checking the victory condition
    if True:
        # clear screen
        screen.fill(COLOR_BLACK)

        # player_1 movements
        player_1.movements()

        # ball collision with the upper wall
        if ball.rect.y <= 5:
            ball_dy *= -1
            bop_sfx.play()
            
        # ball collision with side wall
        if ball.rect.x > 580:
            ball.rect.x = 580
            ball_dx *= -1
            bop_sfx.play()
        elif ball.rect.x <= 5:
            ball.rect.x = 5
            ball_dx *= -1
            bop_sfx.play()

        # ball collision with the player 1 's paddle
        if 740 <= ball.rect.y <= 750:

            # collision with the right side of the paddle with the ball coming from
            # the left side
            if player_1.rect.x + 65 <= ball.rect.x + 15 <= player_1.rect.x + 100 and ball_dx > 0:
                ball_dy = ball_dx
                ball_dy *= -1
                ball.rect.y = 740
                bop_sfx.play()

            # collision with the left side of the paddle with the ball coming from
            # the left side
            elif player_1.rect.x <= ball.rect.x + 15 <= player_1.rect.x + 34 and ball_dx > 0:
                ball_dy = ball_dx
                ball_dy *= -1
                ball_dx *= -1
                ball.rect.y = 740
                bop_sfx.play()

            # collision with the left side of the paddle with the ball coming from
            # the right side
            elif player_1.rect.x <= ball.rect.x + 15 <= player_1.rect.x + 34 and ball_dx < 0:
                ball_dy = ball_dx
                ball_dx *= -1
                ball_dy *= -1
                ball.rect.y = 740
                bop_sfx.play()

            # collision with the right side of the paddle with the ball coming from
            # the right side
            elif player_1.rect.x + 65 <= ball.rect.x + 15 <= player_1.rect.x + 100 and ball_dx < 0:
                ball_dy = ball_dx
                ball_dy *= -1
                ball_dx *= -1
                ball.rect.y = 740
                bop_sfx.play()

            # collision with the middle of the paddle with the ball coming from
            # the right side
            elif player_1.rect.x + 35 <= ball.rect.x + 15 <= player_1.rect.x + 65 and ball_dx < 0:
                ball_dy = -(1 + ball_dx)
                ball_dx *= -1
                ball.rect.y = 740 
                bop_sfx.play()

            # collision with the middle of the paddle with the ball coming from
            # the left side
            elif player_1.rect.x + 35 <= ball.rect.x + 15 <= player_1.rect.x + 65 and ball_dx > 0:
                ball_dy = -(1 + ball_dx)
                ball_dx *= -1
                ball.rect.y = 740
                bop_sfx.play()

        # lost ball
        if ball.rect.y > 780:
            ball.rect.y = 360
            ball.rect.x = 300
            ball_dy = 2
            ball_dx = 2
            att += 1
            player_1.rect.x = 280
            player_1.rect.y = 750

        # ball movement
        ball.rect.x = ball.rect.x + ball_dx
        ball.rect.y = ball.rect.y + ball_dy

        # drawing objects
        screen.blit(ball.image, ball.rect)
        screen.blit(player_1.image, player_1.rect)
        score_text.scoring(count, screen, 60, 35)
        att_text.scoring(att, screen, 380, 35)
        pygame.draw.rect(screen, COLOR_WHITE, pygame.Rect(0, 0, 600, 800), 12)

        # drawing blocks
        for i in blocks:
            if not i.rect.colliderect(ball.rect):
                screen.blit(i.image, i.rect)
            else:
                # checking score and collisions
                if i.rect.y == 150 or i.rect.y == 170:
                    count += 7
                    if (ball.rect.x < i.rect.x and ball.rect.y < i.rect.y+12) or \
                            (ball.rect.x > i.rect.x+32 and ball.rect.y < i.rect.y+12):
                        ball_dx *= -1
                    elif ball_dy < 0:
                        if ball_dy >= -7:
                            if ball_dx > 0:
                                ball_dy = 7
                                ball_dx = 7
                            else:
                                ball_dy = 7
                                ball_dx = -7
                        else:
                            ball_dy *= -1
                    elif ball_dy > 0:
                        if ball_dy <= 7:
                            if ball_dx > 0:

                                ball_dy = -7
                                ball_dx = 7
                            else:
                                ball_dy = -7
                                ball_dx = -7
                        else:
                            ball_dy *= -1

                if i.rect.y == 190 or i.rect.y == 210:
                    count += 5

                    if (ball.rect.x < i.rect.x and ball.rect.y < i.rect.y + 12) or \
                            (ball.rect.x > i.rect.x + 32 and ball.rect.y < i.rect.y + 12):
                        ball_dx *= -1

                    elif ball_dy < 0:
                        if ball_dy >= -5:
                            if ball_dx > 0:
                                ball_dy = 5
                                ball_dx = 5
                            else:
                                ball_dy = 5
                                ball_dx = -5
                        else:
                            ball_dy *= -1
                    elif ball_dy > 0:
                        if ball_dy <= 5:
                            if ball_dx > 0:
                                ball_dy = -5
                                ball_dx = 5
                            else:
                                ball_dy = -5
                                ball_dx = -5
                        else:
                            ball_dy *= -1

                if i.rect.y == 230 or i.rect.y == 250:
                    count += 3

                    if (ball.rect.x < i.rect.x and ball.rect.y < i.rect.y + 12) or \
                            (ball.rect.x > i.rect.x + 32 and ball.rect.y < i.rect.y + 12):
                        ball_dx *= -1
                    elif ball_dy < 0:
                        if ball_dy >= -3:
                            if ball_dx > 0:
                                ball_dy = 3
                                ball_dx = 3
                            else:
                                ball_dy = 3
                                ball_dx = -3
                        else:
                            ball_dy *= -1
                    elif ball_dy > 0:
                        if ball_dy <= 3:
                            if ball_dx > 0:
                                ball_dy = -3
                                ball_dx = 3
                            else:
                                ball_dy = -3
                                ball_dx = -3
                        else:
                            ball_dy *= -1

                if i.rect.y == 270 or i.rect.y == 290:
                    if (ball.rect.x < i.rect.x and ball.rect.y < i.rect.y + 13) or \
                            (ball.rect.x > i.rect.x + 33 and ball.rect.y < i.rect.y + 13):
                        ball_dx *= -1

                    else:
                        ball_dy *= -1
                    count += 1

                blocks.remove(i)
                hid_block += 1
                brick_sfx.play()

    if hid_block == 112:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(victory_text, victory_text_rect)
        ball_dx = 0
        ball_dy = 0
    if att == 5:
        # drawing game overs
        screen.fill(COLOR_BLACK)
        screen.blit(game_over_text, game_over_text_rect)
        ball_dx = 0
        ball_dy = 0

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()

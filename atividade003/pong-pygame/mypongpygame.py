# Jucimar Jr
# João Pedro Telles Paes 2415310011
# 2024

import pygame
import random
import os

pygame.init()

COLOR_BLACK = (random.randrange(0, 50), random.randrange(0, 50), random.randrange(0, 25))
COLOR_WHITE = (random.randrange(150, 255), random.randrange(150, 255), random.randrange(150, 255))

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-02")

# correct directory addressing
folder_path = os.path.dirname(__file__)
os.chdir(folder_path)

# score text
score_font = pygame.font.Font(r'assets\PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# debug text remove later
debug_font = pygame.font.Font(r'assets\PressStart2P.ttf', 10)
debug_text = debug_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
debug_text_rect = debug_text.get_rect()
debug_text_rect.center = (50, 120)
debug_text_2 = debug_font.render('DEBUG REMOVER DEPOIS', True, COLOR_WHITE, COLOR_BLACK)
debug_text_2_rect = debug_text_2.get_rect()
debug_text_2_rect.center = (50, 150)

# victory text
victory_font = pygame.font.Font(r'assets\PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound(r'assets\bounce.wav')
scoring_sound_effect = pygame.mixer.Sound(r'assets\258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load(r"assets\player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False
player_1_center = 0
player_1_top = 0
player_1_bottom = 0

# player 2 - robot
player_2 = pygame.image.load(r"assets\player2.png")
player_2_y = 300
player_2_move_up = False
player_2_move_down = False
player_2_center = 0
player_2_top = 0
player_2_bottom = 0

# ball
ball = pygame.image.load(r"assets\ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = -5
ball_relative_y_p1 = 0
ball_relative_y_p2 = 0

# score
score_1 = 0
score_2 = 0

# hidden score
hidden_score = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # player 2 "Artificial Intelligence"
    if ball_y < player_2_center - 20:
        player_2_move_up = True
        player_2_move_down = False
    elif ball_y > player_2_center + 20:
        player_2_move_down = True
        player_2_move_up = False
    else:
        player_2_move_down = False
        player_2_move_up = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            ball_y += ball_dy
            bounce_sound_effect.play()
            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        elif ball_y <= 0:
            ball_dy *= -1
            ball_y += ball_dy
            bounce_sound_effect.play()
            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        # define coordinates of important positions of each paddle
        player_1_center = player_1_y + 62
        player_2_center = player_2_y + 62

        player_1_top = player_1_center + 75
        player_2_top = player_1_center + 75
        player_1_bottom = player_1_center + 76
        player_2_bottom = player_2_center + 76

        # ball collision with the player 1 's paddle
        if ball_x < 100 and ball_x > 40 and ball_dx < 0:
            if player_1_y < ball_y + 25:
                if player_1_y + 150 > ball_y:
                    ball_dx *= -1
                    ball_dx *= 1.05
                    ball_dy += ball_relative_y_p1 * 4
                    bounce_sound_effect.play()

            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 50), random.randrange(0, 50), random.randrange(0, 20))
        # ball collision with the player 2 's paddle
        if ball_x > 1160 and ball_x < 1200 and ball_dx > 0:
            if player_2_y < ball_y + 25:
                if player_2_y + 150 > ball_y:
                    ball_dx *= -1
                    ball_dx *= 1.05
                    ball_dy += ball_relative_y_p2 * 4
                    bounce_sound_effect.play()

            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        # ball maximum y axis speed
        if ball_dy > 15:
            ball_dy = 15
        if ball_dy < -15:
            ball_dy = -15

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dy = random.randrange(-5, 5)
            ball_dx = random.choice([5,-5])
            score_2 += 1
            scoring_sound_effect.play()
            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dy = random.randrange(-5, 5)
            ball_dx = random.choice([5, -5])
            score_1 += 1
            scoring_sound_effect.play()
            COLOR_WHITE = (random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255))
            COLOR_BLACK = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 2 up movement
        if player_2_move_up:
            player_2_y -= 5
        else:
            player_2_y += 0

        # player 2 down movement
        if player_2_move_down:
            player_2_y += 5
        else:
            player_2_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 570:
            player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
        
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update position based values

    ball_relative_y_p1 = (ball_y - player_1_center)/75
    ball_relative_y_p2 = (ball_y - player_2_center)/75



    # remove later debug info
    #debug_text = debug_font.render(f'{ball_relative_y_p1:.2f} | player 1 center pos: {player_1_center} | ball x speed: {ball_dx:.2f} | ball y speed: {ball_dy:.2f}', True, COLOR_WHITE, COLOR_BLACK)
    #debug_text2 = debug_font.render(f'DEBUG REMOVER DEPOIS', True, COLOR_WHITE, COLOR_BLACK)
    #screen.blit(debug_text_2, debug_text_rect)
    #screen.blit(debug_text,debug_text_2_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()

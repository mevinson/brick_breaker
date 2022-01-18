import pygame
from pygame.locals import *

# Window setup
pygame.init()
dis_width = 1000
dis_height = 1000
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Brick Breaker')

# Paddle elements
pad_width = 50
pad_height = 10
pad_Lspeed = -0.75
pad_Rspeed = 0.75

# Colors:
white = (255, 255, 255)
garnet = (154, 42, 42)
black = (0, 0, 0)


def bricks():
    for i in range(46):
        for j in range(20):
            pygame.draw.rect(dis, white, [(i + 2) * 20, (j + 2) * 20, 10, 10])


def ball(ball_x, ball_y):
    pygame.draw.circle(dis, black, [ball_x, ball_y], 5)


def gameLoop():
    gameOver = False

    # pad init values
    pad_x = dis_width / 2.0
    pad_y = 900.0
    pad_x_change = 0

    # ball init values
    ball_x = 500
    ball_y = 500

    while not gameOver:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pad_x_change = pad_Lspeed
                    print("move left")
                elif event.key == pygame.K_RIGHT:
                    pad_x_change = pad_Rspeed
                    print("move right")
            if event.type == pygame.KEYUP:
                pad_x_change = 0

        ball_x -= 0.1
        ball_y -= -0.1

        pad_x += pad_x_change
        dis.fill(garnet)
        pygame.draw.rect(dis, black, [pad_x, pad_y, pad_width, pad_height])
        ball(ball_x, ball_y)
        bricks()
        pygame.display.update()
    pygame.quit()
    print("Exiting game")
    quit()


gameLoop()

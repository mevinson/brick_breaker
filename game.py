import pygame
from pygame.locals import *

# Window setup
pygame.init()
dis_width = 1000
dis_height = 1000
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Brick Breaker')

# Colors:
white = (255, 255, 255)
garnet = (154, 42, 42)
black = (0, 0, 0)


def gameLoop():
    gameOver = False
    x1 = dis_width / 2
    y1 = 800
    x_change = 0
    y_change = 0
    while not gameOver:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                    print("move left")
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                    print("move right")
        x1 += x_change
        dis.fill(garnet)
        pygame.draw.rect(dis, black, [x1, y1, 50, 10])
        pygame.display.update()
    pygame.quit()
    quit()


gameLoop()

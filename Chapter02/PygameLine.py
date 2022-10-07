import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_heigth))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
timesClicked = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            timesClicked += 1
            if timesClicked > 1:
                pygame.draw.line(screen, white, point1, point2, 1)
                timesClicked = 0

    pygame.display.update()
pygame.quit()
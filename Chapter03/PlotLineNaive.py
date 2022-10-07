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

def plot_line(point1, point2):
    x0, y0 = point1
    x1, y1 = point2
    dx = abs(x1 - x0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    dy = -abs(y1 - y0)
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx + dy

    while True:
        screen.set_at((x0, y0), white)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


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
                plot_line(point1, point2)
                timesClicked = 0

    pygame.display.update()
pygame.quit()
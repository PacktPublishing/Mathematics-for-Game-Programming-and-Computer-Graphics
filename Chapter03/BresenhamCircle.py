import pygame
from pygame.locals import *  #support for getting mouse button events

pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,
                                  screen_height))
done = False
white = pygame.Color(255, 255, 255)

def circle_points(x, y, center):
    screen.set_at((x + center[0], y + center[1]), white)
    screen.set_at((y + center[0], x + center[1]), white)
    screen.set_at((y + center[0], -x + center[1]), white)
    screen.set_at((x + center[0], -y + center[1]), white)
    screen.set_at((-x + center[0], -y + center[1]), white)
    screen.set_at((-y + center[0], -x + center[1]), white)
    screen.set_at((-y + center[0], x + center[1]), white)
    screen.set_at((-x + center[0], y + center[1]), white)


def plot_circle(radius, center):
    x = 0
    y = radius
    d = 5/4.0 - radius
    circle_points(x, y, center)
    while y > x:
        if d < 0:  # select E
            d = d + 2 * x + 3
            x += 1
        else:  # select SE
            d = d + 2 * (x - y) + 5
            x = x + 1
            y = y - 1
        circle_points(x, y, center)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    plot_circle(50, (200, 200))
    pygame.display.update()
pygame.quit()

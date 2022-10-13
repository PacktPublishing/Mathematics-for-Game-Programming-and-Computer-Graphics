import pygame
from pygame.locals import *

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
white = pygame.Color(255, 255, 255)
mouse_down = False
last_mouse_pos =(0, 0)
green = pygame.Color(0, 255, 0)
button = (0, 0, 100, 30)
while not done:
    pygame.draw.rect(screen, green, button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
        elif event.type == MOUSEMOTION and mouse_down is True:
            pygame.draw.line(screen, white, last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
            if button[0] < mpos[0] < (button[0] + button[2]) and button[1] < mpos[1] < (button[1] + button[3]):
                print("Mouse Over")
    pygame.display.update()
pygame.quit()

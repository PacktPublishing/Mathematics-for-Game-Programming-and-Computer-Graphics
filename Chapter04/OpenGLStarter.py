import pygame
from pygame.locals import *
from OpenGL.GL import *

pygame.init()

screen_width = 500
screen_heigth = 500

screen = pygame.display.set_mode((screen_width, screen_heigth), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")
done = False
white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.flip()
pygame.quit()
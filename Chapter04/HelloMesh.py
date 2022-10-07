import pygame

from Mesh3D import *
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 500
screen_heigth = 500

screen = pygame.display.set_mode((screen_width, screen_heigth), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")
done = False
white = pygame.Color(255, 255, 255)
gluPerspective(30, (screen_width // screen_heigth), 0.1, 100.0)
# glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0.0, 0.0, -3.0)
mesh = Cube()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    mesh.draw()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
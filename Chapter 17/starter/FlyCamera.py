import math

import pygame
from Object import *
#from Display_Normals import *
from pygame.locals import *
from OpenGL.GLU import *
from LoadMesh import *
from Cube import *
from Camera import *
from Camera2D import *

pygame.init()
screen_width = math.fabs(window_dimensions[1] - window_dimensions[0])
screen_height = math.fabs(window_dimensions[3] - window_dimensions[2])
pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
done = False
white = pygame.Color(255, 255, 255)

objects_3d = []
objects_2d = []

teapot = Object("Teapot")
teapot.add_component(Transform())
teapot.add_component(LoadMesh(GL_LINE_LOOP, "../models/teapotSM.obj"))
trans: Transform = teapot.get_component(Transform)
trans.rotate_y(90)
trans.update_position(pygame.Vector3(0,-2,-3))

camera = Camera(60, (screen_width/screen_height), 0.1, 1000.0)
camera2D = Camera2D(gui_dimensions[0], gui_dimensions[1], gui_dimensions[3], gui_dimensions[2])

objects_3d.append(teapot)

clock = pygame.time.Clock()
fps = 30

def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(camera2D.get_PPM())
    #glLoadIdentity()  # reset projection matrix
    #gluOrtho2D(gui_dimensions[0], gui_dimensions[1], gui_dimensions[3], gui_dimensions[2])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # reset modelview matrix
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(camera.get_PPM())
    #glLoadIdentity()
    #gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)
    #pv = glGetDoublev(GL_PROJECTION_MATRIX)
    #print("PV: ")
    #print(pv)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_LIGHTING)
    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 0, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))
    glEnable(GL_LIGHT0)


pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
            if event.key == K_SPACE:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)


    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.update()

    set_3d()
    for o in objects_3d:
        o.update(camera, events)

    set_2d()
    for o in objects_2d:
        o.update(events)

    glPopMatrix()
    pygame.display.flip()
    dt = clock.tick(fps)
pygame.quit()
import math

from Object import *
from pygame.locals import *
from OpenGL.GLU import *
from Cube import *

pygame.init()
screen_width = math.fabs(window_dimensions[1] - window_dimensions[0])
screen_height = math.fabs(window_dimensions[3] - window_dimensions[2])
pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
done = False
white = pygame.Color(255, 255, 255)

objects_3d = []
objects_2d = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, 0)))
cube.add_component(Cube(GL_POLYGON, "../images/wall.tif"))
trans: Transform = cube.get_component(Transform)
trans.set_position((0, 0, -3))
trans.set_rotation_axis(pygame.Vector3(1, 0, 0))
trans.update_rotation_angle(45)
trans.set_scale(pygame.Vector3(0.5, 2, 1))

objects_3d.append(cube)

clock = pygame.time.Clock()
fps = 30

def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # reset projection matrix
    gluOrtho2D(gui_dimensions[0], gui_dimensions[1],
                       gui_dimensions[3], gui_dimensions[2])
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # reset modelview matrix
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 0, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))
    glEnable(GL_LIGHT0)

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_3d()
    for o in objects_3d:
        o.update(events)

    set_2d()
    for o in objects_2d:
        o.update(events)

    glPopMatrix()
    pygame.display.flip()
    dt = clock.tick(fps)
pygame.quit()

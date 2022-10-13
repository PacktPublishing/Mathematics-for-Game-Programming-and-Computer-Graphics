import math

from Object import *
from Cube import *
from Grid import *
from DisplayNormals import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, "images/wall.tif"))
cube.add_component(DisplayNormals(cube.get_component(Cube).vertices, cube.get_component(Cube).triangles))

cube2 = Object("Cube")
cube2.add_component(Transform((0, 1, -5)))
cube2.add_component(Cube(GL_POLYGON, "images/brick.tif"))

objects_3d.append(cube)
objects_3d.append(cube2)

grid = Object("Grid")
grid.add_component(Transform((0, 0, -5)))
grid.add_component(Grid(0.5, 8, (0, 0, 255)))

objects_3d.append(grid)

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


trans: Transform = cube.get_component(Transform)
start_position = pygame.Vector3(-3, 0, -5)
end_position = pygame.Vector3(0, 0, -5)
v = end_position - start_position
t = 0
trans.set_position(start_position)
dt = 0

trans2: Transform = cube2.get_component(Transform)
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    if t <= 1:
        trans.set_position(start_position + t * v)
        t += 0.0001 * dt

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

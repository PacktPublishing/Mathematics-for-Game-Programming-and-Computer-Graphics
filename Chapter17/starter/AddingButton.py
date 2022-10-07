from Button import *
from Cube import *
from Object import *
from Settings import *
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen_width = math.fabs(window_dimensions[1] - window_dimensions[0])
screen_height = math.fabs(window_dimensions[3] - window_dimensions[2])

pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width, screen_height),
                                 DOUBLEBUF | OPENGL)

done = False
white = pygame.Color(255, 255, 255)

objects_3d = []
objects_2d = []

cube = Object("Cube")
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, "../images/crate.png"))

objects_3d.append(cube)

def button_click():
    print("Hello Button")

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

button1 = Object("Button")
button1.add_component(Button(screen, (0, 0), 100, 50, white, green, blue, button_click))

objects_2d.append(button1)

clock = pygame.time.Clock()
fps = 30


def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # reset projection matrix
    # gluOrtho2D(0, screen.get_width(), 0, screen.get_height())
    gluOrtho2D(gui_dimensions[0], gui_dimensions[1], gui_dimensions[3], gui_dimensions[2])

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # reset modelview matrix
    glViewport(0, 0, screen.get_width(), screen.get_height())


def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height),

                   0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

trans: Transform = cube.get_component(Transform)

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        trans.move_x(-0.1)
    if keys[pygame.K_RIGHT]:
        trans.move_x(0.1)
    if keys[pygame.K_UP]:
        trans.move_y(0.1)
    if keys[pygame.K_DOWN]:
        trans.move_y(-0.1)

    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    set_3d()
    for o in objects_3d:
        o.update()

    set_2d()
    for o in objects_2d:
        o.update(events)

    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)
    print(pygame.mouse.get_pos())
pygame.quit()

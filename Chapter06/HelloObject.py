from Object import *
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Python")
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
# glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)
objects = []
cube = Object("Cube")
cube.add_component(Transform((0, 0, 0)))
cube.add_component(Cube(GL_POLYGON, "../images/wall.tif"))
objects.append(cube)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))

glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))
clock = pygame.time.Clock()
fps = 60
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    for o in objects:
        o.update()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
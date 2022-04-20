from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Lights in OpenGL')
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))
glMaterial(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

glEnable(GL_LIGHT0)

# Change path name to suit your directory structure
mesh = Cube(GL_POLYGON, "../images/bricks.jpg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    mesh.draw()
    pygame.display.flip()
    pygame.time.wait(50)
pygame.quit()

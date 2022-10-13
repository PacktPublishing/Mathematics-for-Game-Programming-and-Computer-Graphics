from Object import *
from pygame.locals import *
from Camera import *
from LoadMesh import *
from Material import *
from Settings import *

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
screen_width = math.fabs(window_dimensions[1] - window_dimensions[0])
screen_height = math.fabs(window_dimensions[3] - window_dimensions[2])
pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
done = False
white = pygame.Color(255, 255, 255)
glDisable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
objects_3d = []
camera = Camera(60, (screen_width / screen_height), 0.01, 10000.0)

quat_teapot = Object("Teapot")
quat_teapot.add_component(Transform())
mat = Material("shaders/vertexcolvert.vs", "shaders/vertexcolfrag.vs")
quat_teapot.add_component(LoadMesh(quat_teapot.vao_ref, mat, GL_LINE_LOOP, "../models/teapotSM.obj"))
quat_teapot.add_component(mat)
quat_trans: Transform = quat_teapot.get_component(Transform)
quat_trans.update_position(pygame.Vector3(0, 0, 0))

objects_3d.append(quat_teapot)

clock = pygame.time.Clock()
fps = 30

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

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.update()
    for o in objects_3d:
        o.update(camera, events)

    pygame.display.flip()
    dt = clock.tick(fps)
pygame.quit()

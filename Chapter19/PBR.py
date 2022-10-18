from Object import *
from pygame.locals import *
from Camera import *
from LoadMesh import *
from Material import *
from Settings import *
from Light import *

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
#put this next line back in for Mac
#pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
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

for x in range(10):
    for y in range(10):
        sphere = Object("Sphere")
        sphere.add_component(Transform())
        mat = Material("shaders/pbrvert.vs",
                       "shaders/pbrfrag.vs")
        sphere.add_component(
                            LoadMesh(sphere.vao_ref, mat,
                            GL_TRIANGLES,
                            "models/sphere.obj"))
        sphere_mesh: LoadMesh = sphere.get_component(LoadMesh)
        sphere_mesh.set_properties(
              pygame.Vector3(1, 0, 1),
              x/10.0, x/10.0, y/10.0)
        sphere.add_component(mat)
        sphere_trans: Transform = sphere.get_component(Transform)
        sphere_trans.update_position(
                pygame.Vector3(x*20, y*20, -20))
        objects_3d.append(sphere)


lights = []
lights.append(Light(pygame.Vector3(0, 100, 200), pygame.Vector3(0, 1, 1), 5, 0))
lights.append(Light(pygame.Vector3(0, 50, 200), pygame.Vector3(1, 0, 1), 2, 1))
lights.append(Light(pygame.Vector3(100, 0, 200), pygame.Vector3(1, 1, 0), 5, 2))

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
        o.update(camera, lights, events)

    pygame.display.flip()
    dt = clock.tick(fps)
pygame.quit()

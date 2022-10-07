from Mesh3D import *
from Transform import *
from Button import *
from Grid import *
from Display_Normals import *
from Camera import *

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        self.scene_angle = 0

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)
        self.components.append(component)

    def update(self, camera: Camera, events = None):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                glLoadMatrixf(c.get_MVM() * camera.get_VM())
                #mv = glGetDoublev(GL_MODELVIEW_MATRIX)
                #print("MV: ")
                #print(mv)
            elif isinstance(c, Mesh3D):
                glColor(1, 1, 1)
                c.draw()
            elif isinstance(c, Grid):
                c.draw()
            elif isinstance(c,DisplayNormals):
                c.draw()

        glPopMatrix()

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None

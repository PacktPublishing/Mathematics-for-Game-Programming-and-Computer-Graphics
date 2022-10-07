from Mesh3D import *
from Transform import *
from Button import *
from Grid import *

class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)
        self.components.append(component)

    def update(self, events = None):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                pos = c.get_position()
                glTranslatef(pos.x, pos.y, pos.z)
            elif isinstance(c, Mesh3D):
                c.draw()
            elif isinstance(c, Grid):
                c.draw()

        glPopMatrix()

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None

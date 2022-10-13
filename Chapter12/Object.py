from Mesh3D import *
from Transform import *
from Button import *
from Grid import *
from DisplayNormals import *


class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        self.scene_angle = 45

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)
        self.components.append(component)

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None


    def update(self, events = None):
        glPushMatrix()
        for c in self.components:
            if isinstance(c, Transform):
                pos = c.get_position()
                scale = c.get_scale()
                rot_angle = c.get_rotation_angle()
                rot_axis = c.get_rotation_axis()

                glTranslatef(pos.x, pos.y, pos.z)
                glScalef(scale.x, scale.y, scale.z)
                glRotated(rot_angle, rot_axis.x, rot_axis.y, rot_axis.z)


            elif isinstance(c, Mesh3D):
                glColor(1, 1, 1)
                c.draw()
            elif isinstance(c, Grid):
                c.draw()
            elif isinstance(c, DisplayNormals):
                c.draw()
            elif isinstance(c, Button):
                c.draw(events)
        glPopMatrix()

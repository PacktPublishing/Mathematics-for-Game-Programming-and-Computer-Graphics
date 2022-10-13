from LoadMesh import *
from Camera import *
from Material import *
from Uniform import *


class Object:
    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []
        self.material = None
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)

    def add_component(self, component):
        if isinstance(component, Transform):
            self.components.insert(0, self.components)
        if isinstance(component, Material):
            self.material = component
        self.components.append(component)

    def get_component(self, class_type):
        for c in self.components:
            if type(c) is class_type:
                return c
        return None


    def update(self, camera: Camera, events = None):
        self.material.use()
        for c in self.components:
            if isinstance(c, Transform):
                projection = Uniform("mat4", camera.get_PPM())
                projection.find_variable(self.material.program_id, "projection_mat")
                projection.load()

                lookat = Uniform("mat4", camera.get_VM())
                lookat.find_variable(self.material.program_id, "view_mat")
                lookat.load()

                transformation = Uniform("mat4", c.get_MVM())
                transformation.find_variable(self.material.program_id, "model_mat")
                transformation.load()

            elif isinstance(c, LoadMesh):
                c.draw()







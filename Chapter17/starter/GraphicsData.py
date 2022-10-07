from OpenGL.GL import *
import numpy as np

class GraphicsData():
    def __init__(self, data_type, data):
        self.data_type = data_type
        self.data = data
        self.buffer_ref = glGenBuffers(1)
        self.load()

    def load(self):
        data = np.array(self.data, np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    def create_variable(self, program_id, variable_name):
        variable_id = glGetAttribLocation(program_id, variable_name)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)
        if self.data_type == "vec3":
            glVertexAttribPointer(variable_id, 3, GL_FLOAT, False, 0, None)
        elif self.data_type == "vec2":
            glVertexAttribPointer(variable_id, 2, GL_FLOAT, False, 0, None)

        glEnableVertexAttribArray(variable_id)

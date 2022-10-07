from Mesh3D import *

class LoadMesh(Mesh3D):
    def __init__(self, draw_type, model_filename):
        self.vertices, self.triangles = self.load_drawing(model_filename)
        self.draw_type = draw_type

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)


    def load_drawing(self, filename):
        vertices = []
        triangles = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in
                                  line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in
                                  line[2:].split()]
                    triangles.append(
               [int(value) for value in t1.split('/')][0] - 1)
                    triangles.append(
               [int(value) for value in t2.split('/')][0] - 1)
                    triangles.append(
              [int(value) for value in t3.split('/')][0] - 1)
                line = fp.readline()
        return vertices, triangles


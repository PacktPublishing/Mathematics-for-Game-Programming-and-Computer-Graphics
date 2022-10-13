from Mesh3D import *


class LoadMesh(Mesh3D):
    def __init__(self, draw_type, model_filename, texture_file="", back_face_cull=False):
        self.vertices, self.uvs, self.normals, self.normal_ind, self.triangles = self.load_drawing(model_filename)
        self.texture_file = texture_file
        self.draw_type = draw_type
        self.back_face_cull = back_face_cull

        if self.texture_file != "":
            self.texture = pygame.image.load(texture_file)
            self.texID = 0
            self.texID = glGenTextures(1)
            textureData = pygame.image.tostring(self.texture, "RGB", 1)
            width = self.texture.get_width()
            height = self.texture.get_height()
            glBindTexture(GL_TEXTURE_2D, self.texID)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)

    def draw(self):
        if self.back_face_cull:
            glEnable(GL_CULL_FACE)
        if self.texture_file != "":
            glEnable(GL_TEXTURE_2D)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
            glBindTexture(GL_TEXTURE_2D, self.texID)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            if self.texture_file != "":
                glTexCoord2fv(self.uvs[self.triangles[t]])
            glNormal3fv(self.normals[self.normal_ind[t]])
            glVertex3fv(self.vertices[self.triangles[t]])
            if self.texture_file != "":
                glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glNormal3fv(self.normals[self.normal_ind[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            if self.texture_file != "":
                glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glNormal3fv(self.normals[self.normal_ind[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        if self.texture_file != "":
            glDisable(GL_TEXTURE_2D)
        if self.back_face_cull:
            glDisable(GL_CULL_FACE)

    def load_drawing(self, filename):
        vertices = []
        uvs = []
        normals = []
        normal_ind = []
        triangles = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "vn":
                    vx, vy, vz = [float(value) for value in line[3:].split()]
                    normals.append((vx, vy, vz))
                if line[:2] == "vt":
                    vx, vy = [float(value) for value in line[3:].split()]
                    uvs.append((vx, vy))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0] - 1)
                    triangles.append([int(value) for value in t2.split('/')][0] - 1)
                    triangles.append([int(value) for value in t3.split('/')][0] - 1)
                    normal_ind.append([int(value) for value in t1.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t2.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t3.split('/')][2] - 1)
                line = fp.readline()
        return vertices, uvs, normals, normal_ind, triangles


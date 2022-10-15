from Mesh3D import *
from GraphicsData import *
from Uniform import *
from Texture import *
from Utils import *


class LoadMesh(Mesh3D):
    def __init__(self, vao_ref, material, draw_type, model_filename, texture_file="", back_face_cull=False):
        self.vertices, self.uvs, self.uvs_ind, self.normals, self.normal_ind, self.triangles = self.load_drawing(model_filename)
        self.coordinates = self.format_vertices(self.vertices, self.triangles)
        self.norms = self.format_vertices(self.normals, self.normal_ind)
        self.uv_vals = self.format_vertices(self.uvs, self.uvs_ind)
        self.draw_type = draw_type
        self.vao_ref = vao_ref
        self.material = material
        position = GraphicsData("vec3", self.coordinates)
        position.create_variable(material.program_id, "position")
        vertex_normals = GraphicsData("vec3", self.norms)
        vertex_normals.create_variable(material.program_id, "vertex_normal")
        #v_uvs = GraphicsData("vec2", self.uv_vals)
        #v_uvs.create_variable(self.material.program_id, "vertex_uv")
        self.albedo = None
        self.metallic = None
        self.roughness = None
        self.ao = None
        #if texture_file is not None:
            #self.image = Texture(texture_file)
            #self.texture = Uniform("sampler2D", [self.image.texture_id, 1])

    def format_vertices(self, coordinates, triangles):
        allTriangles = []
        for t in range(0, len(triangles), 3):
            allTriangles.append(coordinates[triangles[t]])
            allTriangles.append(coordinates[triangles[t + 1]])
            allTriangles.append(coordinates[triangles[t + 2]])
        return np.array(allTriangles, np.float32)

    def set_properties(self, albedo, metallic, roughness, ao):
        self.albedo = Uniform("vec3", albedo)
        self.metallic = Uniform("float", metallic)
        self.roughness = Uniform("float", roughness)
        self.ao = Uniform("float", ao)

    def draw(self):
        #if self.texture is not None:
        #    self.texture.find_variable(self.material.program_id, "albedo")
        #    self.texture.load()
        self.albedo.find_variable(self.material.program_id, "albedo")
        self.albedo.load()

        self.metallic.find_variable(self.material.program_id, "metallic")
        self.metallic.load()

        self.roughness.find_variable(self.material.program_id, "roughness")
        self.roughness.load()

        self.ao.find_variable(self.material.program_id, "ao")
        self.ao.load()

        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.coordinates))

    def load_drawing(self, filename):
        vertices = []
        uvs = []
        uvs_ind = []
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
                    uvs_ind.append([int(value) for value in t1.split('/')][1] - 1)
                    uvs_ind.append([int(value) for value in t2.split('/')][1] - 1)
                    uvs_ind.append([int(value) for value in t3.split('/')][1] - 1)
                    normal_ind.append([int(value) for value in t1.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t2.split('/')][2] - 1)
                    normal_ind.append([int(value) for value in t3.split('/')][2] - 1)
                line = fp.readline()
        return vertices, uvs, uvs_ind, normals, normal_ind, triangles


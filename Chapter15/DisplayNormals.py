import pygame
from OpenGL.GL import *
from MathOGL import *


class DisplayNormals:

    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles
        self.normals = []
        for t in range(0, len(self.triangles), 3):
            vertex1 = self.vertices[self.triangles[t]]
            vertex2 = self.vertices[self.triangles[t + 1]]
            vertex3 = self.vertices[self.triangles[t + 2]]
            p = pygame.Vector3(vertex1[0] - vertex2[0],
                               vertex1[1] - vertex2[1],
                               vertex1[2] - vertex2[2])
            q = pygame.Vector3(vertex2[0] - vertex3[0],
                               vertex2[1] - vertex3[1],
                               vertex2[2] - vertex3[2])

            norm = cross_product(p, q)

            #find median
            middle = (vertex3 + q * 0.5)
            v = (middle - vertex1) * 2/3
            median = vertex1 + v
            nstart = median
            self.normals.append((nstart, nstart + norm * 10))
            print(vertex1, vertex2, vertex3, middle, v, nstart, p, q)


    def draw(self):
        glColor3fv((0, 1, 0))
        glBegin(GL_LINES)
        for i in range(0, len(self.normals)):
            start_point = self.normals[i][0]
            end_point = self.normals[i][1]
            glVertex3fv((start_point[0], start_point[1], start_point[2]))
            glVertex3fv((end_point[0], end_point[1], end_point[2]))
        glEnd()

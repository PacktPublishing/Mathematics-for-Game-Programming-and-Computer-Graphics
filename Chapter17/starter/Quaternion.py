from __future__ import annotations
import pygame
import math
import numpy as np
import sys

class Quaternion:
    def __init__(self, vector=None, axis: pygame.Vector3 = None, angle: float=None):
        if vector is not None:
            self.w = vector[0]
            self.x = vector[1]
            self.y = vector[2]
            self.z = vector[3]
        else:
            axis = axis.normalize()
            sin_angle = math.sin(math.radians(angle/2.0))
            cos_angle = math.cos(math.radians(angle/2.0))
            self.w = cos_angle
            self.x = axis.x * sin_angle
            self.y = axis.y * sin_angle
            self.z = axis.z * sin_angle
        self.normalise()

    def normalise(self):
        l = math.sqrt(self.w * self.w + self.x * self.x +
                      self.y * self.y + self.z * self.z)
        if l > sys.float_info.epsilon:
            self.w /= l
            self.x /= l
            self.y /= l
            self.z /= l

    def __mul__(self, other: Quaternion):
        v1 = pygame.Vector3(self.x, self.y, self.z)
        v2 = pygame.Vector3(other.x, other.y, other.z)
        cross = v1.cross(v2)
        dot = v1.dot(v2)
        v3 = cross + (self.w * v2) + (other.w * v1)
        result = Quaternion(vector=(self.w * other.w - dot, v3.x, v3.y, v3.z))
        return result

    def get_matrix(self):
        x2 = self.x + self.x
        y2 = self.y + self.y
        z2 = self.z + self.z
        xx2 = self.x * x2
        xy2 = self.x * y2
        xz2 = self.x * z2
        yy2 = self.y * y2
        yz2 = self.y * z2
        zz2 = self.z * z2
        wx2 = self.w * x2
        wy2 = self.w * y2
        wz2 = self.w * z2

        return np.matrix([
            [1 - (yy2 + zz2), xy2 + wz2, xz2 - wy2, 0],
            [ xy2 - wz2, 1 - (xx2 + zz2), yz2 + wx2, 0],
            [xz2 + wy2, yz2 - wx2, 1 - (xx2 + yy2), 0],
            [0, 0, 0, 1]])


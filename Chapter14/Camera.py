import pygame
import math
import numpy as np


class Camera:
    def __init__(self, fovy, aspect, near, far):
        f = 1/math.tan(math.radians(fovy/2))
        a = f/aspect
        b = f
        c = (far + near) / (near - far)
        d = 2 * near * far / (near - far)
        self.PPM = np.matrix([
            [a, 0, 0, 0],
            [0, b, 0, 0],
            [0, 0, c, -1],
            [0, 0, d, 0]
        ])
        self.VM = np.identity(4)

    def get_VM(self):
        return self.VM

    def get_PPM(self):
        return self.PPM

    def get_position(self):
        position = pygame.Vector3(self.VM[0, 3], self.VM[1, 3], self.VM[2, 3])
        return position

    def update_position(self, position: pygame.Vector3):
        self.VM = self.VM @ np.matrix([[1, 0, 0, 0],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 0],
                                       [position.x, position.y, position.z, 1]])

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.update_position(self.get_position() + pygame.Vector3(0, 0, 0.01))
        if key[pygame.K_s]:
            self.update_position(self.get_position() + pygame.Vector3(0, 0, -0.01))


import pygame
import math
import numpy as np
from Quaternion import *

class Transform:
    def __init__(self):
        self.MVM = np.identity(4)

    def get_MVM(self):
        return self.MVM

    def update_position(self, position):
        self.MVM = self.MVM @ np.matrix(
            [[1,0,0,0],
             [0,1,0,0],
             [0,0,1,0],
             [position.x, position.y, position.z, 1]]
        )

    def update_scale(self, amount: pygame.math.Vector3):
        self.scale = amount
        self.MVM = self.MVM @ np.matrix(
            [[amount.x,0,0,0],
             [0,amount.y,0,0],
             [0,0,amount.z,0],
             [0,0,0,1]]
        )

    def rotate_x(self, amount, local=True):
        amount = math.radians(amount)
        if local:
            self.MVM = self.MVM @ np.matrix(
                [[1,0,0,0],
                 [0,math.cos(amount),math.sin(amount),0],
                 [0,-math.sin(amount),math.cos(amount),0],
                 [0,0,0,1]]
            )
        else:
            self.MVM = np.matrix(
                [[1, 0, 0, 0],
                 [0, math.cos(amount), math.sin(amount), 0],
                 [0, -math.sin(amount), math.cos(amount), 0],
                 [0, 0, 0, 1]] @ self.MVM
        )

    def rotate_y(self, amount, local=True):
        amount = math.radians(amount)
        if local:
            self.MVM = self.MVM @ np.matrix([
                [math.cos(amount),0,-math.sin(amount),0],
                [0,1,0,0],
                [math.sin(amount),0,math.cos(amount),0],
                [0,0,0,1]])
        else:
            self.MVM = np.matrix([
                [math.cos(amount), 0, -math.sin(amount), 0],
                [0, 1, 0, 0],
                [math.sin(amount), 0, math.cos(amount), 0],
                [0, 0, 0, 1]]) @ self.MVM

    def rotate_z(self, amount, local=True):
        amount = math.radians(amount)
        if local:
            self.MVM = self.MVM @ np.matrix([
                [math.cos(amount),math.sin(amount),0,0],
                [-math.sin(amount),math.cos(amount),0,0],
                [0,0,1,0],
                [0,0,0,1]])
        else:
            self.MVM = np.matrix([
                [math.cos(amount), math.sin(amount), 0, 0],
                [-math.sin(amount), math.cos(amount), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]) @ self.MVM

    def rotate_axis(self, axis: pygame.Vector3, angle, local=True):
        q = Quaternion(axis=axis, angle=angle)
        r_mat = q.get_matrix()
        if local:
            self.MVM = self.MVM @ r_mat
        else:
            self.MVM = r_mat @ self.MVM

    def get_position(self):
        position = pygame.Vector3(self.MVM[0, 3], self.MVM[1, 3],
                                  self.MVM[2, 3])
        return position

    def get_scale(self):
        sx = pygame.Vector3(self.MVM[0, 0], self.MVM[1, 0],
                            self.MVM[2, 0])
        sy = pygame.Vector3(self.MVM[0, 1], self.MVM[1, 1],
                            self.MVM[2, 1])
        sz = pygame.Vector3(self.MVM[0, 2], self.MVM[1, 2],
                            self.MVM[2, 2])
        return pygame.Vector3(sx.magnitude(), sy.magnitude(),
                              sz.magnitude())

    def get_rotation(self):
        scale = self.get_scale()
        rotation = np.identity(4)
        rotation[0, 0] = self.MVM[0, 0] / scale.x
        rotation[0, 1] = self.MVM[0, 1] / scale.x
        rotation[0, 2] = self.MVM[0, 2] / scale.x
        rotation[1, 0] = self.MVM[1, 0] / scale.y
        rotation[1, 1] = self.MVM[1, 1] / scale.y
        rotation[1, 2] = self.MVM[1, 2] / scale.y
        rotation[2, 0] = self.MVM[2, 0] / scale.z
        rotation[2, 1] = self.MVM[2, 1] / scale.z
        rotation[2, 2] = self.MVM[2, 2] / scale.z
        return rotation

    def rotate_quaternion(self, quaternion: Quaternion, local=True):
        r_mat = quaternion.get_matrix()
        if local:
            self.MVM = self.MVM @ r_mat
        else:
            self.MVM = r_mat @ self.MVM


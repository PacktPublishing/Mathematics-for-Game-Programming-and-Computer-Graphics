import pygame
import math
import numpy as np
from Transform import *


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
        self.transform = Transform()
        self.pan_speed = 0.1
        self.rotate_speed = 10
        self.last_mouse = pygame.math.Vector2(0, 0)
        self.mouse_sensitivityX = 0.5
        self.mouse_sensitivityY = 0.5
        self.mouse_invert = -1

    def get_VM(self):
        return self.transform.MVM

    def get_PPM(self):
        return self.PPM

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.transform.update_position(self.transform.get_position() + pygame.Vector3(0, 0, self.pan_speed), False)
        if key[pygame.K_s]:
            self.transform.update_position(self.transform.get_position() + pygame.Vector3(0, 0, -self.pan_speed), False)
        if key[pygame.K_a]:
            self.transform.update_position(self.transform.get_position() + pygame.Vector3(self.pan_speed, 0, 0), False)
        if key[pygame.K_d]:
            self.transform.update_position(self.transform.get_position() + pygame.Vector3(-self.pan_speed, 0, 0), False)
        if key[pygame.K_q]:
            self.transform.rotate_y(self.rotate_speed)
        if key[pygame.K_e]:
            self.transform.rotate_y(-self.rotate_speed)

        if not pygame.mouse.get_visible():
            mouse_pos = pygame.mouse.get_pos()
            mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
            pygame.mouse.set_pos(pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2)
            self.last_mouse = pygame.mouse.get_pos()
            self.rotate_with_mouse(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

    def rotate_with_mouse(self, yaw, pitch):
        forward = pygame.Vector3(self.get_VM()[0, 2], self.get_VM()[1, 2], self.get_VM()[2, 2])
        up = pygame.Vector3(0, 1, 0)
        angle = forward.angle_to(up)
        self.transform.rotate_y(self.mouse_invert * yaw * self.mouse_sensitivityY, False)
        if angle < 170.0 and pitch > 0 or angle > 30.0 and pitch < 0:
            self.transform.rotate_x(self.mouse_invert * pitch * self.mouse_sensitivityX, False)


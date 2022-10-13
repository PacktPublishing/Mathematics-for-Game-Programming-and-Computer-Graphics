import pygame

class Transform:
    def __init__(self, position):
        self.set_position(position)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = pygame.math.Vector3(position)

    def move_x(self, amount):
        self.position = pygame.math.Vector3(self.position.x + amount, self.position.y, self.position.z)

    def move_y(self, amount):
        self.position = pygame.math.Vector3(self.position.x, self.position.y + amount, self.position.z)
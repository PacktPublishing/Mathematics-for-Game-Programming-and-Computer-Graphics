import pygame

class Transform:
   def __init__(self, position):
       self.set_position(position)

   def get_position(self):
       return self.position

   def set_position(self, position):
       self.position = pygame.math.Vector3(position)

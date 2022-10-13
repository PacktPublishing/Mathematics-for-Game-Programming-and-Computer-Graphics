import pygame

def cross_product(v, w):
    return pygame.Vector3((v.y*w.z - v.z*w.y), (v.x*w.z - v.z*w.x), (v.x*w.y - v.y*w.x))


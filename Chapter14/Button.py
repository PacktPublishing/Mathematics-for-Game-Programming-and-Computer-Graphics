import pygame
from pygame.locals import *
from OpenGL.GL import *
from Utils import *
from Settings import *

class Button:
    def __init__(self, screen, position, width, height, color, ocolor, pcolor, on_click):
        self.position = position
        self.width = width
        self.height = height
        self.screen = screen
        self.normal_color = color
        self.over_color = ocolor
        self.pressed_color = pcolor
        self.mouse_down = False
        self.on_click = on_click


    def draw(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mx = map_value(window_dimensions[0], window_dimensions[1],
                       gui_dimensions[0], gui_dimensions[1], mouse_pos[0])
        my = map_value(window_dimensions[2], window_dimensions[3],
                       gui_dimensions[2], gui_dimensions[3], mouse_pos[1])

        glPushMatrix()
        glLoadIdentity()
        # if mouse over button
        if self.position[0] < mx < (self.position[0] + self.width) and \
                self.position[1] < my < (self.position[1] + self.height):

            for e in events:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    self.mouse_down = True
                    self.on_click()
                elif e.type == MOUSEBUTTONUP and e.button == 1:
                    self.mouse_down = False
            if self.mouse_down:
                glColor3f(self.pressed_color[0], self.pressed_color[1], self.pressed_color[2])
            else:
                glColor3f(self.over_color[0], self.over_color[1], self.over_color[2]);
        else:
            glColor3f(self.normal_color[0], self.normal_color[1], self.normal_color[2]);
        glBegin(GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()






from OpenGL.GL import *

class Grid():
    def __init__(self, interval, halfsize, color):
        self.interval = interval
        self.halfsize = halfsize
        self.color = color

    def draw(self):
        glColor3fv(self.color)
        glBegin(GL_LINES)
        for x in range(-self.halfsize, self.halfsize):
            for y in range(-self.halfsize, self.halfsize):
                glVertex3fv((x * self.interval, y * self.interval - 10, 0))
                glVertex3fv((x * self.interval, y * self.interval + 500, 0))
                glVertex3fv((y * self.interval - 10, x * self.interval, 0))
                glVertex3fv((y * self.interval + 500, x * self.interval, 0))
        glEnd()

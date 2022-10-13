from Transform import *
from Uniform import *


class Light:
    def __init__(self, position=pygame.Vector3(0, 0, 0), color=pygame.Vector3(1, 1, 1), atten=0, light_number=0):
        self.position = position
        self.atten = atten
        self.color = color
        self.light_variable = "light_data[" + str(light_number) + "].position"
        self.atten_variable = "light_data[" + str(light_number) + "].attenuation"
        self.color_variable = "light_data[" + str(light_number) + "].color"



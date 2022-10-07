import numpy as np


class Camera2D:
    def __init__(self, left, right, top, bottom):
        near_val = -1
        far_val = 1
        a = 2/(right-left)
        b = 2/(top-bottom)
        c = -2/(far_val - near_val)
        d = -(right + left)/(right - left)
        e = -(top + bottom)/(top - bottom)
        f = -(far_val + near_val)/(far_val - near_val)
        self.PPM = np.matrix([
            [a, 0, 0, 0],
            [0, b, 0, 0],
            [0, 0, c, 0],
            [d, e, f, 0]
        ])
        self.VM = np.identity(4)

    def get_PPM(self):
        return self.PPM

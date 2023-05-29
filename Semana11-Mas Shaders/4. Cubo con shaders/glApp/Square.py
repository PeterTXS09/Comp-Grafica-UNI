from .Mesh import *

class Square(Mesh):
    def __init__(self, program_id, location):
        vertices = [[ 0.5,  0.5, -1.0],
                    [ 0.5, -0.5, -1.0],
                    [-0.5, -0.5, -1.0],
                    [-0.5,  0.5, -1.0]]

        colors = [[1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0],
                  [1.0, 0.0, 1.0]]
        super().__init__(program_id, vertices, colors, GL_TRIANGLE_FAN, location)
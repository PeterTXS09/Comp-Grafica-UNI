import pygame

from .Mesh import *
from .Utils import format_vertices

class Cube(Mesh):
    def __init__(self, program_id, location=pygame.Vector3(0, 0, 0)):
        coordinates = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, -0.5, -0.5),
                         (-0.5, -0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (-0.5, 0.5, -0.5),
                         (-0.5, -0.5, -0.5),
                         (0.5, -0.5, -0.5),
                         (0.5, 0.5, -0.5),
                         (0.5, 0.5, 0.5),
                         (0.5, -0.5, 0.5)]
        triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
                     13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]
        colors = [0.49003227, 0.79483813, 0.75940506,
                  0.42319287, 0.43266072, 0.03658556,
                  0.30616817, 0.43356325, 0.61798824,
                  0.11685137, 0.35776707, 0.6440496,
                  0.37705121, 0.9329588,  0.23876349,
                  0.07577037, 0.57541673, 0.3763994,
                  0.2785837, 0.93675507, 0.82039642,
                  0.49136861, 0.92484412, 0.15922967,
                  0.31429208, 0.06344174, 0.72207986,
                  0.17362509, 0.67128428, 0.34815369,
                  0.64012601, 0.61081542, 0.98774679,
                  0.10549675, 0.9466021, 0.02848752,
                  0.66511925, 0.0455912, 0.14421397,
                  0.98610733, 0.86296314, 0.3192845,
                  0.84974437, 0.55960762, 0.81264375,
                  0.9685953,  0.69634656, 0.98156571,
                  0.75809291, 0.15779596, 0.78826552,
                  0.42205717, 0.6057628,  0.79793583,
                  0.19698852, 0.7518348,  0.77798001,
                  0.40311648, 0.28829237, 0.90954136,
                  0.32009955, 0.51251015, 0.44992558,
                  0.41725506, 0.42791642, 0.26814589,
                  0.29382634, 0.103745, 0.11347258,
                  0.79507597, 0.46307491, 0.51145213,
                  0.78788667, 0.21338181, 0.40365226,
                  0.58678658, 0.01836139, 0.25714104,
                  0.70919548, 0.68831791, 0.14906229,
                  0.20583127, 0.17497932, 0.78490463,
                  0.93163786, 0.26253747, 0.6608386,
                  0.9802343, 0.93161866, 0.42230004,
                  0.4528885,  0.92858131, 0.23691459,
                  0.80091807, 0.15792865, 0.27055861,
                  0.18443894, 0.3044263,  0.23006992,
                  0.77828035, 0.82431087, 0.35225275,
                  0.43566603, 0.11929511, 0.67476846,
                  0.96745204, 0.3360623,  0.04449883]
        vertices = format_vertices(coordinates, triangles)
        super().__init__(program_id, vertices, colors, GL_TRIANGLES, location)
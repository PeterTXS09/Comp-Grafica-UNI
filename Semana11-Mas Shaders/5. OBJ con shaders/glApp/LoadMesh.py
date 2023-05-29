from OpenGL.GL import *
from .Mesh import *
import numpy as np
import pygame
import random
from .Utils import *



class LoadMesh(Mesh):
    def __init__(self, filename, program_id, draw_type=GL_TRIANGLES, location=pygame.Vector3(0, 0, 0)):
                 #rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 #scale=pygame.Vector3(1, 1, 1)):
        coordinates, triangles = self.load_drawing(filename)
        vertices = format_vertices(coordinates, triangles)
        colors = []
        for i in range(len(vertices)):
            colors.append(random.random())
            colors.append(random.random())
            colors.append(random.random())
        super().__init__(program_id, vertices, colors, draw_type, location)

    def load_drawing(self, filename):
        vertices = []
        triangles = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in line[2:].split()]
                    triangles.append([int(value) for value in t1.split('/')][0]-1)
                    triangles.append([int(value) for value in t2.split('/')][0]-1)
                    triangles.append([int(value) for value in t3.split('/')][0]-1)
                line = fp.readline()
        return vertices, triangles

